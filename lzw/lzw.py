def lzw_compress(uncompressed):
    # Create a dictionary with single characters and their corresponding codes
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256  # The next available code after the initial ASCII table
    current_string = ""
    compressed_data = []

    for char in uncompressed:
        current_string_plus_char = current_string + char
        if current_string_plus_char in dictionary:
            current_string = current_string_plus_char
        else:
            compressed_data.append(dictionary[current_string])
            # Add the new sequence to the dictionary
            dictionary[current_string_plus_char] = next_code
            next_code += 1
            current_string = char

    # Output the code for the last string
    if current_string:
        compressed_data.append(dictionary[current_string])

    return compressed_data


def lzw_decompress(compressed):
    # Create the initial dictionary with single characters
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    current_string = chr(compressed.pop(0))
    decompressed_data = [current_string]

    for code in compressed:
        if code in dictionary:
            entry = dictionary[code]
        elif code == next_code:
            entry = current_string + current_string[0]
        else:
            raise ValueError(f"Bad compressed code: {code}")

        decompressed_data.append(entry)

        # Add new sequence to the dictionary
        dictionary[next_code] = current_string + entry[0]
        next_code += 1

        current_string = entry

    return ''.join(decompressed_data)


# Example usage
if __name__ == "__main__":
    text = input("Enter any text : ")
    print(f"Original text: {text}")

    compressed = lzw_compress(text)
    print(f"Compressed: {compressed}")

    decompressed = lzw_decompress(compressed)
    print(f"Decompressed: {decompressed}")

