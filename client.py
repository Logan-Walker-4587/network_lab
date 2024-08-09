import socket
import json

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 9999))
    
    message = {"msg": "Hello, Server!", "client": "Client1"}
    client.send(json.dumps(message).encode('utf-8'))
    
    response = client.recv(1024)
    print(f"Response from server: {response.decode('utf-8')}")
    
    client.close()

if __name__ == "__main__":
    main()

