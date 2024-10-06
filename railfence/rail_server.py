import socket

# Rail Fence Cipher decryption
def rail_fence_decrypt(cipher, depth):
    rail = [['' for _ in range(len(cipher))] for _ in range(depth)]
    
    direction_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        rail[row][col] = '*'
        col += 1

        if row == 0:
            direction_down = True
        elif row == depth - 1:
            direction_down = False

        row += 1 if direction_down else -1

    index = 0
    for i in range(depth):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    decrypted_text = []
    row, col = 0, 0
    for i in range(len(cipher)):
        decrypted_text.append(rail[row][col])
        col += 1

        if row == 0:
            direction_down = True
        elif row == depth - 1:
            direction_down = False

        row += 1 if direction_down else -1

    return ''.join(decrypted_text)


# UDP Server to handle Rail Fence Cipher decryption
def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    print("Server is ready and waiting for messages...")

    while True:
        # Receive the encrypted message and depth from the client
        encrypted_message, client_address = server_socket.recvfrom(1024)
        depth, _ = server_socket.recvfrom(1024)

        encrypted_message = encrypted_message.decode()
        depth = int(depth.decode())

        print(f"Received encrypted message: {encrypted_message} from {client_address}")
        print(f"Received depth: {depth}")

        # Decrypt the message using the Rail Fence Cipher
        decrypted_message = rail_fence_decrypt(encrypted_message, depth)
        print(f"Decrypted message: {decrypted_message}")

        # Server can display the decrypted message (no need to send it back in this case)

if __name__ == "__main__":
    server()
