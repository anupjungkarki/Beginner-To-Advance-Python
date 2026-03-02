# user and password validation using nested if else

username = input("Enter Your Username:")
password = input("Enter Your Password:")
is_active = True

if username:
    if password:
        if is_active:
            print("Login Sucessful!")
        else:
            print("Account is not Active!")
    else:
        print("Password is required!")
else:
    print("Username is required!")