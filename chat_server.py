import socket
import threading

clients = []

def broadcast(message, sender_address):
    print(f"Broadcasting message from {sender_address}: {message.decode('utf-8')}")
    for client in clients:
        if client != sender_address:
            try:
                server_socket.sendto(message, client)
            except Exception as e:
                print(f"Failed to send message to {client}: {e}")
                clients.remove(client)

def handle_server_input():
    while True:
        message = input("Server: ")
        broadcast(f"Server: {message}".encode('utf-8'), None)

def start_server():
    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 12345))

    print("Server is running...")

    threading.Thread(target=handle_server_input).start()

    while True:
        message, client_address = server_socket.recvfrom(1024)
        if client_address not in clients:
            clients.append(client_address)
            print(f"New client connected: {client_address}")
        
        broadcast(message, client_address)

if __name__ == "__main__":
    start_server()
