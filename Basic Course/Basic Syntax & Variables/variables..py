'''
In This Section We will learn about the various Python Variables that are used during our course

Let's get into the topic =======>

What is  variables in python ?
Answer :  Python variable are container for storing the data value. Variables do not need to be declared 
with any particular type they are based upon the data value type.

'''
# Simple Example of Integer Varable
a = 5 
b = 6
s = a + b
print(s)


# Simple example of string variable
p = 'Hello World We are Learning Variable In Python Programming Language'
print(p)
print(type(p))  # Just Checking the type of variable


# There are other types variable also we are using in python in most of the case.
m = 2.5 # Float
n = True # Boolean
print(type(m), type(n)) # Just Verify the types of variable


''' 
Let's talk about the variable name declaration method here
1: A variable name must start with a letter or the underscore character but variable
   name can't start with a number (e.g 3MyvariableName) like this.
2: We are allow to use camel case = myVariableName , pascal case = MyVariableName ,
   snake case = my_variable_name any of this form and also underscore at the beginning.

Conculusion : variable name can only contain alpha-numeric characters and underscores.

'''

# We can also declare multiple variable in python
x , y , z = 3 , 'car' , True
print(x,y,z)
print(type(x),type(y),type(z)) # Just Checking the types

# Similary we can also assign the multiple variblable for any data types.