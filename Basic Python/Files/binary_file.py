# Writing to binary file
file = open('data.bin','wb')
data = b"Hello Pyhton" # b prefix converts string to binary
file.write(data)
file.close()
print("Binary data written successfully!") 