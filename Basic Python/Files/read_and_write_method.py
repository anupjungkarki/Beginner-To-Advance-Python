# Here we are learning read and write various method for practices
#Opening and creating the file and writing on it using write() method.
stdentdata = "\n Name: Ram Karki \n Address: Kathmandu"
try:
    with open('C:\PROGRAMMING ZONE\PYTHON\Beginner-To-Advance-Python\Basic Python\Files\student.txt','w') as fp:
        fp.write("Here is the details of students.")
        print('File created sucessfully and Written into the file.')
except FileNotFoundError:
    print("OOps! File Not Found!")



# Open the file in read-write mode
with open("C:\PROGRAMMING ZONE\PYTHON\Beginner-To-Advance-Python\Basic Python\Files\student.txt", "r+") as fp:
   # Move the read/write pointer to the 5th byte position
   fp.seek(5, 0)
   # Read 3 bytes from the current position
   data = fp.read(3)
   # Print the read data
   print(data)
   fp.seek(0)
   fp.write('This is the first Line in File.')
   print("Sucessfully Written into the file!")

# Open the file in Write-Read mode
with open("C:\PROGRAMMING ZONE\PYTHON\Beginner-To-Advance-Python\Basic Python\Files\student.txt", "w+") as fp:
   # Write data to the file
   fp.write("This is a addition data on it.")
   print("Sucessfully Written into the file!")
   # Rewind the pointer to the beginning of the file
   fp.seek(0)
   # Read data from the file
   data = fp.read()
   print(data)

