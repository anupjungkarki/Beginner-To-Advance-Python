# Recursive addition 
def recursive_addition(num):
    if num == 1: # Base case
        return num
    else:
        return num + recursive_addition(num - 1)  # Recursive case
sum = recursive_addition(3)
print(sum)

