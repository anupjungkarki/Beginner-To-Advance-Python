# Write a program to merge two lists and remove duplicates.
list1 = [4, 6, 3, 4, 3, 6, 6, 9, 1]
lsit2 = [1, 3, 5, 7, 9, 11, 13, 15]

merged_list = list1 + lsit2
print(merged_list)

unique_list = list(set(merged_list))
print(unique_list)


print(max(list1))

list1.append(12)
print(list1)
