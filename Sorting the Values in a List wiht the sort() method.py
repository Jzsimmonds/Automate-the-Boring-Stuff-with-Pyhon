# Sorting the Values in a List wiht the sort() method
# Lists of number values or lists of strings can be sorted with the sort()
# method.
spam = [2,3,5,3.14,1,-7]
spam.sort()
print(spam)
spam = ['ants','cats','dogs','pets','badgers','elephants']
spam.sort()
print(spam)
# You can also pass True for the reverse keyword argument to have sort()
# sort the values in reverse order.
spam.sort(reverse=True)
print(spam)
# If you need to sort the values in regular alphabetical order, pass str.
# wer for the key keyword argument in the sort() method call.
spam = ['a','z','A','Z']
spam.sort(key=str.lower)
print(spam)
# This causes the sort() function to treat all the items in the list as if they
# re lowercase without actually changing the values in the list.
