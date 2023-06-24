'''
String in python are surrounded either by single quotation 'String' or  Double quotation "String" 

'''
# Example 1
String1 = "Hello, This Double Quotation String."
String2 = 'Hello, This Single Quotation String.'
print(String1)
print(String2)


# Multiline String basic Example,
MultiLineString = """
 Hello, Here we are learning about,
 How Multiline String Work In Python,
 Here The Text Pargraph is Split Into Many Different Individual Line,
 So, If You Print This Paragraph Without Three Double Quotation Mark,
 Then It Will Through Error You can try this with ThreeSingle Quotation Too."""
# If you use One Double Quotation and Single Quotation in This Type of Paragraph Text It Will Give Error.
print(MultiLineString)


# String are Array of bytes representating unicode character so each Single character have their length of 1.
MyString = "Hello, We are Learning Python Programming Language"
# Let's Find the Index Position Of Each Character by Traversing Through The String.
print(MyString[20])


# As we Know that string are Array So, Let's Loop Through The String by using For Loop.
for s in MyString:
    print(s)
    

# Let's Find the Length of String
length = len(MyString)
print("The Length Of String is:", length)


# We can also check the presence of string or not in Paragraph using 'if' Statement Like This,
is_available = "Programming" in MyString
is_notAvailable = "World" in MyString
print(is_available)
print(is_notAvailable)