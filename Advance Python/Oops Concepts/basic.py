# Here We are learning about basic of python OOPs Concepts 

# Define a class Name Student
class Student:
    # Constructor to initialize the attributes 
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    #Method 
    def get_name(self):
        return f"The name of student is {self.name} ."
    
    # Method to get age
    def get_age(self):
        return f"{self.name} is {self.age} year's old . "
    
# creating an object  instant of the student class 

obj = Student("Anup", 23)
print(obj.get_name)