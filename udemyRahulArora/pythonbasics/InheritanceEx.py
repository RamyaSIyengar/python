"""

Inheritance:


Class A ---> Base Class  / Parent Class - Single level Inheritance

    def add(self):

Class B ---> Derived Class / Child Class


so from Inheritance we can access members, properties and methods from the another class

A <--- B <--- C - MultiLevel Inheritance

A    B --> Multiple Inheritance

  C

"""

class AnimalParent:
    def ap(self):
        print("Inside the Animal Parent class")

    def hello(self):
        print("Hello from Animal Parent class")


class Animal:
    name = "Rahul"
    def a(self):
        print("I am inside Animal class")

    def hello(self):
        print("Hello from Animal class")


class Mammals(AnimalParent, Animal):
    def b(self):
        print("I am inside Mamals class")


mam = Mammals()
mam.b()
mam.a()
print(mam.name)
mam.ap()
mam.hello()


# method resolution order in inheritance

# if you want to do polymorphism - inheritance shd be there
# method overloading and constructor overloading is not supported in python
