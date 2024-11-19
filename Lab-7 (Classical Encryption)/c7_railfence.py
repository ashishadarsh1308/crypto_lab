# Function to encrypt the plaintext using the Rail Fence Cipher
def railfence_encrypt(plaintext, rails):
    # Create a matrix with 'rails' number of rows and 'len(plaintext)' columns
    matrix = [['' for _ in range(len(plaintext))] for _ in range(rails)]
    
    # Initialize row and column indices
    row, col = 0, 0
    direction = 1  # 1 means moving downwards, -1 means moving upwards

    # Place the characters in the matrix in a zigzag pattern
    for char in plaintext:
        matrix[row][col] = char
        col += 1

        # If we reach the top or bottom row, we reverse the direction
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        
        row += direction

    # Read the matrix row by row to get the ciphertext
    ciphertext = ''.join(''.join(row) for row in matrix)
    return ciphertext

# Function to decrypt the ciphertext using the Rail Fence Cipher
def railfence_decrypt(ciphertext, rails):
    # Create a matrix with 'rails' number of rows and 'len(ciphertext)' columns
    matrix = [['' for _ in range(len(ciphertext))] for _ in range(rails)]
    
    # Initialize row and column indices
    row, col = 0, 0
    direction = 1  # 1 means moving downwards, -1 means moving upwards

    # Mark the positions in the matrix that will hold the ciphertext characters
    for i in range(len(ciphertext)):
        matrix[row][col] = '*'
        col += 1

        # If we reach the top or bottom row, we reverse the direction
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        
        row += direction

    # Fill the matrix with the ciphertext characters
    index = 0
    for r in range(rails):
        for c in range(len(ciphertext)):
            if matrix[r][c] == '*':
                matrix[r][c] = ciphertext[index]
                index += 1

    # Read the matrix in a zigzag pattern to get the plaintext
    plaintext = []
    row, col = 0, 0
    direction = 1
    for i in range(len(ciphertext)):
        plaintext.append(matrix[row][col])
        col += 1

        # If we reach the top or bottom row, we reverse the direction
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        
        row += direction

    return ''.join(plaintext)

# Example usage:
def main():
    plaintext = input("Enter the plaintext to encrypt: ")
    rails = 2
    
    # Encrypt the plaintext
    ciphertext = railfence_encrypt(plaintext, rails)
    print(f"Encrypted ciphertext: {ciphertext}")
    
    # Decrypt the ciphertext back to plaintext
    decrypted_text = railfence_decrypt(ciphertext, rails)
    print(f"Decrypted plaintext: {decrypted_text}")

if __name__ == "__main__":
    main()
