import socket

# LZW Compression Algorithm
def lzw_compress(uncompressed):
    # Build the dictionary with single character strings
    dictionary = {chr(i): i for i in range(256)}
    dict_size = 256
    w = ""
    compressed_data = []

    for char in uncompressed:
        wc = w + char
        if wc in dictionary:
            w = wc
        else:
            compressed_data.append(dictionary[w])
            dictionary[wc] = dict_size
            dict_size += 1
            w = char

    # Output the code for w
    if w:
        compressed_data.append(dictionary[w])

    return compressed_data


def client():
    server_address = ('localhost', 12345)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Input the text from the user
    text = input("Enter the text to compress using LZW: ")

    # Compress the text using LZW
    compressed_data = lzw_compress(text)
    compressed_data_str = ','.join(map(str, compressed_data))  # Convert list to string for transmission
    print(f"Compressed data: {compressed_data_str}")

    # Send the compressed data to the server
    client_socket.sendto(compressed_data_str.encode(), server_address)

    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    client()
