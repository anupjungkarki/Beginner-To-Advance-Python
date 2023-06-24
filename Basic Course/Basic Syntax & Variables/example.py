# Here we will do basic example from day 1 topics.

# Example using int,float and string
total_marks = 600
gain_marks = 450.50
msg1 = "Congratulation! Pass"
msg2 = "Sorry! Fail"

avg = gain_marks/total_marks * 100

if (avg > 40):
    print(msg1)
else:
    print(msg2)
    

# Example of boolean
x= 20
y = 40       
print(bool(x>y))
print(bool(x<y))