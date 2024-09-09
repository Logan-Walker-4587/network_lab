import socket

# Functionto calculate the 7-bit Hamming code from a 4-bit dataword
def calculate_hamming(dataword):
    d = list(map(int, dataword))
    
    # Parity bits
    p1 = d[0] ^ d[1] ^ d[3]
    p2 = d[0] ^ d[2] ^ d[3]
    p3 = d[1] ^ d[2] ^ d[3]
    
    # Hamming code is p1 p2 d0 p3 d1 d2 d3
    hamming_code = [p1, p2, d[0], p3, d[1], d[2], d[3]]
    
    return ''.join(map(str, hamming_code))

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    host = 'localhost'
    port = 12345

    client_socket.connect((host, port))
    print("Connected to the server")

    # Input 4-bit dataword from the user
    dataword = input("Enter 4-bit dataword: ")
    
    if len(dataword) != 4 or not all(bit in '01' for bit in dataword):
        print("Invalid dataword. Please enter exactly 4 bits (0 or 1).")
        return

    # Calculate the Hamming code
    hamming_code = calculate_hamming(dataword)
    print(f"Hamming code generated: {hamming_code}")

    # Send the Hamming code to the server
    client_socket.send(hamming_code.encode('utf-8'))

    # Receive the server's response
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Response from server: {response}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
 
