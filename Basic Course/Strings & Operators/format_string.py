'''
As we know that string and number can't be combine by simply doing concatenation so here,
we have special method called format() to do this things in  easier way.Where format() take the 
pass argument and formats them as per the index value and place them accordingly in the string
where the placeholder is define {}.

'''

# Example of format String
months = 6
String = "Hello We Are Learning Python Programming For {} Months"
f = String.format(months)
print(f)


#Format Take Unlimited Number of argument and we can give index value to assign the respective placeholder.
age = 23
day = 4
week = 6
txt = "Hello ,I am {0} years old and I am Learning Python From {1} Day's ago till to next {2} Weeks."
result = txt.format(age,day,week)
print(result)
