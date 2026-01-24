'''
History : Python was created by Guido van Rossum and first release in 1991.
Principles : Python follows the principles of simplicity, readability, and explicitness.
Python uses indentation to define code blocks instead of curly braces or keywords.

What is Python Syntax and Variables?
 - Python Syntax is a set of rules that defines how a Python program will be written an interpreted.
 - Variables are used to store data values in a program.

What is indentation in Python?
- Indentation refers to the spaces at the beginning of a code line.
- In python indentation is used to define the structure and hierarchy of the code.
- Proper indentation is crucial in Python as it determines how the code is grouped together.
Example of indentation in Python:
if 5 > 2:
    print("Five is greater than two!")

What is print() function in Python?
- The print() function in Python is used to output data to the standard output device (screen).
- It can print various data types including strings, integers, floats, and more.

What is input() function in Python?
- The input() function in Python is used to take input from the user.

What is eval() function in Python?
- The eval() function in Python is used to evaluate a string as a Python expression and return the result.

'''
# Example of indentation in Python:
if 5 > 2:
    print("Five is greater than two!")

# if 5 > 2:
# print("Five is greater than two!") # This will raise an IndentationError

# Example of input() function in Python:
name = input("Enter your name:")
print("Hello, " + name + "!")
print(name)

a = input("Enter first number:")
b = input("Enter second number:")
sum = int(a) + int(b)
print("The sum of", a, "and", b, "is:", sum)

# # Example of print() function in Python:
print("Hello, World!")
print("Welcome to Python Programming")
print(5 + 3)
print("The sum of 5 and 3 is:", 5 + 3)

# Example of eval() function in Python:
expression = input("Enter a mathematical expression (e.g., 5+3):")
result = eval(expression)
print("The result of the expression is:", result)
