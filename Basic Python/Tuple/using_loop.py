# Travesing in tuple
list_tuple = [(1, 2), (3, 4), (5, 6)]
for item in list_tuple:
      for data in item:
             print(data, end =' ')

# Unpacking tuple using loop 
list_tuple = [(1, 2), (3, 4), (5, 6)]
for a, b in list_tuple:
    print("First:", a, "Second:", b)
    nested_tuple = ((20, 40, 60), (10, 30, 50), "Python")

# Nested tuple
nested_tuple = ((20, 40, 60), (10, 30, 50), "Python")

# access the first item of the third tuple
print(nested_tuple[2][0])  # P

# iterate a nested tuple
for i in nested_tuple:
    for j in i:
        print(j, end=" ")
    print("\n")
