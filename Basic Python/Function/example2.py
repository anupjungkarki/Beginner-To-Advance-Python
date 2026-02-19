
# Acheiving modularity by using python functions
def get_number():
    a=int(input("Enter the number first:"))
    b= int(input("Enter ther number second:"))
    return a , b

def sum(x ,y):
    return x + y
x , y = get_number()
result = sum(x ,y)
print(f'The sum of {x} and {y} is:', result)


# Reusing The input by calling function
# p , q = get_number()
# result = p + q
# print(result)