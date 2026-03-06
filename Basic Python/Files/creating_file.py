#Creating a empty text file in current directory
fp = open('student.txt', 'x')
fp.close()

# Creating file in specific directory
with open("C:\python\student.txt",'w') as fp:
    fp.write('Creating File In Specific Path.')
print('File Sucessfully Created!')

# Another way of creating File in specific path
file = open("C:\python\student.txt",'w')
file.write("File Creating Using Simple Method")
print('File Sucessfully Created!')
file.close()