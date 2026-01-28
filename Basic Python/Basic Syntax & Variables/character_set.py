'''
The character set in Python refers to the collection of characters that are used to represent text in the Python programming Language.
Python uses the Unicode character set, which includes a wide range of characters from various languages and scripts, as well as special symbols and emojis.
Character likes a-z, A-Z, 0-9, and special characters like !, @, #, $, %, etc. are all part of the character set in Python.

Unicode Support:
Python's support for Unicode allows developers to work with text in multiple Languages seamlessly.
This means that you can use characaters from different Languages in your Python programs without any issues.
# Example of Unicode Characters in Python
print("Hello, World!")  # English
print("こんにちは世界")  # Japanese
print("Привет, мир!")  # Russian
print("😊🌍🚀")  # Emojis
print("नमस्ते !")  # Nepali

# Character Encoding in Python
Character encoding is the process of converting characters into a specific format for storage or transmission.
Python uses UTF-8 encoding by default, which is a widely used encoding that can represent all Unicode characters.
This ensures that text data is stored and transmitted correctly across different systems and platforms.
# Example of Encoding and Decoding
text = "Hello, World!"
encoded_text = text.encode('utf-8')  # Encoding to UTF-8
print(encoded_text)  # Output: b'Hello, World!'
decoded_text = encoded_text.decode('utf-8')  # Decoding back to string
print(decoded_text)  # Output: Hello, World!

# Conclusion
Python's character set and Unicode support make it a powerful language for handling text data from various Languages and scripts.

'''
# Example of Encoding and Decoding
text = "Hello, World!"
encoded_text = text.encode('utf-8')  # Encoding to UTF-8
print(encoded_text)  # Output: b'Hello, World!'
decoded_text = encoded_text.decode('utf-8')  # Decoding back to string      
print(decoded_text)  # Output: Hello, World!

# Example of Unicode Characters in Python
print("Hello, World!")  # English
print("こんにちは世界")  # Japanese
print("Привет, мир!")  # Russian
print("😊🌍🚀")  # Emojis]
print("नमस्ते !")  # Nepali

