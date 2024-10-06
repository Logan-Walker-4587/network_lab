import socket

# LZW Decompression Algorithm
def lzw_decompress(compressed):
    # Build the dictionary with single character strings
    dictionary = {i: chr(i) for i in range(256)}
    dict_size = 256
    result = []

    # Get the first code
    w = chr(compressed[0])
    result.append(w)

    for k in compressed[1:]:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError("Bad compressed k: %s" % k)

        result.append(entry)

        # Add w + entry[0] to the dictionary
        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry

    return ''.join(result)

# UDP Server to handle LZW decompression
def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    print("Server is ready and waiting for messages...")

    while True:
        # Receive the compressed data from the client
        compressed_data, client_address = server_socket.recvfrom(1024)
        compressed_data_str = compressed_data.decode()

        # Convert the received string back to a list of integers
        compressed_list = list(map(int, compressed_data_str.split(',')))
        print(f"Received compressed data: {compressed_list} from {client_address}")

        # Decompress the received data using LZW
        decompressed_data = lzw_decompress(compressed_list)
        print(f"Decompressed message: {decompressed_data}")

if __name__ == "__main__":
    server()
