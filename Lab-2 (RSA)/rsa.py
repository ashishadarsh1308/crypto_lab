# For the evaluation

import math

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def modInverse(a, m): 
    a = a % m
    for x in range(m):
        if (a * x) % m == 1:
            return x
    return -1  # No modular inverse exists

def RSA(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17  # Common choice for e, can be any small prime > 1
    
    while e < phi:
        if gcd(e, phi) == 1:
            break
        else:
            e += 1

    d = modInverse(e, phi)
    if d == -1:
        print("Inverse doesn't exist")
        return
    
    print("Public key -> (", e, ",", n, ")")
    print("Private key -> (", d, ",", n, ")")

    # Message (m) should be less than n
    m = int(input("Enter a message (as a number) less than n -> "))
    if m >= n:
        print("Message must be less than n")
        return
    
    c = pow(m, e, n)  # Encrypt
    print("Cipher text ->", c)
    
    m = pow(c, d, n)  # Decrypt
    print("Plain text ->", m)

def checkPrime(n):
    cnt = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            cnt += 1
            if n // i != i:
                cnt += 1

    return cnt == 2

p = int(input("Enter the value of p -> "))
while not checkPrime(p):
    p = int(input("Enter a prime value for p -> "))

q = int(input("Enter the value of q -> "))
while not checkPrime(q):
    q = int(input("Enter a prime value for q -> "))

RSA(p, q)
