# Function to generate the Playfair cipher key matrix
def generate_key_matrix(keyword):
    matrix = []
    seen = set()
    keyword = keyword.replace("j", "i").lower()  # Treat 'j' as 'i'
    for char in keyword + "abcdefghiklmnopqrstuvwxyz":  # Append alphabet
        if char not in seen:
            seen.add(char)
            matrix.append(char)
    return [matrix[i:i + 5] for i in range(0, 25, 5)]  # Create 5x5 matrix

# Function to process the plaintext
def preprocess_message(message):
    message = message.replace("j", "i").lower()
    processed_message = ""
    i = 0
    while i < len(message):
        if i + 1 < len(message) and message[i] == message[i + 1]:
            processed_message += message[i] + 'x'  # Insert 'x' between duplicates
            i += 1
        else:
            processed_message += message[i]
            i += 1
    if len(processed_message) % 2 != 0:
        processed_message += 'x'  # Add 'x' if length is odd
    return processed_message

# Function to find the position of a character in the matrix
def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

# Function to encrypt the plaintext using the Playfair cipher
def encrypt(message, key_matrix):
    encrypted_message = ""
    for i in range(0, len(message), 2):
        row1, col1 = find_position(key_matrix, message[i])
        row2, col2 = find_position(key_matrix, message[i + 1])
        
        if row1 == row2:  # Same row
            encrypted_message += key_matrix[row1][(col1 + 1) % 5]
            encrypted_message += key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            encrypted_message += key_matrix[(row1 + 1) % 5][col1]
            encrypted_message += key_matrix[(row2 + 1) % 5][col2]
        else:  # Rectangle rule
            encrypted_message += key_matrix[row1][col2]
            encrypted_message += key_matrix[row2][col1]
    return encrypted_message

# Input message and keyword
message = input("Enter the message to encrypt: ").replace(" ", "").lower()
keyword = input("Enter the keyword: ").replace(" ", "").lower()

# Generate key matrix
key_matrix = generate_key_matrix(keyword)

# Preprocess message
processed_message = preprocess_message(message)

# Encrypt the message
encrypted_message = encrypt(processed_message, key_matrix)

print("Key Matrix:")
for row in key_matrix:
    print(row)

print("\nProcessed Message:", processed_message)
print("Encrypted Message:", encrypted_message)
