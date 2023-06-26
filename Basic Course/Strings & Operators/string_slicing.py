'''
By using slice syntax string can be slice.Specify the start index and the end index,
separated by a colon (:), to return a part of the string.As we know that string itself is
just behave like array and we can traverse through the entire string character.

'''

# Simple slice Example
x = "Hello, Programmer!"
result  = x[7:14]
print(result)


# Slice from the start
p = "Programmer are very Passionated"
res = p[:10]
print(res)


# Slice to the end
w = "Slicing to the end example"
r = w[8:]
print(r)

# Negative Indexing In 
n = "Negative Indexing In Slice"
m = n[-25:-3]
print(m)

