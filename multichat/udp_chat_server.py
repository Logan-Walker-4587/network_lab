import socket
import threading

# Define server address and port
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345
BUFFER_SIZE = 1024

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server address
server_socket.bind((SERVER_IP, SERVER_PORT))

clients = set()  # Set to store unique client addresses

print(f"Server started on {SERVER_IP}:{SERVER_PORT}")

def broadcast_message(message, sender_address):
    """Broadcast message to all clients except the sender."""
    for client in clients:
        if client != sender_address:
            try:
                server_socket.sendto(message, client)  # Send to other clients
            except Exception as e:
                print(f"Failed to send message to {client}: {e}")

def handle_client():
    while True:
        # Receive message from client
        try:
            message, client_address = server_socket.recvfrom(BUFFER_SIZE)

            # Add the client address to the set of connected clients
            clients.add(client_address)

            # Print the received message
            print(f"Message from {client_address}: {message.decode('utf-8')}")

            # Broadcast the message to all other clients
            broadcast_message(message, client_address)

        except Exception as e:
            print(f"Error receiving message: {e}")

# Start the server to handle clients in a separate thread
server_thread = threading.Thread(target=handle_client)
server_thread.daemon = True
server_thread.start()

# Keep the server running indefinitely
while True:
    pass

