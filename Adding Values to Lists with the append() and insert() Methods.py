# Adding Values to Lists with the append() and insert() Methods
spam = ['cat','dog','bat','fish']
spam.append('elephant')
print(spam)

# The previous append() method call adds the argument to the end of
#the list. The insert() method can insert a value at any index in the list.
#The first argument to insert() is the index for the new value, and the second argument is the new value to be inserted.
spam = ['cat','dog','bat']
spam.insert(1, 'chicken')
print(spam)
