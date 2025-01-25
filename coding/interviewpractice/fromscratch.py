# 42.as_integer_ratio()
import time
from collections import Counter

print((42).as_integer_ratio())


# When you want to call a method directly on an integer literal,
# you need to wrap the integer in parentheses to avoid a SyntaxError.
# This is because the dot character (.) can be interpreted as a decimal point
# in Python, which leads to confusion with the syntax for floating-point numbers.
# For example, (42).as_integer_ratio() works correctly, but 42.as_integer_ratio() results in a syntax error:


my_dict = {
    'fname': 'Ramya',
    'lname': 'iyengar'
}

for i, j in my_dict.items():
    print(f"{i}:{j}")

# list comprehension

x = [2,3,4,5,6]

print([i**2 for i in x])
print([i**2 for i in [9,8,7]])

print([i for i in range(11) if i%2==0])

# matrix

print([[j for j in range(2)] for i in range(3)])

# dict comprehension
print({x: x**2 for x in [1,2,3] if x%2==0})

# combining 2 lists
# Comprehensions allow for multiple iterators and hence, can be used to combine multiple lists into one.


a = [1,2,3]
b = [4,5,6]

print([x + y for x, y in zip(a, b)])  # parallel iterators
print([(x, y) for x in a for y in b]) # nested iterators

# lambda
mul = lambda a, b: a*b
print(mul(2,3))


# lambda inside another func
def wrapper(n):
    return lambda a: a*n


doubler = wrapper(2)
print(doubler(10))

# split and join
"""
You can use split() function to split a string based on a delimiter to a list of strings.
You can use join() function to join a list of strings based on a delimiter to give a single string.
"""

str1 = 'this is a string'
str1_list = str1.split(' ')
print(str1_list)  # ['this', 'is', 'a', 'string']
list_to_str = " ".join(str1_list)
print(list_to_str)  # this is a string


# *args
# *args allows a function to accept any number of positional arguments.
# The * in front of args tells Python to pack all the extra
# positional arguments into a tuple. This way, you can pass multiple arguments
# to the function, and they will be stored as a tuple.

def addtupleitems(*args):
    sum = 0
    for a in args:
        sum += a
    print(sum)

addtupleitems(1,2,23,45,12)

# **kwargs
# **kwargs allows a function to accept any number of keyword arguments.
# The ** tells Python to pack all the extra keyword arguments into a dictionary
# where the keys are the argument names, and the values are the arguments passed.

def addDictitems(**kwargs):
    for i, j in kwargs.items():
        print(f"{i}:{j}")

addDictitems(name="Ramya", place="tiptur")


def example_combined(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


example_combined(1, 2, 3,4, name="Alice", age=30)

# time.sleep(-100)


def palindrome(string):
    s = ''
    for i in range(len(string)-1, -1, -1):
        s += string[i]
    if s == string:
        return True
    else:
        return False

    # if string == string[::-1]:
    #     return True
    # else:
    #     return False

print(palindrome("maam"))


def is_symetrical(s):
    mid = len(s)//2
    print(mid)
    if len(s)%2 == 0:
        return s[:mid] == s[mid:]
    else:
        return s[:mid] == s[mid+1:]

print(is_symetrical("amaama"))
print(palindrome("amaama"))

# Reverse Words in a Given String in Python
# Input : str =" geeks quiz practice code"
# Output : str = code practice quiz geeks

strin = "geeks quiz practice code"

strin_l = strin.split()[::-1]
print(' '.join(strin_l))

l = []
for i in strin_l:
    l.append(i)
print(" ".join(l))


# 3. Count the Number of Vowels in a String

def countVowels(s):
    vowels = 'aeiou'
    count = 0
    for char in s:
        if char in vowels:
            count +=1
    return count
print(countVowels("Ramyae hello"))


# remove duplicate character
def remove_duplicates(s):
    return ''.join(sorted(set(s), key=s.index))


print(remove_duplicates("ramya"))

# Count Words in a Sentence
def count_words(s):
    return len(s.split(' '))

print(count_words("This is a test sentence"))  # Output: 5

# capitalize
a ="rama".split()
print(a[0].capitalize())

l = 'hello'
c = Counter(l)
print(c)

# Input: Substring = "geeks"
# String="geeks for geeks"
# Output: yes

Substring = "geeks"
String="geeks for geeks"

if Substring in String:
    print('yes')

#word frequency
test_str = 'Gfg is best'
# Output : {'Gfg': 1, 'is': 1, 'best': 1}

print(Counter(test_str.split()))

# Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n
num = 6

factorial = 1
for i in range(1, num+1):
    factorial *= i
print(factorial)

def factorial(n):
    return 1 if n==0 or n==1 else n*factorial(n-1)


print(factorial(6))


# Given an array, find the largest element in it.
# Input : arr[] = {10, 20, 4}
# Output : 20

ar = [10, 20, 4]
l =ar[0]
for i in ar:
    if l < i:
        l = i
print(l)