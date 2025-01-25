class Car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")


class Tata(Car):
    def __init__(self, name):
        self.name = name


car1 = Tata("nano")
car1.start()


# Multi level base -> derived -> derived
class Nano(Tata):
    def __init__(self, types, name):
        super().__init__(name)
        self.types = types
        print(self.name)


c = Nano('EV', "NanoTata")
c.stop()
print(c.name)


# Multiple inheritance

class Add:
    @staticmethod
    def add(a, b):
        return a + b


class Sub:
    @staticmethod
    def sub(a, b):
        return a - b

class MathOp(Add, Sub):
    def __init__(self):
        print("math operation can be done here")

operation = MathOp()
print(operation.add(1, 2))
print(operation.sub(10, 2))
