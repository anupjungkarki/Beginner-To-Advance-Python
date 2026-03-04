# All example of the python dictionary Methods
# Keys() Method in Python Dictionary
student = {
    "name": "Anup",
    "age": 20,
    "course": "Computer Science",
    "grade": "A"
}

# Using keys() method
all_keys = student.keys()
print(all_keys)

# Using loop accsing all keys
for key in student.keys():
      print(key, end= ' ')

# Using values() method
all_values = student.values()
print(all_values)

# Using loop accsing all values
for value in student.values():
      print(value, end= ' ')


# Using items() method
all_items = student.items()
print(all_items)

# Using loop for accessing all items
for key, value in student.items():
      print(key,":", value)

# add_new items using update
student.update({"faculty":"AI","semester":"1st"})
print(student)
# Update the existing value using update
student.update({"age":24,"course":"Science and Technoloy"})
print(student)
