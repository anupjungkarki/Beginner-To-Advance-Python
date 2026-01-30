'''
Operator Precedence and Associativity in Python
Operator precedence determines the order in which operators are evaluated in an expression.
Operators with higher precedence are evaluated before operators with lower precedence.
When operators have the same precedence, their associativity determines the order of evaluation (left-to-right or right-to-left).
Here is a summary of operator precedence and associativity in Python (from highest to lowest precedence):
1. Parentheses: ( ) - Highest precedence
2. Exponentiation: ** - Right-to-left associativity
3. Unary plus and minus: +x, -x, ~x - Right-to-left associativity
4. Multiplication, Division, Floor Division, Modulus: *, /, //, % - Left-to-right associativity
5. Addition and Subtraction: +, - - Left-to-right associativity
6. Bitwise Shift Operators: <<, >> - Left-to-right associativity
7. Bitwise AND: & - Left-to-right associativity
8. Bitwise XOR: ^ - Left-to-right associativity
9. Bitwise OR: | - Left-to-right associativity
10. Comparison Operators: ==, !=, >, <, >=, <= - Left-to-right associativity
11. Identity Operators: is, is not - Left-to-right associativity
12. Membership Operators: in, not in - Left-to-right associativity

'''
# Example to demonstrate operator precedence and associativity
a = 10
b = 5
c = 2
result = a + b * c ** 2 - (a / b)
print("Result:", result)  # Output: Result: 17.0

# Explanation of the example:
# 1. Exponentiation: c ** 2 = 2 ** 2 = 4 
# 2. Multiplication: b * 4 = 5 * 4 = 20
# 3. Division: a / b = 10 / 5 = 2.0
# 4. Addition: a + 20 = 10 + 20 = 30
# 5. Subtraction: 30 - 2.0 = 28.0
# Final result is 28.0
# Note: Parentheses have the highest precedence, so expressions within parentheses are evaluated first.

e =  a ** b * c
print(e)