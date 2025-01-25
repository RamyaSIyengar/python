my_set = {1,2,3}
this_Set = {0,9,8,2}
empty_set = {}
empty_set1 = set(())
print(my_set, empty_set, type(empty_set1))

# add
my_set.add(10)
# my_set.add([23, 11])  # TypeError: unhashable type: 'list' => cant add 2 or more items so use update()
print(my_set)

# update
# Adds multiple elements (from an iterable like list, tuple, or set) to the set.
my_set.update([23,45,67])
print(my_set)

# remove -
# Removes a specific element from the set.
# Raises a KeyError if the element is not found.
my_set.remove(23)
print(my_set)

# discard
# Removes a specific element from the set, but does not raise an error if the element is not found.
my_set.discard(100)
print(my_set)

e = my_set.pop()
print(e, my_set)

# union()
# Returns a new set containing all elements from both sets (without duplicates).

res = my_set.union(this_Set)
print(res)

# intersection()
# Returns a new set containing only the elements common to both sets.

res1 = my_set.intersection(this_Set)
print(res1)

# difference
# Returns a new set containing elements in the first set but not in the second.
res2 = my_set.difference(this_Set)
print(res2)

#  symmetric_difference()
# Returns a new set containing elements that are in either of the sets, but not in both.

res3 = my_set.symmetric_difference((this_Set))
print(res3)

# issubset()
# Checks if the first set is a subset of the second set.

set1 = {1, 2}
set2 = {1, 2, 3}
result = set1.issubset(set2)
print(result)  # Output: True

# issuperset()
# Checks if the first set is a superset of the second set.

set1 = {1, 2, 3}
set2 = {1, 2}
result = set1.issuperset(set2)
print(result)  # Output: True

#  isdisjoint()
# Checks if two sets have no elements in common.

set1 = {1, 2, 3}
set2 = {4, 5}
result = set1.isdisjoint(set2)
print(result)  # Output: True
