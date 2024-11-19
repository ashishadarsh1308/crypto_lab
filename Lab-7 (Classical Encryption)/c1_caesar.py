def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

# Main Function
def main():
    print("Choose an option:")
    print("1. Encrypt plaintext to ciphertext")
    print("2. Decrypt ciphertext to plaintext")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        message = input("Enter the plaintext message: ")
        shift = int(input("Enter the shift value: "))
        encrypted = caesar_cipher_encrypt(message, shift)
        print(f"Encrypted Ciphertext: {encrypted}")
    elif choice == "2":
        message = input("Enter the ciphertext message: ")
        shift = int(input("Enter the shift value: "))
        decrypted = caesar_cipher_decrypt(message, shift)
        print(f"Decrypted Plaintext: {decrypted}")
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Run the program
main()
