import math
def gcd(a,b):
    if(a==0):
        return b
    return gcd(b%a,a)

def modInverse(a,m): 
    a = a % m
    for x in range(m):
        # print(x)
        if ((a * x) % m == 1):
            return x
    return -1 #No modular inverse exists


def RSA(p,q):
    bit_length_p= p.bit_length()
    bit_length_q=q.bit_length()
    # print("bit lenght",bit_length_p,"   ",bit_length_q)
    n=p*q
    phi=(p-1)*(q-1)
    e=17   #2<=e<phi
    while(e<phi):
        if(gcd(e,phi)==1):
            break;
        else:
            e=e+1

    d=modInverse(e,phi)
    if(d==-1):
        print("inverse doesn't exist");
        return
    print("public key ->(",e,",",n,")")
    print("private key ->(",d,",",n,")")

    # m should be less than n
    m=65#for 'HI'
    c=pow(m,e)%n
    # print(c)
    print("cipher text ->",c)
    m=pow(c,d)%n
    print("plain text",m)


def checkPrime(n):
    # Initialize a counter variable to
    # count the number of factors.
    cnt = 0

    # Loop through numbers from 1
    # to the square root of n.
    for i in range(1, int(math.sqrt(n)) + 1):
        # If n is divisible by i
        # without any remainder.
        if n % i == 0:
            # Increment the counter.
            cnt = cnt + 1

            # If n is not a perfect square,
            # count its reciprocal factor.
            if n // i != i:
                cnt = cnt + 1

    # If the number of
    # factors is exactly 2.
    if cnt == 2:
         # Return true, indicating
         # that the number is prime.
        return True
    # If the number of
    # factors is not 2.
    else: 
        # Return false, indicating
        # that the number is not prime.
        return False
    
p=int(input("enter the value of p ->"))
while not checkPrime(p):
      p=int(input("enter the value of p ->"))

q=int(input("enter the value of q->"))
while not checkPrime(q):
      q=int(input("enter the value of q ->"))
RSA(p,q)