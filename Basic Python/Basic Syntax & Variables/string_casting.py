'''
The string casting in Python refers to the process of converting other data types into string data type.
This is often done using the built-in str() function, which takes an object as an argument and returns its string representation.
# Example of String Casting in Python
# Converting Integer to String

'''
num = 100
str_num = str(num)
print(str_num)
print(type(str_num))  # Output: <class 'str'>


'''
Type Casting in Pyhton is of two types
1: Implicit Type Casting
Implicit Type Casting is automatically done by Python when we perform operations involving different data types. Python automatically converts one data type to another without any user intervention.
example of Implicit Type Casting

2: Explicit Type Casting
Explicit Type Casting is also known as Type Conversion where we can convert one data type to another data type by using certain built-in functions like int(), float(), str() etc.
'''

# Example of Explicit Type Casting
# Converting Float to Integer
float_num = 10.75
float_int = int(float_num)
print(float_int)  # Output: 10
print(type(float_int))  # Output: <class 'int'>


# Implicit Type Casting Example
# When an integer and a float are used in an operation, Python automatically converts the integer to a float.
int_num = 5
float_num = 2.5
result = int_num + float_num
print(result)  # Output: 7.5
print(type(result))  # Output: <class 'float'>