# Function to generate the full key
def generate_key(message, keyword):
    keyword = list(keyword)
    if len(message) == len(keyword):
        return keyword
    else:
        for i in range(len(message) - len(keyword)):
            keyword.append(keyword[i % len(keyword)])
    return "".join(keyword)

# Function to encrypt the message
def encrypt(message, keyword):
    encrypted_text = ""
    key = generate_key(message, keyword)
    for i in range(len(message)):
        if message[i].isalpha():  # Encrypt only alphabetic characters
            ascii_offset = 65 if message[i].isupper() else 97
            encrypted_char = chr((ord(message[i]) - ascii_offset + ord(key[i].lower()) - 97) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += message[i]  # Keep non-alphabetic characters unchanged
    return encrypted_text

# Function to decrypt the message
def decrypt(encrypted_message, keyword):
    decrypted_text = ""
    key = generate_key(encrypted_message, keyword)
    for i in range(len(encrypted_message)):
        if encrypted_message[i].isalpha():  # Decrypt only alphabetic characters
            ascii_offset = 65 if encrypted_message[i].isupper() else 97
            decrypted_char = chr((ord(encrypted_message[i]) - ascii_offset - (ord(key[i].lower()) - 97) + 26) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += encrypted_message[i]  # Keep non-alphabetic characters unchanged
    return decrypted_text

# Input from user
message = input("Enter the message: ")
keyword = input("Enter the keyword: ")

# Encrypt the message
encrypted_message = encrypt(message, keyword)
print("Encrypted Message:", encrypted_message)

# Decrypt the message
decrypted_message = decrypt(encrypted_message, keyword)
print("Decrypted Message:", decrypted_message)
