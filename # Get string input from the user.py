# Get string input from the user
text = input("Enter a string: ")

# Display first and last characters with safety checks for empty strings
print("First character :", text[0] if text else "Empty string")
print("Last character :", text[-1] if text else "Empty string")

# Slicing and reversing
print("First five characters:", text[:5])
print("Reversed string :", text[::-1])

# Case conversions
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# Count occurrences of a substring
sub = input("Enter a character/substring to count: ")
print("Occurrence count:", text.count(sub))

# Replace a substring or word
old = input("Enter word to replace: ")
new = input("Enter new word: ")
print("After replacement:", text.replace(old, new))

# Split and join operations
words = text.split()
print("Split words:", words)
print("Joined with '-':", "-".join(words))

# Check start and end substrings
start_sub = input("Enter starting substring to check: ")
end_sub = input("Enter ending substring to check: ")
print("Starts with given substring:", text.startswith(start_sub))
print("Ends with given substring :", text.endswith(end_sub))
