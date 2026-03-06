# Simple example to write text into the file
text = "Hello we are learning to Write in Python File!"
# Writing the content into the file
fp = open("message.txt",'w')
fp.write(text)
print("Sucessfully Wire Into the file!")
fp.close()

# Writing in file using absolute path
fp = open("C:\PROGRAMMING ZONE\PYTHON\Beginner-To-Advance-Python\Basic Python\Files\message.txt",'w')
fp.write(text)
print("Sucessfully Wire Into the file!")
fp.close()

# To open the file for reading the content
fp = open("message.txt", 'r')
print(fp.read())
fp.close()


# Writing to a existing file after reading 
fp = open("message.txt", 'r')
print(fp.read())
fp.close()

# Overwriting existing content of a file using write method
fp = open("message.txt",'w')
new_message = "Overwritten Message!"
fp.write(new_message)
print("Writing into existing file is completed!")
fp.close()

#Again read from the file 
fp = open("message.txt", 'r')
print(fp.read())
fp.close()

# Use of writelines() method 
person_data = ['Name: Anup', '\nAddress: Pepsicola', '\nCity: Kathmandu']
# Writing string and list of lines to a file
fp = open("person.txt",'w')
fp.writelines(person_data)
print("Writing is Complete!")
fp.close()

# Use of write() method
fp = open("message.txt", "w")
fp.write("Hello, We are Learning File write() method.")
fp.write("\n Take it easy to learn.")
print("Writing is Complete!")
fp.close()
