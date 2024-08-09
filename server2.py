import socket

def start_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    

    host = 'localhost'
    port = 12345
    

    server_socket.bind((host, port))
    

    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")
    
    while True:
 
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established.")
        

        message = client_socket.recv(1024).decode('utf-8')
        print(f"Received message: {message}")
        

        response = "Message received".encode('utf-8')
        client_socket.send(response)
        

        client_socket.close()

if __name__ == "__main__":
    start_server()

