import socket
import threading

clients = []  # List to keep track of connected clients
clients_lock = threading.Lock()  # Lock to synchronize access to the clients list

def handle_client(client_socket, client_address):
    global clients
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received message: {message} from {client_address}")
            broadcast(message, client_socket)
        except Exception as e:
            print(f"Error handling message from {client_address}: {e}")
            break
    with clients_lock:
        client_socket.close()
        clients.remove(client_socket)
    print(f"Client {client_address} disconnected")

def broadcast(message, sender_socket):
    with clients_lock:
        for client_socket in clients:
            if client_socket != sender_socket:
                try:
                    client_socket.send(message.encode('utf-8'))
                except Exception as e:
                    print(f"Error sending message to a client: {e}")
                    clients.remove(client_socket)

def server_broadcast():
    while True:
        try:
            server_message = input("Enter a message for all clients: ")
            broadcast(f"Server: {server_message}", None)
        except KeyboardInterrupt:
            print("\nServer shutting down...")
            break

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 12346  # Change port to avoid conflict
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Server started and listening for connections...")

    # Start a thread for the server to broadcast messages
    broadcast_thread = threading.Thread(target=server_broadcast)
    broadcast_thread.start()

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            print(f"Client {client_address} connected")
            with clients_lock:
                clients.append(client_socket)
            client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_handler.start()
        except Exception as e:
            print(f"Error accepting connection: {e}")

if __name__ == "__main__":
    start_server()

