''' 
There are different data types in assigned python variable and those are identify 
by the nature of data value.
'''

# Number type in Python  (int , float , complex)
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x), type(y), type(z))

# Boolean (True , False)
m = False
n = True
print(type(m))


# Let's cover python casting in this topic
# Python casting is the process of converting one data types to another data types.

# Example
integer = 4 
string = '4567'

to_float_value =  float(integer) # Converts the integer 4 to the float 4.0
print(to_float_value)

to_integer_value = int(string) # Converts the string '4567' to the integer 4567
print(to_integer_value)
