import re
"""
The (+) means "Match one or more"
The group preceding a plus must appear at least once, it is not optional
"""

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batman')
print(mo3== None)

"""
The regex Bat(wo)+man will not match the string 'The Adventures of
Batman' because at least one wo is required by the plus sign.
If you need to match an actual plus sign character, prefix the plus sign
with a backslash to escape it: \+.
"""