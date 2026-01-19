'''
# Function with parameters and arguments in Python
# Parameters are the variables defined in the function definition, and arguments are the values passed to the function when calling it.
# Here is an example of a simple function that takes two parameters and returns their sum.
# Define the function with parameters a and b
# call the function with arguments 3 and 5
# Print the result
# You can call the function with different values of parameters to get the sum of different numbers.
# For example, calling sum(10, 20) will return 30.
# Try calling the function with different arguments to see the results.
'''
# Simple function to add two numbers using user input as parameters and return the result by calling the function with different values of parameters.
def sum(a , b):
    return a + b
input1=int(input("Enter first number:"))
input2 = int(input("Enter second number:"))
result = sum(input1, input2)
print("The sum of given numbers is:", result)

# Parameters are the variables defined in the function definition and arguments are the values passed to the function when calling it.
# Here, input1 and input2 are the arguments passed to the function sum when calling it, and a and b are the parameters defined in the function sum.

# You can call the function with different values of parameters to get the sum of different numbers.
# For example:
result1 = sum(10,20)
print("The sum of 10 and 20 is:", result1)
