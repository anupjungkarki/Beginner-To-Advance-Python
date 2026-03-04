# Creating Sets usin set() constructor
set1 = set((4,5, 6,5,3,5,7,8))
print(set1)

# creating set using curly braces { }
set2 = {1, 2, 3, 4, 5}
set2.add(6)
print(set2)

# Accessing items of a set
items = {"laptop" , "book", "pc", 1 , 4}
for data in items:
    print(data , end=' ')

# Checking the item exist in the set
items = {"laptop" , "book", "pc", 1 , 4}
if "laptop" in items:
    print("Items is found!")
else:
    print("Items is not found!")

# Adding Items to the set using add() method
days = {"Sunday", "Monday", "Tuesday", "Wednesday"}
print(days)
days.add("Thurdsay")
print(days)

# Update the multiple items in the sets
months = {"Jan", "Feb", "Mar", "Apr", "May"}
print(months)
months.update(["Jun","July","Aug"])
print(months)

# Sets Methods for removing sets data
# Removing Single Items from sets
new_set = months = {"Jan", "Feb", "Mar", "Apr", "May"}
print(new_set)
new_set.remove("Jan")
print(new_set)

# Pop the items form the sets
new_set.pop()
print(new_set)

# discard items form the sets
new_set.discard("Apr")
print(new_set)

# clear all sets items
new_set.clear()
print(new_set)

# Set Operations
# Union operation
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union_result = set1 | set2
print(union_result)


# using Set Operator (&) to intersection
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection_result = set1 & set2
print(intersection_result)

# Symmetric difference
Days1={"Mon","Tue","Wed","Sat"}
Days2={"Thr","Fri","Sat","Sun","Mon"}
print(Days1. symmetric_difference(Days2))

# using Set Operator (^)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
sym_diff_result = set1 ^ set2
print(sym_diff_result)

# Looping through the sets data
set_data = {"anup", 1, 3,"sunday", "jan"}
for items in set_data:
    print(items, end=' ')