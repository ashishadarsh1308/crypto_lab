import math
import random

def gcd(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return b if a == 0 else a

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_random_prime(limit):
    while True:
        num = random.randint(2, limit)
        if is_prime(num):
            return num

# Generate two random prime numbers less than 500
p = generate_random_prime(1000)
print(f"First prime number generated: {p}")

q = generate_random_prime(1000)
while p == q:  # Ensure p and q are different
    q = generate_random_prime(500)
print(f"Second prime number generated: {q}\n")

# Continue with the rest of your code
n = p * q
flag = False

pt = int(input("Enter plaintext in numerical form: "))
if pt >= n:
    flag = True

while flag:
    print("Enter plaintext in numerical form and less than", n)
    pt = int(input(""))
    if pt < n:
        break

print("Original message:", pt)
phi = (p - 1) * (q - 1)
e = 2

while e < phi:
    if gcd(e, phi) == 1:
        break
    e += 1

d = 2
while True:
    if (e * d) % phi == 1:
        break
    d += 1

print("Private key is: (", d, ",", n, ") which is used for signature generation")
print("Public key is: (", e, ",", n, ") which is used for signature verification")

print("Computing signature...\n")
s = (pt ** d) % n

print("Generated signature is:", s)

print("\nVerifying signature...\n")
verification_result = (s ** e) % n

print("Verification result is:", verification_result)
print("Original message is", pt)

if verification_result == pt:
    print("Signature verified\n")
else:
    print("Signature verification unsuccessful\n")
