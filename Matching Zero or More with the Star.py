import re
"""
The (*) asterik or star, means match zero or more

The group that precedes the star can occur any number of times 
in the text

It can be completely absent or repeated over and over again.

"""
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())

"""
For 'Batman', the (wo)* part of the regex matches zero instances of wo
in the string; for 'Batwoman', the (wo)* matches one instance of wo; and for
'Batwowowowoman', (wo)* matches four instances of wo.
If you need to match an actual star character, prefix the star in the
regular expression with a backslash, \*.
"""

