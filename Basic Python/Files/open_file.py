# Opening file using relative path in python
file = open('student.txt','w')
file.write('Here is student Message!')
print('Sucessfully written into file.')
file.close()

# Open file in read mode from relative path
file = open('student.txt','r')
data = file.read()
print(data)
file.close()

# Opening file in read mode form absolute path
file = open('C:\python\student.txt','r')
data = file.read()
print(data)
file.close()