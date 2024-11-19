def caesar_cipher(text, shift):
    result = ""

    # Loop through each character in the text
    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Non-alphabetical characters remain unchanged
        else:
            result += char
    
    return result

# Example usage
plaintext = input("Enter the message: ")
shift_value = 3  # You can change this value to shift by a different number

ciphertext = caesar_cipher(plaintext, shift_value)
print("Encrypted text:", ciphertext)

# Decrypting the ciphertext (shift in the opposite direction)
decrypted_text = caesar_cipher(ciphertext, -shift_value)
print("Decrypted text:", decrypted_text)
