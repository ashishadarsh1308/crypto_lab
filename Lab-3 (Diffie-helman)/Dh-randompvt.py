# import math module
from math import sqrt
import random

# Prime number -> a number that is greater than 1 and has no positive divisors other than 1 and itself
def checkPrime(num):
    if num > 1:
        for i in range(2, int(sqrt(num))+1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

someCoprimeOfn = []
def is_primitive_root(g, n):
    """Check if g is a primitive root modulo n"""
    if gcd(g, n) != 1:
        return False
    
    phi_n = n-1
    divisors = []
    # Find all divisors of φ(n)
    for i in range(1, int(sqrt(phi_n)) + 1):
        if phi_n % i == 0:
            divisors.append(i)
            if i != phi_n // i:
                divisors.append(phi_n // i)
    
    # Check the order of g
    print(f"Divisors of {phi_n} are {divisors}")
    for d in divisors:
        coprimeOfn = pow(g, d, n)
        someCoprimeOfn.append(coprimeOfn)
        if coprimeOfn == 1:
            if d != phi_n:
                return False
    
    return True


# Alice class
class Alice:
    def __init__(self, n, g):
        self.n = n
        self.g = g
        self.public_key_a, self.__private_key_a = self.generate_alice_keys(n, g)
    
    def get_public_key(self):
        return self.public_key_a
    
    def get_private_key(self):
        return self.__private_key_a
    
    def generate_alice_keys(self, n, g):
        private_key_a = self.generate_random_private_key(n)
        public_key_a = pow(g, private_key_a, n)
        print(f"------------Private key implemented using random number below {n}------------------")
        print(f"Alice's public key is {public_key_a}")
        return public_key_a, private_key_a
    
    def generate_random_private_key(self, n):
        private_key_a = random.randint(1, n-1)
        while not checkPrime(private_key_a):
            private_key_a = random.randint(1, n-1)
        # print(f"Alice's private key is {private_key_a}")
        return private_key_a
    
    def generate_alice_secret_key(self, public_key_b):
        return pow(public_key_b, self.__private_key_a, self.n)


# Bob class
class Bob:
    def __init__(self, n, g):
        self.n = n
        self.g = g
        self.public_key_b, self.__private_key_b = self.generate_bob_keys(n, g)
    
    def get_public_key(self):
        return self.public_key_b
    
    def get_private_key(self):
        return self.__private_key_b
    
    def generate_bob_keys(self, n, g):
        private_key_b = self.generate_random_private_key(n)
        public_key_b = pow(g, private_key_b, n)
        
        print(f"Bob's public key is {public_key_b}")
        return public_key_b, private_key_b
    
    def generate_random_private_key(self, n):
        private_key_b = random.randint(1, n-1)
        while not checkPrime(private_key_b):
            private_key_b = random.randint(1, n-1)
        
        return private_key_b
    
    def generate_bob_secret_key(self, public_key_a):
        return pow(public_key_a, self.__private_key_b, self.n)


# Diffie-Hellman Key Exchange
def main():
    n = int(input("Enter a prime number n: ")) # prime number
    while not checkPrime(n): # if n is not a prime number
        n = int(input(f"{n} is not a prime number, please enter a valid prime number: "))

    g = int(input("Enter a primitive root g modulo n: ")) # primitive root
    while not is_primitive_root(g, n): # if g is not a primitive root
        g = int(input(f"{g} is not a primitive root, please enter a valid number: "))

    alice = Alice(n, g) # Alice object
    bob = Bob(n, g) # Bob object

    # Public and private keys of Alice and Bob
    # print(f"Alice's private key is {alice.get_private_key()}")
    # print(f"Bob's private key is {bob.get_private_key()}")

    # print(f"Alice's public key is {alice.get_public_key()}")
    # print(f"Bob's public key is {bob.get_public_key()}")

    # Shared secret key
    shared_secret_key_a = alice.generate_alice_secret_key(bob.get_public_key())
    shared_secret_key_b = bob.generate_bob_secret_key(alice.get_public_key())

    print(f"Alice's shared secret key is {shared_secret_key_a}")
    print(f"Bob's shared secret key is {shared_secret_key_b}")
    print(f"Alice and Bob now have a shared secret key {shared_secret_key_a} that they can use to encrypt and decrypt messages.")

if __name__ == "__main__":
    main()
