# Creating Nested Dictionary
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
        'name':'Hari',
        'age': 21,
        'program': 'BTech AI',
        'faculty':'Science and Technology',
        'semester':'1st',
        'year':'1st'
    },
    'student3':{
        'name':'Sita',
        'age': 22,
        'program': 'BCA',
        'faculty':'Management',
        'semester':'2nd',
        'year':'1st'
    },
    'student4':{
        'name':'Ramesh',
        'age': 23,
        'program': 'BIT',
        'faculty':'Science and Technology',
        'semester':'2nd',
        'year':'2nd'
    }
}
print(students)
# Traversing Nested Dictionary
for student_id , info in students.items():
    print("\nID:", student_id)
    for key , value in info.items():
        print(f'{key} : {value}')