# Let's Learn about self parameter in python

'''
The keyword self in Python is a reference to the current instance of the class.
It is used to access the attributes and methods of the class within its own methods.
When a method is called on an object, self is automatically passed to that method to represent the instance that invoked it.


===== Key Points About self =====

1. Represents the Instance: self allows you to refer to the current object. For example, if you create two objects obj1 and obj2, self
will refer to obj1 when a method is called on it, and obj2 when a method is called on obj2.

2.Defines Instance Attributes: You use self to define or access instance attributes, which are unique to each object of the class.
For example, self.attribute_name = value sets an attribute for the object.

3.Mandatory in Instance Methods: It must be the first parameter of instance methods in Python (although you can name it something else, by convention it is always self).

4.Not Required for Class Methods or Static Methods: Class methods use cls instead of self.
Static methods don’t require self because they don’t operate on an instance of the class.

'''

# Example
class AccountHolder:
    def __init__(self,name,balance):
        # Use 'self' to define instant attributes
        self.name = name
        self.balance = balance

    def check_balance(self):
        print(f"The balance of {self.name} is ${self.balance}.")

# Creating two instance of the class
p1 = AccountHolder("Anup" , 2000)
p2 = AccountHolder("Hari" , 4000)

# Calling Method on the object
p1.check_balance()
p2.check_balance()


'''
=== What Happen Without Self ===
If you try to define a method without using self to access attributes, Python will raise an
error because the method won't know which object's attributes to reference.

'''
