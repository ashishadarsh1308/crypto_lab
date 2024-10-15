import random

def is_prime(n):
    """ Check if a number is prime. """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_random_number(max_value):
    """ Generate a random number between 2 and max_value. """
    return random.randint(2, max_value)

def calculate_modulo_inverse(num, p):
    """ Calculate the modular inverse using the Extended Euclidean algorithm. """
    for i in range(1, p):
        if (num * i) % p == 1:
            return i
    return None  # Return None if no inverse exists

# Input for prime number p
p = int(input("Enter a large prime number (p): "))
if not is_prime(p):
    print(f"{p} is not a prime number. Exiting.")
    exit()

# Input for generator alpha
alpha = int(input(f"Enter a generator (alpha) for the group Z_{p}^*: "))
if not (1 < alpha < p):
    print(f"{alpha} is not a valid generator. Exiting.")
    exit()

# Generate random values for private keys
bob_private_key = find_random_number(p - 2)
print("bobPrivateKey:", bob_private_key)

bob_public_key = pow(alpha, bob_private_key, p)
print("bobPublicKey:", bob_public_key)

alice_private_key = find_random_number(p - 2)
print("alicePrivateKey:", alice_private_key)

alice_public_key = pow(alpha, alice_private_key, p)
print("alicePublicKey:", alice_public_key)

# Generate the masking key
masking_key = pow(bob_public_key, alice_private_key, p)
print("maskingKey:", masking_key)

# Input a message from the user
message = int(input("Enter a number to encrypt: "))
print("message:", message)

# Encrypt the message
cipher_text = (message * masking_key) % p
print("cipherText:", cipher_text)

# Calculate a new masking key
new_masking_key = pow(alice_public_key, bob_private_key, p)
print("newMaskingKey:", new_masking_key)

# Calculate the modular inverse of the new masking key
modulo_inverse = calculate_modulo_inverse(new_masking_key, p)
print("moduloInverse:", modulo_inverse)

# Decrypt the message if the modular inverse exists
if modulo_inverse is not None:
    decrypted_message = (cipher_text * modulo_inverse) % p
    print("decryptedMessage:", decrypted_message)
else:
    print("No modular inverse exists; decryption failed.")