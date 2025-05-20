#  Write a program that demonstrate the usage of various String functions.

# Defining a sample string
text = "  Hello, Python Programming!  "

# 1. String length
print("Length of string:", len(text))

# 2. Converting to uppercase and lowercase
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# 3. Removing whitespace
print("Stripped String:", text.strip())

# 4. Checking if string starts or ends with a specific word
print("Starts with 'Hello':", text.strip().startswith("Hello"))
print("Ends with 'Programming!':", text.strip().endswith("Programming!"))

# 5. Finding a substring
print("Index of 'Python':", text.find("Python"))

# 6. Replacing a word
print("Replacing 'Python' with 'Java':", text.replace("Python", "Java"))

# 7. Splitting a string
words = text.split()
print("Splitting string into words:", words)

# 8. Joining a list of words
joined_text = "-".join(words)
print("Joining words with '-':", joined_text)

# 9. Checking if string is alphanumeric
print("Is Alphanumeric?", text.isalnum())  # False due to spaces and punctuation

# 10. Counting occurrences of a character
print("Count of 'o':", text.count("o"))

