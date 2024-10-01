import random

def soe():
    # Sieve of Eratosthenes to generate prime numbers up to 10000
    isPrime = [True] * 10001
    isPrime[0] = isPrime[1] = False

    for i in range(2, 100):
        if isPrime[i]:
            for j in range(i * i, 10001, i):
                isPrime[j] = False

    prime = []
    for i in range(10001):
        if isPrime[i]:
            prime.append(i)

    return prime

# Generate the list of prime numbers
primes = soe()
size = len(primes)

# Select a random prime number 'p'
primeNumberIndex = random.randint(size - 100, size - 2)
p = primes[primeNumberIndex]
print("p: ", p)

def findRandomNumber(max_value):
    return random.randint(2, max_value)

# Generate random values for alpha and private keys
alpha = findRandomNumber(p - 1)
print("alpha: ", alpha)

bobPrivateKey = findRandomNumber(p - 2)
print("bobPrivateKey: ", bobPrivateKey)

bobPublicKey = pow(alpha, bobPrivateKey, p)
print("bobPublicKey: ", bobPublicKey)

alicePrivateKey = findRandomNumber(p - 2)
print("alicePrivateKey: ", alicePrivateKey)

alicePublicKey = pow(alpha, alicePrivateKey, p)
print("alicePublicKey: ", alicePublicKey)

# Generate the masking key
maskingKey = pow(bobPublicKey, alicePrivateKey, p)
print("maskingKey: ", maskingKey)

# Input a message from the user
message = int(input("enter a number: "))
print("message: ", message)

# Encrypt the message
cipherText = (message * maskingKey) % p
print("cipherText: ", cipherText)

# Calculate a new masking key
newMaskingKey = pow(alicePublicKey, bobPrivateKey, p)
print("newMaskingKey: ", newMaskingKey)

def calculateModuloInverse(num, p):
    # Calculate the modular inverse using the Extended Euclidean algorithm
    for i in range(1, p):
        if (num * i) % p == 1:
            return i
    return None  # Return None if no inverse exists

# Calculate the modular inverse of the new masking key
moduloInverse = calculateModuloInverse(newMaskingKey, p)
print("moduloInverse: ", moduloInverse)

# Decrypt the message if the modular inverse exists
if moduloInverse is not None:
    decryptedMessage = (cipherText * moduloInverse) % p
    print("decryptedMessage: ", decryptedMessage)
else:
    print("No modular inverse exists; decryption failed.")
