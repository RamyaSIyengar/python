# 1  create student class that takes name and marks of 3 subjects as argument
# in constructor the create a method to print the average
import math


class Student:

    def __init__(self, name, marks=0):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, sum//3)


s1 = Student("Ramya", [85, 98, 91])
s1.get_avg()

s1.name = "Krishna"
s1.get_avg()


# 2  create account class with 2 attributes - balance and account no
# create methods for debit, credit and printing the balance

class Account:

    def __init__(self, balance, acc_num):
        self.balance = balance
        self.acc_num = acc_num

    def debit(self, debit_amt):
        self.balance -= debit_amt
        print("Rs-", debit_amt, "debited from your account", self.acc_num,
              "and the balance is", self.show_balance())

    def credit(self, credit_amt):
        self.balance += credit_amt
        print("Rs-", credit_amt, "credited to your account", self.acc_num,
              "and the balance is", self.show_balance())

    def show_balance(self):
        print(self.balance)


p1 = Account(500, 780941)
p1.debit(90)
p1.credit(900)
p1.show_balance()
# print(p1.acc_num)
print(p1)

del p1.acc_num
# print(p1.acc_num)


# 3 class - Circle with radius r, area method calculates are of the circle
# define perimeter() method of the class calculates the perimeter

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        peri = 2 * math.pi * self.radius
        return round(peri, 2)


cir1 = Circle(18)
print(cir1.perimeter())
print(cir1.area())



