
"""
3 types we can intialize the attributes

1. at the time of declaration
2. by using method
3. initializing from main function

"""


class Student:
    sec = "10th"  # 1 while declaring
    count = 0

    # constructor is defined using method name __init__ in the class
    # this method is automatically executed during object creation
    # main purpose of constructor in python is to declare and perform initialization of the object
    # constructor at least will take one argument which is self
    # we can hv one constructor per class
    # defining constructor is not mandatory at all if we dont provide python will provide one default constructor

    def __init__(self, name="Ramya"):  # 2 in constructor, parameterized constructor
        self.name = name
        Student.count = Student.count + 1


    def display(self):
        print(self.name)

    @staticmethod # static method can be directly accesed by class
    def do_read():
        print("Student is reading")

class Person:
    # Constructor - non parameterized
    def __init__(self):
        print("This is non parametrized constructor")
    def show(self,name):
        print("Hello",name)
        
person1 = Person()
person1.show("John")


class Employee:
    def __init__(self, name, id):
        self.id = id
        self.name = name
        self.marks =97.5

    def display(self):
        print("ID: %d \nName: %s\nMarks: %g" % (self.id, self.name, self.marks))


emp1 = Employee("John", 101)
emp2 = Employee("David", 102)

# accessing display() method to print employee 1 information

emp1.display()

# accessing display() method to print employee 2 information
emp2.display()


if __name__ == "__main__":
    s1 = Student("ram")
    print(s1.name, s1.sec)
    s1.age = 15  # 3 in main func
    print(s1.age)

    s2 = Student()
    print(s2.name)  # default argument

    Student.do_read() # static method
    print(Student.count)

