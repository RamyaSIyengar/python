"""
Inheritance
Polymorphism
Data Abstraction
Encapsulation
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from abc import ABC, abstractmethod

class BasePage(ABC):

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.flipkart.com/")

    def click(self, locator):
        self.driver.find_element(By.XPATH, locator).click()

    def type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, locator).send_keys(value)

    # abstractmethod
    @abstractmethod
    def display(self):
        pass


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def display(self):
        logo = self.driver.find_element(By.XPATH, "//img[@title=\"Flipkart\"]")
        if logo.is_displayed:
            return print(self.driver.title)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
reg = RegistrationPage(driver)
reg.display()
mobile_XPATH = "//div[@class='_3sdu8W emupdz']/a[2]"
reg.click(mobile_XPATH)

driver.close()


# multiple inheritance
# When a child class inherits from multiple parent classes,

class Length:
    l = 0

    def length(self):
        return self.l


class Breadth:
    b=0

    def breadth(self):
        return self.b


class Rectangle_Area(Length, Breadth):

    def rec_area(self):
        return (f"Area of rectangle where length is {self.l} units and breadth is "
                f"{self.b} units is {self.l * self.b} sq. units.")


area = Rectangle_Area()
area.l = int(input("Enter a length of rectangle:"))
area.b = int(input("Enter a breadth of rectangle:"))
print(area.rec_area())

# Multilevel inheritance:

# When we have a child and grandchild relationship.
# This means that a child class will inherit from its parent class,
# which in turn is inheriting from its parent class.

# Generally, object is made ancestor of all classes

class Base(object):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Intermediate(Base):

    def __init__(self, name, age):
        Base.__init__(self,name)
        self.age = age

    def get_age(self):
        return self.age


class Derived(Intermediate):
    def __init__(self, name, age, address):
        Intermediate.__init__(self, name, age)
        self.address = address

    def address(self):
        return self.address


g = Derived("Ramya", 26, "Hari Nivasa")
print(g.get_age(), g.get_name(), g.address)


# Hierarchical inheritance More than one derived class can be created from
# a single base.
# Hybrid inheritance: This form combines more than one form of inheritance.
# Basically, it is a blend of more than one type of inheritance.


# access modifiers
class Login:
    _password = "ab12"  # protected
    __MFA = "232156"  # private

    def __init__(self, username):
        self.username = username


