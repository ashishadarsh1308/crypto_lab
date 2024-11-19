def generate_key_matrix(key):
    # Remove duplicates, replace J with I, and prepare the key
    key = "".join(dict.fromkeys(key.upper().replace("J", "I")))  # Remove duplicates and replace J with I
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    combined = key + "".join(char for char in alphabet if char not in key)
    
    # Create the 5x5 matrix
    matrix = [list(combined[i:i + 5]) for i in range(0, 25, 5)]
    return matrix

def print_matrix(matrix):
    # Print the matrix in a readable 5x5 format
    print("Playfair Cipher Matrix: \n ")
    for row in matrix:
        print(" ".join(row))
    print()

def find_position(matrix, char):
    # Find the position of a character in the matrix
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def playfair_encrypt(text, key):
    # Prepare the text (replace J with I, handle repeated letters and odd length)
    text = text.upper().replace("J", "I")
    
    # Remove non-alphabet characters
    text = ''.join(filter(str.isalpha, text))
    
    # Handle repeated letters and odd length by adding 'X'
    processed_text = ""
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            processed_text += text[i] + "X"
            i += 1
        elif i + 1 < len(text):
            processed_text += text[i] + text[i + 1]
            i += 2
        else:
            processed_text += text[i] + "X"
            i += 1

    # Generate the Playfair matrix
    matrix = generate_key_matrix(key)
    print_matrix(matrix)  # Print the matrix

    # Encrypt the text in pairs
    encrypted_text = ""
    for i in range(0, len(processed_text), 2):
        char1, char2 = processed_text[i], processed_text[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:  # Same row
            encrypted_text += matrix[row1][(col1 + 1) % 5]
            encrypted_text += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            encrypted_text += matrix[(row1 + 1) % 5][col1]
            encrypted_text += matrix[(row2 + 1) % 5][col2]
        else:  # Rectangle rule
            encrypted_text += matrix[row1][col2]
            encrypted_text += matrix[row2][col1]

    return encrypted_text

def playfair_decrypt(text, key):
    # Generate the Playfair matrix
    matrix = generate_key_matrix(key)
    print_matrix(matrix)  # Print the matrix

    # Decrypt the text in pairs
    decrypted_text = ""
    for i in range(0, len(text), 2):
        char1, char2 = text[i], text[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:  # Same row
            decrypted_text += matrix[row1][(col1 - 1) % 5]
            decrypted_text += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            decrypted_text += matrix[(row1 - 1) % 5][col1]
            decrypted_text += matrix[(row2 - 1) % 5][col2]
        else:  # Rectangle rule
            decrypted_text += matrix[row1][col2]
            decrypted_text += matrix[row2][col1]

    return decrypted_text

# Main Function
def main():
    # print("Choose an option:")
    # print("1. Encrypt plaintext to ciphertext")
    # print("2. Decrypt ciphertext to plaintext")
    choice = '1'

    key = input("Enter the encryption key: ")

    if choice == "1":
        message = input("Enter the plaintext message: ")
        encrypted_message = playfair_encrypt(message, key)
        print(f"Encrypted Ciphertext: {encrypted_message}")
    elif choice == "2":
        message = input("Enter the ciphertext message: ")
        decrypted_message = playfair_decrypt(message, key)
        print(f"Decrypted Plaintext: {decrypted_message}")
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Run the program
main()
