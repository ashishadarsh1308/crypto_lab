import math

def gcd(a, h):
    temp = 0
    while(1):
        temp = a%h
        if(temp == 0):
            return h
        
p = 3
q = 7
n = p*q
e=2
phi = (p-1)*(q-1)

while(e<phi):
    if(gcd(e, phi)):
        break
    else:
        e+1
        
k = 2
d = (1+(k*phi))/e

msg = 12

print('message data = ', msg)

#encryption
c = pow(msg, e)
c = math.fmod(c,n)
print("entrypted message: ", c)

#decryption
m = pow(c,d)
m = math.fmod(m,n)
print("original message sent: ", m)