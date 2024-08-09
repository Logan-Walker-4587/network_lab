import socket

def start_client():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    

    host = 'localhost'
    port = 12345
    
 
    client_socket.connect((host, port))
    print("Connected to the server")
    
  
    message = "Hello, Server!".encode('utf-8')
    client_socket.send(message)
    

    response = client_socket.recv(1024).decode('utf-8')
    print(f"Response from server: {response}")
    

    client_socket.close()

if __name__ == "__main__":
    start_client()

