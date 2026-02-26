'''
# Tuple in Python
Tuple is a collection which is ordered and unchangeable.
In Python tuples are written with round brackets.
'''
# Create a Tuple using parentheses
# my_tuple = ("apple", "banana", "cherry")
# print(my_tuple)

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


a = (1, 2, 3, 4, 5)
b = (6, 7, 8, 9, 10)

# Concatenating two tuples
c = a + b
print(c)
 