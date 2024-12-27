# Mathching Specific Repetitions with Curly Brackets 
# import r module 
import re
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo1.group()
print(mo1)

mo2 = haRegex.search('Ha')
mo2 == None
print(mo2)

# Example
# Exact Number of Repetitions {n}
# mathching the patterns that repeat a specific number of times

import re

# Match exactly 3 digits
pattern = re.compile(r"\d{3}")

# where
# \d{3} matches any sequence of exactly 3 digits.

text = "123 4567 89"
matches = pattern.findall(text)
print(matches)  # Output: ['123', '456']

# where 
# 4567 is not included because it has more than 3 digits.