import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message, _ = client_socket.recvfrom(1024)
            print(f"\n{message.decode('utf-8')}")
            print(f"{username}: ", end="")
        except Exception as e:
            print(f"An error occurred while receiving: {e}")
            client_socket.close()
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12345)

    global username
    username = input("Enter your username: ")
    client_socket.sendto(f"{username} joined the chat!".encode('utf-8'), server_address)
    
    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    while True:
        message = input(f"{username}: ")
        if message.lower() == 'exit':
            client_socket.sendto(f"{username} has left the chat.".encode('utf-8'), server_address)
            break
        client_socket.sendto(f"{username}: {message}".encode('utf-8'), server_address)

    client_socket.close()

if __name__ == "__main__":
    start_client()
