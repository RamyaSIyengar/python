class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Animal class"

    def sound(self, sound):
        return f"{self.name} is making sound: {sound}"


A1 = Animal("dog")
print(A1)
print(A1.name)
print(A1.sound("woof"))

# List
l1 = [1, 2, 3, 4, 5]
print(l1)
for _ in l1:
    print(_ % 2 == 0)
l1[2] = 3 * 3 // 2 - 1
print(l1)

print(l1[::-1])
r = []
for i in range(len(l1) - 1, -1, -1):
    r.append(l1[i])
print(r)

l1.insert(1, 11)
print(l1)
l1.pop(4)
print(l1)
print(l1.count(1))
del l1[1]
print(id(l1))
# l1.clear()
# print(l1)

l2 = l1.copy()
print("l2", l2)
print(id(l2))

print(l1 + l2)

l3 = [12, 34, 56]
l1.extend(l3)
print(l1)

a, b, *c = r

# tuple
print("------------tuple-----")
t1 = (1, 2, 3, 4, 4)
# t1[1] = 3  # TypeError: 'tuple' object does not support item assignment

print(len(t1))
print(type(("apple")))  # <class 'str'>
print(type(("apple",)))  # <class 'tuple'>
t2 = t1  # copying
print("t2", t2)
print(t1 + t2)
print(t1.count(4))
print(t1.index(4))
# del t1
# print(t1) # NameError: name 't1' is not defined

print("----set---------")

s1 = {1, 2, 3, 4, 5, 5}
# print(s1[2]) #TypeError: 'set' object is not subscriptable
s2 = {True, 1}
s3 = {21, 43}
print(s2)

for i in s1:
    print(i)

# s1[2] = 23  #TypeError: 'set' object does not support item assignment
s1.add(6)
print(s1)
s1.update(s3)
print(s1)
s4 = s1.union(s3)  # returns new set s1|s3
s5 = s1.intersection(s3)
print(s5)

# s1.remove(10)  #KeyError: 10
s1.discard(10)  # doesnt throw err if element not present

# function
print("------------Function-----")

name = "Ramya"


def myf():
    global name
    print(id(name))
    name = "Ram"
    print("inside", name)


myf()
print(id(name))
print("outside", name)

#  to get random num
import random

print(random.randrange(10))

# string
print("------------string-----")

a = 'rAmya '
print(a[1:])
print(len(a))
for i in a:
    print(i)
if 'b' not in a:
    print('yes')
print(a[1:4])
print(a[:3])
print(a[-4:-2])

print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace('r', 'm'))
print(a)
greet = "hello world"
a1 = greet.split(" ")
print(a1)

num1 = int(input("enter a num:")) | 0
print(num1 * 2)







