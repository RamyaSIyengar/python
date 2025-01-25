# 1.  An iterator is an object that can be iterated upon meaning
# you can traverse through all the values

# iterator is an obj that contains countable number of elements

# in Python, an iterator is an object which implements the iterator protocol,
# which consist of the methods __iter__() and __next__().

class Itera:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        self.a +=1
        return self.a


ob = Itera()
ob1 = iter(ob)
print(ob1)  # <__main__.Itera object at 0x00000193DDA67610>
print(next(ob1))
print(next(ob1))
print(next(ob1))

# 2. Lists, tuples, dictionaries, and sets are all iterable objects.
# They are iterable containers which you can get an iterator from.

# All these objects have a iter() method which is used to get an iterator:


list1 = [1,4,5,7,32]
a = iter(list1)
print(a)  # <list_iterator object at 0x000001F4F5557D90>
print(next(a))  # 1
print(next(a))  # 4
print(next(a))  # 5

tuple1 = (0,6,5,23,1)
b = iter(tuple1) # <tuple_iterator object at 0x000002B4DA957D60>
print(b)
print(next(b))
print(next(b))
