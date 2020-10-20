'''
Created on Oct 15, 2020

@author: Filipe
'''
a = 0
b = 0
c = 0

try:
    coeffs = input("Insert the quadratic formula coefficients: ").split(" ")
    a = float(coeffs[0])
    b = float(coeffs[1])
    c = float(coeffs[2])
    
except:
    print("Hey! The input must be separated by spaces!")
    
else:
    aSign = " + " if a >= 0 else " - "
    bSign = " + " if b >= 0 else " - "
    cSign = " + " if c >= 0 else " - "
    
    delta = b ** 2 - 4 * a * c
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    
    print("The quadratic formula" + aSign + str(abs(a)) + "x^2", end = '')
    print(bSign + str(abs(b)) + "x", end = '')
    print(cSign + str(abs(c)) + " = 0 has the following result:")
    
    if x1 == x2:
        print("x = " + str(x1))
    else:
        print("x1 = " + str(x1))
        print("x2 = " + str(x2))