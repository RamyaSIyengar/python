# Python is a Object oriented programming
# everything in python is an object with its properties and methods
# class is object constructor, it's a blueprint for creating objects.
# object is an instance of a class, objects has state and behavior
# A class is a blueprint that defines state and behaviour of the objects

# 1. user orders food
#     I can order pizza, burger, roti
# user has attribute name, gender, age
# methods - orderFood(), payBills()


class Car:
    """it's a car class
    whenever we create an instance variable they hv to be accessible throughout
    the lifecycle of the object
    """

    # Car attributes
    # instance variables
    name = "Tesla"
    wheels = 4
    transportMode = "Road"

    # Car methods
    def drive(self):
        accelarate = "speed"
        print("driving the car {} and {} increased".format(self.name, accelarate))

    def stop(self):
        pass
        # print("stopping the car by decreasing the speed {}".format(self.accelerate))
        # AttributeError: 'Car' object has no attribute 'accelerate'
        # cant access local variable which is created without self keyword in other function


if __name__ == "__main__":
    print(Car.__doc__)  # it's a car class
    print(Car.__name__)  # Car
    help(Car)
    newCar = Car()   # now newCar is a reference variable for the obj of the class
    # we can use reference variable to access attributes and methods of the class
    print(newCar.name)
    newCar.drive()
    newCar.stop()


"""
Help on class Car in module __main__:

class Car(builtins.object)
 |  its a car class
 |  
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

"""
