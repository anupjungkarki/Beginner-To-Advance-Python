# Example of local variable
def function1():
    x = 5
    print("The vlaue is:", x)


# def function2():
#     print("The value is":, x)

function1()
# function2()


# Example if global variable and its modification using global keyword
# Global variable
x = 5

# defining 1st function
def function1():
    print("Value in 1st function :", x)

# defining 2nd function
def function2():
    # Modify global variable using global keyword
    global x
    x = 555
    print("Value in 2nd function :", x)

# Accessing from outside the function
print("Value of global variable:", x)
function1()
function2()

