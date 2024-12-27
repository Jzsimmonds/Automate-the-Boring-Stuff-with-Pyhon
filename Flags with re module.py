# Flags with re.compile()

# We can uses regex for pass regex flags
# directly to re.compile() to modify its behavior 

# Example with Flags 

# Importing the re module
import re

# Compile a case-insensitive regex
pattern = re.compile(r"hello", re.IGNORECASE)

# Sample text
text = "Hello, HELLO, hello"

# Find all matches
matches = pattern.findall(text)
print(matches)  # Output: ['Hello', 'HELLO', 'hello']


# Advanced example



# Compile a verbose regex for phone numbers
phone_pattern = re.compile(r"""
    \(?\d{3}\)?     # Area code (optional parentheses)
    [-.\s]?         # Separator (dash, dot, or space)
    \d{3}           # First 3 digits
    [-.\s]?         # Separator
    \d{4}           # Last 4 digits
""", re.VERBOSE)

text = "Call: 123-456-7890, (555) 555-5555, 9876543210"

# Find all phone numbers
matches = phone_pattern.findall(text)
print(matches)  # Output: ['123-456-7890', '(555) 555-5555', '9876543210']
