# Let's Learn about class and object in pyhton in details 

'''
Class : A class is a collection of objects. A class contains the blueprints or the prototype from which the objects are being created. 
It is a logical entity that contains some attributes and methods. 

Objects : An object is called an instance of a class. In object oriented programming Python, The object is an entity that has
a state and behavior associated with it. It may be any real-world object like a mouse, keyboard, chair, table, pen, etc

'''

# Simple Example

# Defining a class name Car
class Car:
    # The __init__ method is a constructor that initializes object attributes 
    def __init__(self, name, model,year):
        # Instance Variables
        self.name = name 
        self.model = model
        self.year = year
        
    # Methods to display car details
    def display_info(self):
        return f"{self.year} {self.name} { self.model}"
    
    # Method for simulate the car honking 
    def honk(self):
        return "Beep! Beep!"
    
# Creating objects (instances) of the Car class
c1 = Car("Toyata","Corolla",2020)
c2 = Car("Honda","Civic",2024)

# Accessing objects attributes and methods
print(c1.display_info())
print(c1.honk())

# Let's explain the code how it works
'''
1.Class Definition (Car): We define a class named Car that has three instance attributes: make, model, and year.
2.Constructor Method (__init__): This method is called when a new instance of Car is created.
 It initializes the object with make, model, and year.
3.Instance Methods (display_info and honk): These methods allow each Car object to display its details and honk.
'''
