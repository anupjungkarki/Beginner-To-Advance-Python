'''
# Chapter 4 Lab Exercise
1.	Write a Python program using nested if-else statements to determine a student’s grade based on marks: Marks >= 80: A , Marks >= 60: B,Marks >= 40: C , Marks < 40 : F
2.	Write a Python program to find the largest of three numbers entered by the user using if-elif-else.
3.	Write a Python program to check whether a number is prime or not using a loop.
4.	Write a Python program to print all even numbers from 1 to 50 using a while loop.
5.	Write a Python program to check whether a number is palindrome or not.
6.	Write a Python program to print the multiplication table from 1 to 10 using a nested for loop.
7.Write a python program to pring the square pattern 

* * * *
* * * *
* * * *
* * * *
8.	Write a Python program to print a pattern using nested loops:
*
**
***
****
*****
9.Write a Python program to print a following pattern using nested loops:
*****
****
***
**
*
10.Write a Python program to print a follwing pattern using nested loops:
1
22
333
4444
55555

11. Write a Python program to print star pyramid pattern:
    *
   ***
  *****
 *******
*********

12 .Write a python program to print following pattern 
     1
    222
   33333
  4444444
 555555555

14 . Print the follwing pattern 
      *****
       ****
        ***
         **
          *

15. Print the following pattern 
            *
           **
          ***
         ****
        *****

Chapter 5 Lab Exercise
1.Write a Python program to create a function that takes two numbers as parameters and returns their sum.
2.Write a function that accepts a number as argument and checks whether it is prime or not.
3.Write a Python function using assert statement to check that the input number is positive. If not, the program should give an error.
4.Write a Python program to create a function that accepts a string and returns the number of vowels in it.
5.Write a program to demonstrate the use of:Local variable , Global variable
6.Write a recursive function to calculate the factorial of a given number.
7.Write a recursive function to generate the Fibonacci number at position n.
8.Write a recursive function to find the sum of digits of a given number.
9.Write a recursive function to find the sum of first n natural numbers.
Example:
Input: 1234
Output: 10
10.Write a function to calculate the area of a circle. Take radius as parameter.
11.Write a function that takes three numbers and returns the smallest among them.
12.Write a function that accepts a number and prints its multiplication table.
13.Write a recursive function to find LCM of two numbers.
'''
#1.Write a Python program using nested if-else statements to determine a student’s grade based on marks: Marks >= 80: A , Marks >= 60: B,Marks >= 40: C , Marks < 40 : F
marks = int(input("Enter the marks:"))
if marks >= 80:
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 40:
    print("C")
else:
    print("F")


#2.Write a Python program to find the largest of three numbers entered by the user using if-elif-else.
x , y , z = map(int, input("Enter the three number:").split())
if x > y and x > z:
    print(f'x={x} is the greatest number')
elif y > x and y > z:
    print(f'y={y} is the greatest number')
else:
    print(f'z={z} is the greatest number')

#3.Write a Python program to check whether a number is prime or not using a loop.
num = int(input("Enter a number: "))
if num <= 1:
    print("Not Prime")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")

#4.Write a Python program to print all even numbers from 1 to 50 using a while loop.
i= 1
while i<=50:
    if i%2 == 0:
        print(i, end=" ")
    i += 1

#5.Write a Python program to check whether a number is palindrome or not.
num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")

#6.Write a Python program to print the multiplication table from 1 to 10 using a nested for loop.
for i in range(1, 11):     
    print(f"\nMultiplication Table of {i}")
    
    for j in range(1, 11): 
        print(f"{i} x {j} = {i * j}")

# 7.Write a python program to pring the square pattern 
num = 4
for i in range (1 , num + 1):
    for j in range(num):
        print("* ", end="")
    print()

        
# 8.Write a Python program to print a pattern using nested loops:
rows = 5
for i in range(1, rows + 1):        
    for j in range(i):              
        print("*", end="")
    print()                         

# 9.Write a Python program to print a following pattern using nested loops:
num = 5
for i in range(num , 0 , -1):
    for j in range(i):
        print("*" , end="")
    print()

# 10.Write a Python program to print a follwing pattern using nested loops:
rows = 5
for i in range(1, rows + 1):        
    for j in range(i):              
        print(i, end="")
    print() 

# 11. Write a Python program to print star pyramid pattern:
rows = 5
for i in range(1, rows + 1):
    for j in range(rows - i):
        print("", end=" ")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# 12 . Write a python program to print following pattern 
rows = 5
for i in range(1, rows + 1):
    for j in range(rows - i):
        print("", end=" ")
    for k in range(2 * i - 1):
        print(i, end="")
    print()

# 14 . Print the follwing pattern 
rows = 5
for i in range(rows):
    for j in range(i):
        print(" ", end="")
    for k in range(rows - i):
        print("*", end="")
    print()

# 15. Print the following pattern 
rows = 5
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()

######## Chapter 5 Lab Exercise Solution ########
#1.Write a Python program to create a function that takes two numbers as parameters and returns their sum.
def addition(a , b):
    sum = a + b
    return sum
a = int(input("Enter the first number:"))
b= int(input("Enter the second number:"))
res = addition(a, b)
print(f'The sum of {a} and {b} is:', res)

# 2.Write a function that accepts a number as argument and checks whether it is prime or not.
def check_prime(number):
    if number % 2 == 0:
        print(f'{number} is prime!')
    else:
        print(f'{number} is not prime!')
number = int(input("Enter the number to check prime:"))
check_prime(number)

#3.Write a Python function using assert statement to check that the input number is positive. If not, the program should give an error.
def check_positive(num):
    assert num > 0, "Error: Number must be positive!"
    print("The number is positive.")
number = int(input("Enter a number: "))
check_positive(number)

#4.Write a Python program to create a function that accepts a string and returns the number of vowels in it.
def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"
    for ch in text:
        if ch in vowels:
            count += 1     
    return count
string = input("Enter a string: ")
result = count_vowels(string)
print("Number of vowels:", result)

# 5.Write a program to demonstrate the use of:Local variable , Global variable.
num = 2 # Global Variable
def local_function():
    num1 = 10 # Local Variable
    sum = num + num1 # Accessing global variable in function because it can be possible due to global
    print(sum)
local_function()

#6.Write a recursive function to calculate the factorial of a given number.
def rec_factorial(num):
    if num == 1:
        return 1
    else:
        return num * rec_factorial(num - 1)
num = int(input("Enter the number to get factorial:"))
result = rec_factorial(num)
print(result)

# 7.Write a recursive function to generate the Fibonacci number at position n.
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
num = int(input("Enter the number to generate nth positon fibonacci series number:"))
result = fibonacci(num)
print(f'The fibonacci of {num}th positon is:', result)

# 8.Write a recursive function to find the sum of digits of a given number.
def recursive_sum(num):
    if num == 1:
        return 1
    else:
        return num + recursive_sum(num - 1)
num = int(input("Enter the number to get Sum:"))
total = recursive_sum(num)
print("The total sum is:", total)

# 9.Write a recursive function to find the sum of first n natural numbers.
# Example:
# Input: 1234
# Output: 10

def sum_natural(n):
    if n == 1:  # Base case
        return 1
    else:
        return n + sum_natural(n-1) 
num = int(input("Enter a number: "))
print("Sum of first", num, "natural numbers is:", sum_natural(num))

# 10.Write a function to calculate the area of a circle. Take radius as parameter.
pi = 3.14
def area_circle(radius):
    area = pi * radius * radius
    return area
radius = float(input("Enter the radius to calculate the area of circle: "))
result = area_circle(radius)
print("The area of circle is:", result)

#11.Write a function that takes three numbers and returns the smallest among them.
def smallest(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
result = smallest(x, y, z)
print("Smallest number is:", result)

#12.Write a function that accepts a number and prints its multiplication table.
def multiplication_table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)
num = int(input("Enter a number: "))
multiplication_table(num)

#13. Write a recursive function to find LCM of two numbers.
def lcm(a, b):
    if b == 0:  # Base case
        return a
    else:
        return lcm(b, a % b)
a , b = map(int , input("Enter the two natural number to calulate LCM:").split())
res = lcm(a, b)
print("LCM is:", res)