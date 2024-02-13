# Creating Regex Objects
# All the regex function in python are in the re module
'''
(Remember that \d means “a digit
character” and \d\d\d-\d\d\d-\d\d\d\d is the regular expression for the correct phone number pattern.)
'''

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
