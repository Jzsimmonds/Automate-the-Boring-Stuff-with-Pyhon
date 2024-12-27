# import re module
import re

# Precompile the regex for email validation
email_pattern = re.compile(r"\w+@\w+\.\w+")

# Sample text
text = "Emails: alice@example.com, bob@gmail.com"

# Use the precompiled regex to find matches
matches = email_pattern.findall(text)
print(matches)  # Output: ['alice@example.com', 'bob@gmail.com']

