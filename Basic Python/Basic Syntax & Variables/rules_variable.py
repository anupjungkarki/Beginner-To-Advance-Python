'''
Rules of variable declaration in Python:
1. A variable name must start with a letter (a-z, A-Z) or an underscore (_).
2. The rest of the variable name can contain letters, numbers (0-9), or underscores.
3. Variable names are case-sensitive (e.g., myVar and myvar are different variables).
4. Variable names cannot be a reserved keyword in Python (like if, else, while, for, etc.).
5. Variable names should not contain spaces. Use underscores (_) to separate words instead of spaces.
6. Variable names should be descriptive and meaningful to enhance code readability.
# Examples of valid variable names
my_variable = 10
_variable2 = 20
varName = "Hello"
Var123 = 30.5
# Examples of invalid variable names
# 2variable = 10  # Invalid: starts with a number
# my variable = 20  # Invalid: contains a space
# if = 30  # Invalid: 'if' is a reserved keyword
# Demonstration of variable declaration and usage

'''

# Example of variable declaration
x = 5   
y = 10
sum_result = x + y
print("The sum of", x, "and", y, "is:", sum_result)