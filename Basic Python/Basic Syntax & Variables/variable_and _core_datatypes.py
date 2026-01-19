''' 
Variable in Python?
A variable is a reserved memory location to store values. In other words, a variable in a python program gives data to the computer for processing.
When we create a variable, we reserve some space in memory.
You can think of variables as containers that hold data values.

'''

'''
===================================Python Core Data Types ====================================
Data Types in Python?
Python has various standard data types that are used to define the operations possible on them and the storage method for each of them.
Here are some of the most commonly used data types in Python:
1. Numeric Types:
    - int : Integer values (e.g., 1, -5, 100)
    -float : Floating-point numbers (e.g., 3.14, -0.001, 2.0)
    -complex : Complex numbers (e.g., 2 + 3j, -1 + 0j)
2. Sequence Types:
    -list : Ordered, mutable collection of items (e.g., [1, 2, 3], ['apple', 'banana'])
    -tuple : Ordered, immutable collection of items (e.g., (1, 2, 3), ('a', 'b', 'c'))
    -range : Represents a sequence of numbers (e.g., range(0,10))
3. Text Type:
    -str : String, a sequence of characters (e.g., "Hello, World!", 'Python')
4. Set Types:
    -set : Unordered collection of unique items (e.g., {1, 2, 3}, {'apple', 'banana'})
    -frozenset : Immutable version of a set (e.g., frozenset({1, 2, 3}))
5. Mapping Type:
    -dict : Collection of key-value pairs (e.g., {'name': 'Alice', 'age': 25})
6. Boolean Type:
    -bool : Represents True or False values (e.g., True , False)
7. Binary Types:
    -butes : Immutable sequence of bytes (e.g., b'Hello')
    -bytearray : Mutable sequence of bytes (e.g., bytearray(b'Hello'))
    -memoryview : Memory view object of a bytes-like object (e.g., memoryview(b 'Hello'))
Each data type serves a specific purpose and has its own set of operations that can be performed on it.
for example, you can perform arithmetic operations on numeric types, concatenate strings, and manipulate lists and dictionaries.

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

a = 10
b = 3
print(bool(a > b))
print(bool(a < b))


# Let's cover python type casting in this topic
# Python casting is the process of converting one data types to another data types.

# Example
integer = 4 
string = '4567'

to_float_value =  float(integer) # Converts the integer 4 to the float 4.0
print(to_float_value)

to_integer_value = int(string) # Converts the string '4567' to the integer 4567
print(to_integer_value)
