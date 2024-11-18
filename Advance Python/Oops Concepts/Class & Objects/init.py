# Let's Learn about __init__() Method in Python

'''
In Python, __init__() is a special method called a constructor.Constructors are used to initializing the object’s state.
It is automatically invoked when you create an instance of a class.
This method is typically used to initialize the attributes of a class instance.
So, All classes have a function called __init__(), which is always executed when the class is being initiated.

'''

# Example
class Person:
    def __init__(self, name,age,address):
        self.name = name
        self.age = age
        self.address = address
