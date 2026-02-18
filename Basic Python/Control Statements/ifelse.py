'''
If else statements are used to control the flow of the program.
if statement is used to execute a block of code if a condition is true and else statement is used to execute a block of code if the condition is false.
The syntax of if else statement is as follows:
if condition:
    statement
elif condition:
    statement
else:
    statement
In the above syntax, if the condition is true, the block of code under if statement will be executed.
If the condition is false, the block of code under else statement will be executed. If there are multiple conditions, we can use elif statement to check for those conditions.

'''
 # Write a program
user_name = input("Enter your username: ")
password = input("Enter your password:")

if user_name == "admin" and password == "admin123":
    print("Welcome admin!")
elif user_name == "user" and password == "user123":
    print("Welcome user!")
else:
    print("Invalid username or password!")



