'''
Example of stuents grading calculation using variables and data types in python.
Data Types used in this example are :
1.int
2.float
3.string
4.boolean

'''

# Example using int,float and string
total_marks = 600
gain_marks = 450.50
msg1 = "Congratulation! Pass"
msg2 = "Sorry! Fail"

avg = gain_marks/total_marks * 100

if (avg > 40):
    print(msg1)
else:
    print(msg2)
    

# Example of boolean
x= 20
y = 40       
print(bool(x>y))
print(bool(x<y))


# Example of string concatenation using variables
first_name = "Anup"
last_name = "Karki"
full_name = first_name + "" + last_name
print("Full Name is : ", full_name)
print("Type of full_name variable is : ", type(full_name))
# Above we have concatenated two string variable using + operator.


# Basic Example of variable assignment and printing value and type
a = 10
b = 20.5
c = "Hello Python"
print("Value of a is : ", a)
print("Type of a is : ", type(a))
print("Value of b is : ", b)
print("Type of b is : ", type(b))
print("Value of c is : ", c)
print("Type of c is : ", type(c))
# Above we have assigned int, float and string value to variable and printed their value and type.

