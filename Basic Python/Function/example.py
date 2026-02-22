# This is a simple function that adds two numbers and returns the result by calling the function.
def add(a , b):
    return a + b
result = add(3,5)
print("The sum of 3 and 5 is:", result)

# SIMPLE PROGRAM
def msg():
    print("Hello World!")
msg()

# Simple example without using function return 
def addition(a , b):
    sum = a + b
    print(f'The sum of {a} and {b} is:',sum)
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
addition(a, b)

# Simple addition using funcion return 
def addition(a , b):
    sum = a + b
    return sum 
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
total = addition(a, b)
print(f'The sum of {a} and {b} is:',total)

# Example of Positional Argument
def person(name , age):
    print(f'I am {name} and {age} yrs old')
person("Ram", 32)

# Example of Keyword Argument
def person(name , age):
    print(f'I am {name} and {age} yrs old')
person(age = 32 ,name="Ram")

# **kwargs
def info(**data):
    print(data)
info(name="Ram", age=20, city="Kathmandu")


# *args
def total(*num):
    print(num)

total(1,2,3,4)

