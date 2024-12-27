# Using Methods on a Compiled Regex Object 

# The Regex methods are the following 
# search(), match(), findall(), spilt()

# Example 

# import re module
import re

# Precompile the regex
phone_pattern = re.compile(r"\d{3}-\d{3}-\d{4}")

# Sample text
text = "Call me at 123-456-7890 or 987-654-3210"

# Use the compiled object
print(phone_pattern.search(text).group())  # Output: 123-456-7890
print(phone_pattern.findall(text))        # Output: ['123-456-7890', '987-654-3210']
