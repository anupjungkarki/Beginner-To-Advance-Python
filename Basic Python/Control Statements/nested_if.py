# Checking Prime or not using nested if- else

num = int(input("Enter the value to check Even Number:"))
if num > 1:
    if num % 2 == 0:
        print(f'{num} is Prime!')
    else:
        print(f'{num} is not Prime!')
else:
    print("You Enter value less than 1 cannot be allowed")