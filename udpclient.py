import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 12345)
message = "Hello server".encode('UTF-8')

try:
    print(f"sending message = {message}")
    sent = sock.sendto(message, server_address)

finally:
    print('closing socket')
    sock.close()

