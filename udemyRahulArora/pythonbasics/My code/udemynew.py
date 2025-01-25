import sys

x = 100.1
x = {1, 2, 3, 4, 5,43}
y = x
print(sys.getsizeof(x))
print(sys.getsizeof(y))
print(sys.getrefcount(x))

z = {'fname': 'Ramya', 'lname': 'Iyengar'}
print(z)

print(type(y))
print(isinstance(x, int))


import random

print(random.randrange(10))

print('I will buy a new Ramya\'s house')
na = 'ramya'
print(na[::2])


greeting = 'Hello, world'
g = greeting.split(sep=',')
# using split u can convert string to list and div the strings based on separator

print(type(g))

print('     Ramya    '.strip())

num = 10
print(f'Hello {num}')
print("Hello {}".format(num))
print("Hello %d" % num)

# ternary operator
# var = first value if condition else second value
a = 10
b = 20
c = 30 if a < b else 40
print(c)

# num1 = int(input("Enter a num:"))
# num2 = int(input("Enter a num:"))
# min = num1 if num1<num2 else num2
# print(f'min number among two {num1} and {num2} is {min}')

# identity operator  - is, not is
a = 10
b = 10
c = 20
print(a is b)
print(a is not c)

# membership operator - in, not in


# Multiplication table

# n = int(input("Enter a num to get its multiplication table= "))
# for i in range(1, 11):
#     print("{} * {} = {}".format(n, i, n*i))

# list1 = eval(input("Enter numbers to get a sum of it= "))
# sum=0
# for i in list1:
#     sum = sum + i
#
# print(sum)

p = 'Rahul is my name'
pw = p.split(sep=' ')
for i in pw:
    print(i)

for i in range(10):
    if i == 7:
        print("Breaking loop at {}".format(i))
        break
    print("Value {}".format(i))

for i in range(10):
    if i % 2 == 0:
        print("even no", i)
        continue
    print("odd no", i)


# List

# 1. List is ordered

l1 = ['apple', 'banana', 'cherry']
print(l1[2])

# 2. List allows duplicate values

l1 = ['apple', 'banana', 'cherry', 'apple']
print(l1)

# 3. List is mutable in nature
l1.append('grapes')
print(l1)

# 4. updating list value

l1[1] = 'mango'
print(l1)

l1[2:5] = [1, 'app', 2.5]
print(l1)

# sort list

l2 = ['a', 'e', 'z', 'b']
l2.sort()
print(l2)

# reverse sort
l2.sort(reverse=True)
print(l2)


# Dictionaries

d1 = {'name': 'Ramya',
      "sex": 'Female',
      "hobbies": ['Singing', 'art', 'travelling'],
      "marks": {'sci':98, 'math':87}}
for key in d1:
    print(key, ":", d1[key])

print(d1.get("hobbies"))
print(d1.get('marks').get('sci'))


print(sys.version)