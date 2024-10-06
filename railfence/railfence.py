def rail_fence_encrypt(text, depth):
    # Create an empty grid with depth rows and enough columns
    rail = [['' for _ in range(len(text))] for _ in range(depth)]
    
    # Variables to track the direction (up or down the rails) and current row
    direction_down = False
    row, col = 0, 0

    # Fill the rail matrix in a zigzag pattern
    for char in text:
        rail[row][col] = char
        col += 1

        # Change direction when reaching the top or bottom
        if row == 0 or row == depth - 1:
            direction_down = not direction_down

        # Move to the next row based on the direction
        row += 1 if direction_down else -1

    # Read the cipher text row by row
    encrypted_text = []
    for i in range(depth):
        for j in range(len(text)):
            if rail[i][j] != '':
                encrypted_text.append(rail[i][j])

    return ''.join(encrypted_text)


def rail_fence_decrypt(cipher, depth):
    # Create an empty grid with depth rows and enough columns
    rail = [['' for _ in range(len(cipher))] for _ in range(depth)]
    
    # Mark positions in the grid where characters will go (zigzag pattern)
    direction_down = None
    row, col = 0, 0

    for _ in range(len(cipher)):
        rail[row][col] = '*'
        col += 1

        if row == 0:
            direction_down = True
        elif row == depth - 1:
            direction_down = False

        row += 1 if direction_down else -1

    # Now fill the grid with the cipher text
    index = 0
    for i in range(depth):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    # Now read the text in the zigzag manner to decrypt
    decrypted_text = []
    row, col = 0, 0
    for _ in range(len(cipher)):
        decrypted_text.append(rail[row][col])
        col += 1

        if row == 0:
            direction_down = True
        elif row == depth - 1:
            direction_down = False

        row += 1 if direction_down else -1

    return ''.join(decrypted_text)


# Example usage
if __name__ == "__main__":
    text = "HELLOTHERE"
    depth = 3

    encrypted = rail_fence_encrypt(text, depth)
    print(f"Encrypted Text: {encrypted}")

    decrypted = rail_fence_decrypt(encrypted, depth)
    print(f"Decrypted Text: {decrypted}")

