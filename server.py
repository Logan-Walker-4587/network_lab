import socket
import threading
import json

def handle_client(client_socket):
    request = client_socket.recv(1024)
    message = json.loads(request.decode('utf-8'))
    print(f"Received {message['msg']} from {message['client']}")
    

    client_socket.send(json.dumps({"response": "Message received"}).encode('utf-8'))
    
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 9999))
    server.listen()
    
    print("Server listening on port 9999")
    
    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr[0]}:{addr[1]}")
        
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()

