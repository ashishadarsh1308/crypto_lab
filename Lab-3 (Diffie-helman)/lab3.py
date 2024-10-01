def primitiveRootOfp(n):
	for i in range(1,n-1):
		s=set()
		flag=True
		for j in range(0,n-2):
			if (i**j)%n in s:
				flag=False
				break
			s.add((i**j) % n)
		if flag==True:
			return i



def prime(num):
	for i in range(2,num):
		if num%i==0:
			return False
	
	return True
	
	
p=int(input("Enter prime number: "))

isPrime=prime(p)

while isPrime==False:
	p=int(input("Enter prime number again because entered number is not prime :"))
	isPrime=prime(p)
g=primitiveRootOfp(p)

a=int(input("Enter secret key for sender\n"));
b=int(input("Enter secret key for receiver\n"));

A=(g**a) % p
B=(g**b) % p



Kab=(B**a) % p
Kba=(A**b) % p

print("Secret key for Alice is:", Kab)
print("Secret key for Bob is:", Kba)

if Kab==Kba:
	print("Key exchange is successfull and Common secret key is : ",Kab)
else:
	print("Key exchange unsuccessfull\n")
