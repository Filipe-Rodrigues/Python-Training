'''
Created on Oct 16, 2020

@author: Filipe
'''

from math import e
from math import cos

def f(x):
    return e ** (-x ** 2)
    #return cos(x)

def simpson38(a, b, k):
    n = 3 * k
    h = (b - a) / n
    integral = f(a) + f(b)
    i = 1
    while i < n:
        if i % 3 == 0:
            integral += 2 * f(a + i * h)
        else:
            integral += 3 * f(a + i * h)
        i += 1
    integral *= h * 3/8
    return integral
    
a = float(input("Interval start: "))
b = float(input("Interval end: "))
k = int(input("Number of subintervals: "))

if a > b:
    a, b = b, a
if k <= 0:
    k = 1;

print("The estimated integral of exp(-x^2) from " + str(a) + " to " + str(b) + " is " + str(simpson38(a, b, k)))
#print("The estimated integral of cos(x) from " + str(a) + " to " + str(b) + " is " + str(simpson38(a, b, k)))