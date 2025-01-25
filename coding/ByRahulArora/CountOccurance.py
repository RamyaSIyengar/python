s1 = "aaabbbbbbbbcdd"

char = 'b'

count = 0

for i in s1:
    if i == char:
        count = count + 1
print(count)

str1 = 'India'
print(str1[-1])
print(str1[:-1])  # split
print(str1[::-1])  # reverse the string

str2 = 'Hello World'
print(str2[::5])
print(str2[1:10:2])

# Q -  take 2 inputs and print as expected output

list1 = ['my', 'name']
list2 = ['is', 'Ramya']
expected_output = 'my name is Ramya'

list3 = list1+list2
list1.extend(list2)
print(list1)

# join
print(' '.join(list1))
print(list3)


myDict = {
    'name': 'Ramya',
    'job': 'tester',
    'status': 'building'
}

sep = '-'

x = sep.join(myDict.values())
print(x)


# Covert list to dict
l1 = ['a', 'b', 'c']
l2 = [1, 2, 3]

exp_output = {'a': 1, 'b': 2, 'c': 3}
result = {}
for i, j in zip(l1, l2):
    result[i] = j

# print(result)
dict1 = {}
for i in range(len(l1)):
    dict1[l1[i]] = l2[i]
print(dict1)

# print duplicate char in list
a = ['India', 'is', 'my', 'country']
output = ['i', 'n', 'y']

strA = ''.join(a)
duplicate = []
for i in strA:
    if strA.count(i) > 1 and i not in duplicate:
        duplicate.append(i)
print(duplicate)
print(*duplicate)

# print unique characters

t = 'testMatches'
# e_o = e, s

unique = ''
for char in t:
    if t.count(char) == 1:
        unique += char

print(', '.join(unique))


# one line for loop to print words start with i

a = ['india', 'is', 'my', 'country']

op = [i for i in a if i.startswith('i')]
print(op)
