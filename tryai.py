# Calculator for 4 basic functions

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def power(a,b):
    return a**b

def square(a):
    return a**2

def cube(a):
    return a**3

def root(a):
    return a**(1/2)

def square_root(a):
    return a**(1/3)

def cube_root(a):
    return a**(1/4)

def power_root(a,b):
    return a**(1/b)

def factorial(a):
    return a*factorial(a-1) if a>1 else 1

def fibonacci(n):
    return fibonacci(n-1) + fibonacci(n-2) if n>1 else 1

def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_even(n):
    return n%2==0

def is_odd(n):
    return n%2!=0

def is_positive(n):
    return n>0



















