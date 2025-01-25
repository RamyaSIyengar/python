# A higher order function is a function that can take another function as a parameter,
# or it's also a function that can return a function.

# modern alternatives to map and filter is =? list comprehension and generator expresions


l =[2,3,4]

def sq(x):
    return x**2

print(map(sq, l))
print(list(map(sq, l)))
# [4, 9, 16]

l1 = [1,2,3]
l2 = [4,5,6,2]
def add(x,y):
    return x+y
print(list(map(add, l1,l2)))
# [5, 7, 9]

print(list(map(lambda x,y:x+y,l1,l2)))
# [5, 7, 9]


# filter

li = [0,1,2,3,4]

print(list(filter(None, li)))
# [1, 2, 3, 4]
# as 0 is Falsy its not returned

def is_even(x):
    return x%2==0
print(list(filter(is_even, li)))
# [0, 2, 4]


# zip - not a higher order func

l1 = [1,2,3]
l2 = [4,5,6]
l3 = ['a', 'b', 'c']
print(list(zip(l1, l2)))  # [(1, 4), (2, 5), (3, 6)]
print(list(zip(l1,l2,l3)))  # [(1, 4, 'a'), (2, 5, 'b'), (3, 6, 'c')]

a =range(100)
b = 'wxyz'
print(list(zip(a,b)))
# [(0, 'w'), (1, 'x'), (2, 'y'), (3, 'z')]  => it will not print after one iterable is exhausted


#  list comprehension alternative to map
print([x**2 for x in [2,3,4]])  # [4, 9, 16]
print([x+y for x, y in zip(l1, l2)])  # [5, 7, 9]

# list comprehension alternative to filter => use if
print([x**2 for x in [2,3,4] if x % 2 == 0])  # [4, 16]

print([x**2 for x in range(10) if x**2 < 25])

