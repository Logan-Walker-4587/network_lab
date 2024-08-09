import socket

server_address = ('localhost', 12345)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(server_address)

try:
    while True:
        data, address = server_socket.recvfrom(4096)
        print('received {} bytes from {}'.format(len(data), address))
        print(data.decode('utf-8'))
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Closing socket")
    server_socket.close()


