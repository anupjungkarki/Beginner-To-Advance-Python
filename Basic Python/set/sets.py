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
