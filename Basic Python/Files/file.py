# File Opening 
file = open("test.txt","w")
if file:
    print("file open sucessfully!")
else:
    print("File not found!")


# # Opening File using exception handling
try:
   file = open("test.txt", "r") 
   print("File opened sucessfully!")
except FileNotFoundError:
   print("Opps! File doesn’t exist")
finally:
    file.close()

# Opening File and writing on it
file = open("data.txt", "w")
file.write("This file is created using Python.")
file.close()

# Reading data using try and cache
try:
    file = open('data.txt', 'r')
    res = file.read()
    print(res)
    file.close()

except FileNotFoundError:
    print('Opps! File doesn’t exist')
  