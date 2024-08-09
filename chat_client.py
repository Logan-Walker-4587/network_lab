import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(f"\nNew message: {message}")
        except:
            print("Connection closed.")
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 12345
    client_socket.connect((host, port))
    print("Connected to the server")
    
    # Start a thread to handle incoming messages
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()
    
    while True:
        message = input("Enter a message: ")
        client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    start_client()

