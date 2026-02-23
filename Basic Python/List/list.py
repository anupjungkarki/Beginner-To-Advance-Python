# creating a list
list = [1, 2, 3, 4, 4, 5, 5, 6, 7, 8, 8, 9, 10, 11, 12]

# Iterating through the list
for i in list:
    print(i)

 
# Accessing the first element
# print(list[0]) 
# print(list[1])  
print(list)

list.append(13)  # Adding an element to the end of the list
print(list)

# using loop to remove duplicate elements from list
unique_list = []
for item in list:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)

# Adding multiple elements to the end of the list'
new_list = [15, 16, 17, 4 ]
list.extend(new_list) 
print(list)

# Removing an element from the list
list.remove(4)  # Removes the first occurrence of 4
print(list)

# Removing an element by index
list.pop(2) # Removes the element at index 2
print(list)

# Sorting the list
list.sort()  # Sorts the list in ascending order
print(list)

# Reversing the list
list.reverse()  # Reverses the order of the list
print(list)

# Slicing the list
sliced_list = list[2:5]  # Gets elements from index 2 to 4
print(sliced_list)

# Finding the length of the list
print(len(list))  # Prints the number of elements in the list