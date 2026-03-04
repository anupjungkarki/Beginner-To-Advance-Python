# Example of nested dictionaries 
# Creating nested dictionaries

# students = {
#     'student1':{
#         'name':'Anup',
#         'age': 20,
#         'course': ['Python','Artificial Intelligence','Calculas','Digital Logic'],
#         'semester':'1st',
#         'year':'1st'
#         },

#     }

# Creating Nested dictionaries using Curly braces {}
students = {
    'student1':{
        'name':'Anup',
        'age': 20,
        'program': 'BTech AI',
        'faculty':'Science and Technology',
        'semester':'1st',
        'year':'1st'
        },
        'student2':{
        'name':'Anup',
        'age': 20,
        'program': 'BTech AI',
        'faculty':'Science and Technology',
        'semester':'1st',
        'year':'1st'
        }
    }
print(students)


# Using dict() Constructor
students = dict(
    student1 = dict(
            name = "Anup",
            age = 20,
            program = "BTech AI",
            faculty = "Science and Technology",
            semester = "1st",
            year = "1st"
        ),

    student2 = dict(
            name = "Anup",
            age = 20,
            program = "BTech AI",
            faculty = "Science and Technology",
            semester = "1st",
            year = "1st"
            )
        )
print(students)


# Accessing Nested Dictionaries
students = {
    "student1": {
        "name": "Anup",
        "age": 20,
        "program": "BTech AI"
    },
    "student2": {
        "name": "Hari",
        "age": 22,
        "program": "BCA"
    }
}

# Accessing Using Simple Method
print(students["student1"]["name"])
print(students["student2"]["name"])

# Acessing get() Method
print(students.get("student1").get("age"))
print(students.get("student2").get("age"))


# Adding Elements to a Nested Dictionary
students = {
    "student1": {
        "name": "Anup",
        "age": 20
    }
}

# Adding new element inside inner dictionary
students["student1"]["program"] = "BETech AI"
print(students)


# Adding New Outer Dictionary Element
students['student2'] = {  "name": "Hari",
                          "age": 22,
                          "program": "BCA"
                        }
print(students)


# Adding New Elements using update() Method
students['student1'].update({
                             "faculty": "Science and Technology",
                             "semester": "1st"
                        })
print(students)


# Deleting the elements form nested dictionary
students = {
    "student1": {
        "name": "Anup",
        "age": 20,
        "program": "BTech AI"
    }
}

# Delete inner element
del students["student1"]["age"]
print(students)

# Delete element using pop() Method
students['student1'].pop('name')
print(students)

# Deleting Outer dictionary element
del students["student1"]
print(students)
