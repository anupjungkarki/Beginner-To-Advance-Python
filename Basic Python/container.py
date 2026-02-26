list1 = [1, 3, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [10, 3, 8, 25, 16, 14, 12, 19, 10]

# Create a List of 5 Numbers Entered by the User
# list3 = []   # Empty list
# for i in range(5):
#     num = int(input("Enter a number: "))
#     list3.append(num)
# print("The list of numbers is:", list3)


# Join two lists using extend() method
# list1.extend(list2)
# print(list1)

# Join two lists using concatenation operator
# new_list = list1 + list2
# print(new_list)

# Join two lists using for loop 
# for new_list in list2:
#     list1.append(new_list)
# print(list1)

# Here we are copying the list using copy() method, which creates a shallow copy of the list.
# copied_list1 = list1.copy()
# print(copied_list1)

# Remove duplicates from using set() method, which creates a set of unique elements from the list.
# unique_list1 = list(set(list1))
# print(unique_list1)

# Remove duplicates using for loop and if statement
# filtered_list=[]
# for i in list1:
#     if i not in filtered_list:
#         filtered_list.append(i)
# print(filtered_list)

# Also we can use remove() method to remove duplicates from the list, but it will only remove the first occurrence of the duplicate element.
# for i in list1:
#     list1.remove(i)
# print(list1)


# Serching specific element in the list using in operator
# search_value = int(input("Enter the search value: "))
# for i in list1:
#     if i == search_value:
#         print(f'The search value is: {i}')
#         break
# else:
#     print("Item not found in list")
    

# We can also use in operator to search for the specific element in the list, which will return True if the element is found and False if it is not found.
# if search_value in list1:
#     print(f'The search value is: {search_value}')
# else:
#     print("Item not found in list")


# finding the largest number in list
# for i in list1:
#     if i == max(list1):
#         print(f'The largest number in the list is: {i}')

# Creating Nested List

# l = []
# l.append(list1)
# l.append(list2)
# print(l)


# nested list
# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # print(nested_list[0][1])

# for data in nested_list:
#     for v in data:
#         print(v)

# Searching for a specific element in the nested list using for loop and if statement
# search = int(input("Enter the search value: "))
# for data in nested_list:
#     if search in data:
#         print(f'{search} is found in the list: {data}')
#         break
# else:
#     print(f'{search} is not found in the list')
