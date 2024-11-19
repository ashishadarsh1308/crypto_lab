import numpy as np

# Function to preprocess the message
def preprocess_message(message, key_size):
    message = message.lower().replace(" ", "")
    if len(message) % key_size != 0:
        message += 'x' * (key_size - len(message) % key_size)  # Padding with 'x'
    return message

# Function to convert text to numeric values
def text_to_numeric(text):
    return [ord(char) - ord('a') for char in text]

# Function to convert numeric values to text
def numeric_to_text(numeric):
    return ''.join([chr(num + ord('a')) for num in numeric])

# Function to encrypt the message using the Hill Cipher
def encrypt(message, key_matrix):
    key_size = key_matrix.shape[0]
    numeric_message = text_to_numeric(message)
    encrypted_message = []

    # Process message in blocks
    for i in range(0, len(numeric_message), key_size):
        block = numeric_message[i:i + key_size]
        encrypted_block = np.dot(key_matrix, block) % 26
        encrypted_message.extend(encrypted_block)

    return numeric_to_text(encrypted_message)

# Function to decrypt the message using the Hill Cipher
def decrypt(encrypted_message, key_matrix):
    key_size = key_matrix.shape[0]
    numeric_message = text_to_numeric(encrypted_message)

    # Calculate modular inverse of key matrix
    determinant = int(np.round(np.linalg.det(key_matrix))) % 26
    determinant_inverse = pow(determinant, -1, 26)
    adjugate = np.round(np.linalg.inv(key_matrix) * determinant).astype(int) % 26
    inverse_key_matrix = (determinant_inverse * adjugate) % 26

    decrypted_message = []

    # Process message in blocks
    for i in range(0, len(numeric_message), key_size):
        block = numeric_message[i:i + key_size]
        decrypted_block = np.dot(inverse_key_matrix, block) % 26
        decrypted_message.extend(decrypted_block)

    return numeric_to_text(decrypted_message)

# Input message and key
message = input("Enter the message to encrypt: ").replace(" ", "").lower()
key_size = int(input("Enter the key matrix size (e.g., 2 for 2x2): "))

# Input key matrix
print(f"Enter the {key_size}x{key_size} key matrix (row by row):")
key_matrix = []
for i in range(key_size):
    row = list(map(int, input().split()))
    key_matrix.append(row)
key_matrix = np.array(key_matrix)

# Preprocess the message
processed_message = preprocess_message(message, key_size)

# Encrypt the message
encrypted_message = encrypt(processed_message, key_matrix)
print("Encrypted Message:", encrypted_message)

# Decrypt the message
decrypted_message = decrypt(encrypted_message, key_matrix)
print("Decrypted Message:", decrypted_message)
