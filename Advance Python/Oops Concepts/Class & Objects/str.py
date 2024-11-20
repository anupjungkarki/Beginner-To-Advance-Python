# Let's Learn about __str__() Method in Python

'''
The __str__() function in Python is a special method used to define a user-friendly,
readable string representation of an objects. It is automatically called when you pass 
the object to the print() function or use str() on the object.

If __str__() is not defined, the object’s default string representation is used  
then the result will be --> (e.g., <__main__.ClassName object at 0x...>).
'''

# Example

class Account:
    def __init__(self, name , balance):
        self.name = name