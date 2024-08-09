import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    
    host = 'localhost'
    port = 12345
    
    server_socket.bind((host, port))
    
    while True:
        data, address = server_socket.recvfrom(1024)
        print(f"Received number: {data.decode('UTF-8')} from {address}")
        data = int(data.decode('utf-8'))
        if (data%2==0):
               response = "Number is even".encode('utf-8') 
        else:
               response = "Number is odd".encode('utf-8') 
                
        server_socket.sendto(response, address)  
        break

    server_socket.close()


if __name__ == "__main__":
    start_server()


