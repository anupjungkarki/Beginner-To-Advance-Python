'''
1.	Write a Python program using nested if-else statements to determine a student’s grade based on marks: Marks >= 80: A , Marks >= 60: B,Marks >= 40: C , Marks < 40 : F
2.	Write a Python program to find the largest of three numbers entered by the user using if-elif-else.
3.	Write a Python program to check whether a number is prime or not using a loop.
4.	Write a Python program to print all even numbers from 1 to 50 using a while loop.
5.	Write a Python program to check whether a number is palindrome or not.
6.	Write a Python program to print the multiplication table from 1 to 10 using a nested for loop.
7.	Write a Python program to print a pattern using nested loops:
*
**
***
****
*****
'''
# 1.Write a Python program using nested if-else statements to determine a student’s grade based on marks: Marks >= 80: A , Marks >= 60: B,Marks >= 40: C , Marks < 40 : F
marks = int(input("Enter the marks:"))
if marks >= 80:
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 40:
    print("C")
else:
    print("F")


#2.	Write a Python program to find the largest of three numbers entered by the user using if-elif-else.
x , y , z = map(int, input("Enter the three number:").split())
if x > y and x > z:
    print(f'x={x} is the greatest number')
elif y > x and y > z:
    print(f'y={y} is the greatest number')
else:
    print(f'z={z} is the greatest number')

# 3.Write a Python program to check whether a number is prime or not using a loop.
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

# 5.Write a Python program to check whether a number is palindrome or not.
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

# 6.Write a Python program to print the multiplication table from 1 to 10 using a nested for loop.
for i in range(1, 11):     
    print(f"\nMultiplication Table of {i}")
    
    for j in range(1, 11): 
        print(f"{i} x {j} = {i * j}")
        
# 7.Write a Python program to print a pattern using nested loops:
rows = 5
for i in range(1, rows + 1):        
    for j in range(i):              
        print("*", end="")
    print()                         