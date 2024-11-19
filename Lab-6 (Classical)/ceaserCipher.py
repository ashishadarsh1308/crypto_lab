# Function to encrypt a message
def encrypt(message, shift):
    encrypted_text = ""
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            # Get the ASCII code of the character
            ascii_offset = 65 if char.isupper() else 97
            # Apply the Caesar Cipher formula
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            # Keep non-alphabetic characters as they are
            encrypted_text += char
    return encrypted_text

# Function to decrypt a message
def decrypt(encrypted_message, shift):
    return encrypt(encrypted_message, -shift)

# Input message and shift from the user
message = input("Enter the message: ")
shift = int(input("Enter the shift value (number of positions to shift): "))

# Encrypt the message
encrypted_message = encrypt(message, shift)
print("Encrypted Message:", encrypted_message)

# Decrypt the message
decrypted_message = decrypt(encrypted_message, shift)
print("Decrypted Message:", decrypted_message)