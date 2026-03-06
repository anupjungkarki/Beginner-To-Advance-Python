# File Handling With with statement to write a File
message = "Hello we are learning to write in python file using with statement."
with open("with.txt",'w') as fp:
    fp.write(message)
print("Writing is Complete!")

# Appending data to an existing file
new_message = "\nThis is and append message."
file = open('with.txt','a')
file.write(new_message)
file.close()
print("Data Appended Successfully!")

# Appending using with statement
with open('with.txt','a') as fp:
    fp.write(new_message)
print("Data Appended Successfully!")

# # Reading the append file
with open('with.txt','r') as fp:
    read_data = fp.read()
    print(read_data)

# What if we try to append and read without open the file in same file
with open('with.txt','a') as fp:
    fp.write('Hello Append')
    print(fp.read())

# Correct way of append and read on same file using a+ mode
text = "\nWe are using a+ mode here."
with open('with.txt', 'a+') as fp:
    fp.write(text)
    print("Append Sucessfully!")
    fp.seek(0)
    print(fp.read())


# For reading and writing in same file
w_message = "Writing and Reading on same file."
with open('with.txt','w+') as fp:
    fp.write(w_message)
    # move file handle to the start
    fp.seek(0)
    print(fp.read())