
# The enumerate () function adds a counter to an iterable and
# returns it in the form of an enumerating object.
# This enumerated object can then be used directly for loops or converted
# into a list of tuples using the list() function.

# Syntax: enumerate(iterable, start=0)

l1 = ["eat", "sleep", "repeat"]

print(list(enumerate(l1)))   # [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
print(type(enumerate(l1)))   # <class 'enumerate'>

s1 = "geek"
print(list(enumerate(s1, start=3)))   # [(3, 'g'), (4, 'e'), (5, 'e'), (6, 'k')]


# Using Enumerate Object in Loops

# Enumerate() is used with a list called l1. It first prints tuples of index and element pairs.
# Then it changes the starting index while printing them together.
# Finally, it prints the index and element separately, each on its own line.

l1 = ["eat", "sleep", "repeat"]

for i in enumerate(l1):
    print(i)
# (0, 'eat')
# (1, 'sleep')
# (2, 'repeat')

for count, ele in enumerate(l1, 100):
    print(count, ele)

# Accessing the Next Element

# In Python, the enumerate() function serves as an iterator,
# inheriting all associated iterator functions and methods.
# Therefore, we can use the next() function and __next__() method with an enumerate object.

fruits = ['apple', 'banana', 'cherry']
enum_fruits = enumerate(fruits)

# next_element = next(enum_fruits)
# print(next_element)

for index,value in enum_fruits:
    print(index, value)



