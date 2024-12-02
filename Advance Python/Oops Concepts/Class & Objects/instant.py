# Let's learn about python instant
'''
In Python ,the term "instance" refers to a specific objects created from a class.
An instance represent one unique realization of the class, with its own attributes
and methods. Essentially , a class is a blueprint , and an instance is an object 
built from that blueprint.

'''

# Example
class People:
    def __init__(self, name ,address):
        # Instance Attributes 
        self.name  = name
        self.address = address

    # Instance Method
    def details(self):
        return f"Name: {self.name} , Address: {self.address}"
    
# Creating Instance of People Class
p1 = People("John" ,"New York")

# Accessing attributes and methods of p1 instance
print(p1.details())