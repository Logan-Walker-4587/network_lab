import socket
import random

# Function to check if a 7-bit Hamming code contains an error
def check_hamming(hamming_code):
    h = list(map(int, hamming_code))

    p1 = h[0] ^ h[2] ^ h[4] ^ h[6]
    p2 = h[1] ^ h[2] ^ h[5] ^ h[6]
    p3 = h[3] ^ h[4] ^ h[5] ^ h[6]

    # Error position
    error_pos = p1 * 1 + p2 * 2 + p3 * 4
    
    return error_pos

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    host = 'localhost'
    port = 12345

    server_socket.bind((host, port))
    print("Server is listening...")

    while True:
        # Receive the Hamming code from the client
        hamming_code, address = server_socket.recvfrom(1024)
        hamming_code = hamming_code.decode('utf-8')
        print(f"Received Hamming code: {hamming_code} from {address}")

        # Ask whether to introduce an error
        introduce_error = input("Do you want to introduce an error? (yes/no): ").strip().lower()

        if introduce_error == 'yes':
            # Introduce an error by flipping a random bit
            error_bit = random.randint(0, 6)
            hamming_code_list = list(hamming_code)
            hamming_code_list[error_bit] = '1' if hamming_code_list[error_bit] == '0' else '0'
            hamming_code = ''.join(hamming_code_list)
            print(f"Error introduced at bit {error_bit + 1}. Modified code: {hamming_code}")

        # Check if the Hamming code is correct
        error_pos = check_hamming(hamming_code)

        if error_pos == 0:
            result = "No error detected. Codeword is correct."
        else:
            result = f"Error detected at bit position {error_pos}."

        # Send the result back to the client
        server_socket.sendto(result.encode('utf-8'), address)

        break

    server_socket.close()

if __name__ == "__main__":
    start_server()

