# Program to take input from the user and display it back to the user.
user_input = input("Please enter something: ")
print("You entered:", user_input)

# # Program to take two numbers as input from the user and display their sum.
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
sum = float(num1) + float(num2)
print("The sum of", num1, "and", num2, "is:", sum)
# Note: The input() function takes input as a string by default.
# To perform arithmetic operations, we need to convert the input strings to numbers (int or float).


# Taking multiple input in same line 
a , b = map(int, input("Enter number first and second:").split())
sum  = a + b
print(sum)