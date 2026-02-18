# if condition1:
#     statement
# elif conditon2:
#     statement
# else:
#     statement

'''
Docstring for Basic Python.ifelse
Take a input from user 
Enter name of students
enter marks of five subjects 
pass marks: 32
total marks per subject = 100
total marks in all subjcts  = 500
calculate total obtained marks of studnts in all subjects
display result pass and failed
find percentage and display the grade
'''
total_marks = 500
name = input("Enter the name of student:")
ai = int(input("Enter the marks of ai:"))
python = int(input("Enter the marks of python:"))
java = int(input("Enter the marks of java:"))
c = int(input("Enter the marks of c:"))
sql = int(input("Enter the marks of sql:"))

total_obtained = ai + python + java + c + sql
percentage  = float(total_obtained) / float(total_marks) * 100
print("The percentage by student is :", percentage , "%")

print("The total marks of " + name + "is:", total_obtained)


if(ai >= 32 and python >= 32 and java >= 32 and c >= 32 and sql >= 32):
    print("Pass")
else:
    print("Fail")

if percentage >= 85:
    print("A+")
elif percentage >= 70:
    print("A")
elif percentage >= 60:
    print("B+")
elif percentage > 45:
    print("B")
else:
    print("C")
