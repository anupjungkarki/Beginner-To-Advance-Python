# Different ways to create dictonary in Python
# Python dictonary
data = {}
data["name"] = "Anup"
data["age"] = 25
print(data)

# Another way to create dictonary
data2 = {"name" :"Ram", "age":30}
print(data2)

# Creating dictonary using dict() function
data3 = dict(name="Shyam", age=35)
print(data3)

# length of dictonary
print(len(data3))

# Types checking of dictonary
print(type(data3))

# Accessing dictonary values using keys
name = data3["name"]
print(name)

age = data.get("age")
print(age)

k = data3.keys()
print(k)

v = data3.values()
print(v)    

i = data3.items()
print(i)

# Change the items in dictonary
data3["age"] = 40
print(data3)    

# Update the dictonary using update() method
data3.update({"name": "Hari", "age": 45})
print(data3)

# deleting an item from dictonary
# del data3["age"]
# print(data3)

# data3.pop("name")
# print(data3)

# data2.clear()
# print(data2)


