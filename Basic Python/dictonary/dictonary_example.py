# Accessing Dictonary Value  using Square Brackets []
person = {"name":"Anup karki",
          "age":10,
          "gender":"Male",
          "profession":"Student"
          }
access_name = person["name"]
# using get() method
access_gender = person.get("gender")
print(access_gender)
print(access_name)

# Accessing all keys using keys()
student = {
    "name":"Ram Magar",
    "age":21,
    "faculty":"AI",
    "semester":"1st"
}
all_keys = student.keys()
print(all_keys)

# Accessing all values using values()
all_values = student.values()
print(all_values)

# Acessing all items() i.e key:value
all_items = student.items()
print(all_items)


# Adding items to the dictionary 
# using simple square bracket which means key: value assignmet
student["year"] = "1st"
print(student)
# Using update method
student.update({"section":"A","rollno":12})
print(student)


# Changing Dictionary Items
staff = {'name': 'Anup',
         'age': 12,
         'city': 'Kathmandu'
         }
# Modifying the value associated with the key 'age'
staff['age'] = 18
print(staff)
# Modifying/updating using update method
staff.update({"name": "Ram","age":45})
print(staff)

# Removing Items form the dictionary using pop(),popitem(), clear() and del
stu = {"name":"kiran", "age":22,"regno": 123 , "branch":"AI"}
# using pop method
stu.pop("age")
print(stu)
# using popitem method
stu.popitem()
print(stu)

# using del keyword
del stu["regno"]
print(stu)
# using clear
stu.clear()
print(stu)

