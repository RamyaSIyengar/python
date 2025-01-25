print(type(1))
print(type(1.1))
print(type(True))
print(type('hi'))
print(type([1, 2, 3]))
print(type((4, 5, 6)))
print(type({1, 2, 3}))
print(type({'a': 1, 'b': 2}))

for i in [1, 2, 3]:
    print(i * 2 + 1)

dict1 = {'name': 'ramya', 'age': 26, 'maritial status': 'single',
         'occupation': 'software tester'
         }
print(dict1.items())
print(dict1.keys())
print(dict1.values())
for key, value in dict1.items():
    print(f"key-{key},value-{value}")

age = 26
if age > 18:
    print("eligible for licence")
else:
    print("not eligible for licence")


def welcome():
    print("Welcome to the fam")
welcome()

# parameterized func
def welcome(name):
    print(f"Welcome to the fam {name}")

welcome('ramya')


# Python Function Arguments
# 1. Default Arguments
def myfunc(x, y=20):
    print("x:{} and y:{}".format(x,y))


myfunc(10)  # x:10 and y:20
myfunc(15, 30)  # x:15 and y:30


# Positional Arguments
# if you forget the order of the positions, the values can be used in the wrong places
def mul(a, b):
    print(a*b)

mul(2,3)

# Keyword Arguments
mul(a=4, b=7)

# Arbitrary Keyword  Arguments
# *args in Python (Non-Keyword Arguments)
# **kwargs in Python (Keyword Arguments)


def myfunc(*args):
    print(args)  #tuple
    for arg in args:
        print(arg)


myfunc("Hello", "Ramya", "you", "been", "selected")


def keyfunc(**kwargs):
    """ function to check keyword args"""
    print(kwargs)  #dict
    for x,y in kwargs.items():
        print(x,":",y)


keyfunc(first='Geeks', mid='for', last='Geeks')
print(keyfunc.__doc__)

# lambda function
add1 = lambda x,y: x+y
print(add1(12,34))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4))

# raise exception
# try:
#     raise NameError("Hi there")
# except NameError:
#     print("An exception")
#     raise

# shallow copy
import copy
original = [[1, 2, 3], [4, 5, 6]]
shallow_copy = copy.copy(original)

print(id(original[0]))
print(id(shallow_copy[0]))
print()
shallow_copy[0][2] = 'c'
s_c = original.copy()
print(s_c)
print(original)  # [[1, 2, 'c'], [4, 5, 6]]

# deepcopy
original = [[1, 2, 3], [4, 5, 6]]
deep_copy = copy.deepcopy(original)

deep_copy[1][0] = 'R'
print(deep_copy)  # [[1, 2, 3], ['R', 5, 6]]
print(original)  # [[1, 2, 3], [4, 5, 6]]

o=original[:]
print()
print(id(original))
print(id(o))


# inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person name:{self.name}, age:{self.age}"


ramya = Person('Ramya', 26)
print(ramya)    # Person name:Ramya, age:26, company:TechM


class Student(Person):
    # When you add the __init__() function,
    # the child class will no longer inherit the parent's __init__() function.
    # The child's __init__() function overrides the inheritance of the parent's __init__() function.
    # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
    def __init__(self, name, age, id, college="KIT"):
        super().__init__(name, age)
        self.id = id
        self.college = college

    def student_details(self):
        print(f"name:{self.name}, age:{self.age}, id:{self.id}, college:{self.college}")


s1 = Student("Ramya", 26, id=58)
s1.student_details()


# Polymorphism
# method overloading -Python does not support method overloading in the traditional way

# method overriding

class Animal:
    def speak(self):
        return "some sound"

class Dog:
    def speak(self):
        return "woof"


class Cat:
    def speak(self):
        return "meow"


animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())


# operator overloading

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x+other.x, self.y+other.y

v1 = Vector(1,2)
v2 = Vector(3,4)
print(v1+v2)

# program to illustrate access modifiers of a class

# super class
class Super:

    # public data member
    var1 = None

    # protected data member
    _var2 = None

    # private data member
    __var3 = None

    # constructor
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

  # public member function
    def displayPublicMembers(self):

        # accessing public data members
        print("Public Data Member:", self.var1)

    # protected member function
    def _displayProtectedMembers(self):

        # accessing protected data members
        print("Protected Data Member:", self._var2)

    # private member function
    def __displayPrivateMembers(self):

        # accessing private data members
        print("Private Data Member:", self.__var3)

    # public member function
    def accessPrivateMembers(self):

        # accessing private member function
        self.__displayPrivateMembers()

# derived class
class Sub(Super):

      # constructor
    def __init__(self, var1, var2, var3):
        Super.__init__(self, var1, var2, var3)

      # public member function
    def accessProtectedMembers(self):

        # accessing protected member functions of super class
        self._displayProtectedMembers()

# creating objects of the derived class
obj = Sub("Geeks", 4, "Geeks!")

# calling public member functions of the class
obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()
print()

# Can also be accessed using
obj._displayProtectedMembers()
obj._Super__displayPrivateMembers()
print()

# Object can access protected member
print("Object is accessing protected member:", obj._var2)
print("Object is accessing private member:", obj._Super__var3)

# object can not access private member, so it will generate Attribute error
# print(obj.__var3)


class BasePage:
    def click_element(self, element):
        element.click()

class LoginPage(BasePage):
    def click_element(self, element):
        print("Login button clicked")
        super().click_element(element)

class DashboardPage(BasePage):
    def click_element(self, element):
        print("Dashboard button clicked")
        super().click_element(element)
# Here, LoginPage and DashboardPage override click_element from BasePage. This is dynamic polymorphism: the correct click_element version is invoked based on the object type at runtime.





