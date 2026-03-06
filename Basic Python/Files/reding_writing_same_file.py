# Creating File Using Relative Path
file = open('demo.txt', 'w')
print("File Created Sucessfully!")
file.close()


#Creating File Using with statement in Relative Path
with open('student.txt','w') as fp:
    print('File Created Sucessfully!')

# Writing and reading in same file
text = "\nWe are using a+ mode here."
file = open('data.txt','a+')
file.write(text)
print("Sucessfully Written into file!")
file.seek(0)
data_read = file.read()
print(data_read)
file.close()


