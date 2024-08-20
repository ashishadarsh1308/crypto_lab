import math

def is_equilateral(a, b, c):
    if(a == b and b == c):
        return True
    else:
        return False
    
def is_isoscelees(a, b, c):
    if(a == b or a == c or b == c):
        return True
    else:
        return False
    
def is_scalar(a, b, c):
    if(a != b or a != c or b != c):
        return True
    else:
        return False
    
def is_degenarate(a, b, c):
    if(a+b==c or a+c==b or b+c==a):
        return True 
    else:
        return False

#for a shape to be traingle, all sides to be > 0, sum of lengths of any two sides is >= 3rd side
x = float(input('Enter the value for first side of the triangle: '))
y = float(input('Enter the value for second side of the triangle: '))
z = float(input('Enter the value for third side of the triangle: '))

if (x <= 0 or y <= 0 or z <= 0) or (x+y < z or x+z < y or y+z < x):
        raise ValueError("Invalid input! please try Again")
else:
    print('Is Trianle: True')
    
print('is Equilateral : ', is_equilateral(x,y,z))
print('is Issosceles : ',is_isoscelees(x,y,z))
print('is Scalar : ',is_scalar(x, y,z))
print('is Degenarate : ',is_degenarate(x, y, z))