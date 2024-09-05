import socket
import threading

# Define server address and port
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345
BUFFER_SIZE = 1024

# Get the username from the user
username = input("Enter your username: ")

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def receive_messages():
    """Receive messages from the server."""
    while True:
        try:
            message, _ = client_socket.recvfrom(BUFFER_SIZE)
            print(message.decode('utf-8'))
        except:
            break

def send_messages():
    """Send messages to the server."""
    while True:
        message = input()  # Input from the user
        full_message = f"{username}: {message}"
        client_socket.sendto(full_message.encode('utf-8'), (SERVER_IP, SERVER_PORT))

# Start a thread for receiving messages from the server
receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()

# Main thread handles sending messages
send_messages()

