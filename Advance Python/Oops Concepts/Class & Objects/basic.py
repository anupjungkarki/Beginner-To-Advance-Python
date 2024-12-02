# Here We are learning about basic of python OOPs Concepts 

# Define a class Name Student
class Student:
    # Constructor to initialize the attributes 
    def __init__(self, name, age):
        # instance attribute
        self.name = name 
        self.age = age

    #Method to get the name 
    def get_name(self):
        return f"The name of student is {self.name}."
    
    # Method to get age
    def get_age(self):
        return f"{self.name} is {self.age} year's old. "
    
# creating an object instant of the student class 
stu = Student("Anup", 23)

# Access attributes and methods of the object
print(stu.get_name())
print(stu.get_age())


# Let's explain the code how it works

'''
1.Class ( Student): A blueprint for creating objects. It has attributes (name and age) and methods (get_name() and get_age()).
2.Constructor (__init__): The __init__ method initializes name and age when a Student object is created.
3.Object (stu): An instance of the Student class, created with the name "Anup" and age 23.
4.Attributes: Store data related to the object (name and age).
5.Methods: Define behaviors (get_name() and get_age()) of the object.

'''