import socket

# Rail Fence Cipher encryption
def rail_fence_encrypt(text, depth):
    rail = [['' for _ in range(len(text))] for _ in range(depth)]
    
    direction_down = False
    row, col = 0, 0

    for char in text:
        rail[row][col] = char
        col += 1

        if row == 0 or row == depth - 1:
            direction_down = not direction_down

        row += 1 if direction_down else -1

    encrypted_text = []
    for i in range(depth):
        for j in range(len(text)):
            if rail[i][j] != '':
                encrypted_text.append(rail[i][j])

    return ''.join(encrypted_text)


def client():
    server_address = ('localhost', 12345)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Input plain text and depth from the user
    text = input("Enter the plain text: ")
    depth = input("Enter the depth for the Rail Fence Cipher: ")

    # Encrypt the message using Rail Fence Cipher
    encrypted_text = rail_fence_encrypt(text, int(depth))
    print(f"Encrypted message: {encrypted_text}")

    # Send encrypted message and depth to the server
    client_socket.sendto(encrypted_text.encode(), server_address)
    client_socket.sendto(depth.encode(), server_address)

    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    client()
