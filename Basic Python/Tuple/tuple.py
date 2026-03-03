'''
# Tuple in Python
Tuple is a collection which is ordered and unchangeable.
In Python tuples are written with round brackets.
'''
# Create a Tuple using parentheses
# my_tuple = ("apple", "banana", "cherry")
# print(my_tuple)


# Creating tuple using tuple() function
new_tuple = tuple(("anup", "Kathmandu", "AI" , 23))
print(new_tuple)
# Output : (“anup”, “ Kathmandu”, “AI” , 23)

# when an iterable(e.g., string) is passed
s = "anupkarki"
d = tuple(s)
print(d)

# # unpacking a tuple
# t3 = 1, 2, 4, 5
# print(t3)

# for i in t3:
#     print(i)


# t4 = list(t3)
# print(t4)

# Nested Tuple
# t5 = ((1, 2, 3) ,(4, 5))
# for i in t5:
#     for j in i:
#         print(j)

# Accessing Tuples using for loop and range() function
tuples = (1, 2, 3, 4, 5)
for i in range(len(tuples)):
    print(tuples[i])

# Accessing Tuples uing index
print(tuples[2])

# Concatenating two tuples
a = (1, 2, 3, 4, 5)
b = (6, 7, 8, 9, 10)
c = a + b
print(c)

# Tupe Negative Indexing
tuple1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# slice a tuple using negative indexing
print(tuple1[-5:-1])

# Sort Tuple in ascending and decending order
num=(1,3,2,4,6,5)
ascending = (sorted(num))
decending = (sorted(num,reverse=True))
print(ascending)
print(decending)
# As we can see that tuple return list of sorted data by using sorted function do we need to bring back to the original tuple form in following way.
print(tuple(ascending))
print(tuple(decending))
# output : 
