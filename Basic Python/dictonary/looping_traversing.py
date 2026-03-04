# Sample dictionary
student = {
    "name": "Anup",
    "age": 21,
    "major": "Computer Science",
    "gpa": 3.7,
    "year": "3rd",
    "Semester":"7th"
}

# Using a simple for loop
for data in student:
    print(data, ":" ,student[data])

# Using dict_name.keys() method
for key in student.keys():
    print(f'{key},', end=' ')

# Using dict.name.values() method
for value in student.values():
    print(f'{value},',end=' ')

# Using dict_nam.items() method
for key , value in student.items():
    print(f'{key} : {value}')