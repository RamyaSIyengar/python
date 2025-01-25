# lambda - anonymys function
from inspect import isfunction

print(type(lambda a:a**2)) #<class 'function'>

f = lambda x,y=30: x*y
print(f(3))

def apply_func(fn, x):
    return fn(x)


print(apply_func(lambda x:x**2, 3))


print(apply_func(lambda x:x*2, 6))

print(apply_func(lambda s: s[1:]*3, 'abc'))


# with normal func
def fn(s:str):   # annotation
    return s[1:]*3


print(apply_func(fn, 'abc'))

# limitations of lambda
# body of the lambda is limited to single expression


fn = lambda x, *args, y, **kwargs: (x, args, y, kwargs)

print(fn(10, 'a', 'b', y=11, k=23, l=45))


def reapplied_func(fn, *args, **kwargs):
    return fn(*args, **kwargs)   # unpacking argument * and dict with**


print(reapplied_func(lambda x, y: x+y, 1, 2))  # 3

print(reapplied_func(lambda x, *, y: x*y, 2, y=32))  # 64

print(reapplied_func(lambda *args: sum(args), 1,2,3,4,5,6))

# sorted with lambda

l= ['B', 'a', 'C', 'd']
print(sorted(l))   # ['B', 'C', 'a', 'd']

print(ord('B'))  #66
print(ord('a'))  #97

print(sorted(l, key=lambda s: s.upper()))


d = {'def': 200, 'ghi': 100, 'abc': 200}

print(d)
for i in d:
    print(i)
print(sorted(d))   # ['abc', 'def', 'ghi']  sorts based on key

# if u want to sort for value
for i in d:
    print(d[i])

print(sorted(d, key=lambda key: d[key]))   # ['ghi', 'def', 'abc']  100, 200, 300

# complex nums with sorted and lambda
print(type(1+1j))

liOfCmplx = [1+2j, 0, 3+1j, 2+2j]

# print(sorted(liOfCmplx))  #error


def distance(x):
    return (x.real)**2 + (x.imag)**2


print(sorted(liOfCmplx, key=distance))
# [0, (1+2j), (2+2j), (3+1j)]

print(sorted(liOfCmplx, key=lambda x: (x.real)**2 + (x.imag)**2))


# randomize iterable using sorted
import random

print(f'random no between 0 to 1:{random.random():.2f}')

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sorted(l, key=lambda i: random.random()))


# functions are first class objects they have attribute __doc__ __annotations__
# we can attach our own attribute to function
f.catogary = 'math'
f.sub_catogary = 'arithematic'
print(f.catogary, f.sub_catogary)

#  dir - will give list of attributes of object passed
print(dir(f))
# ['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__',
#  '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
#  '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__',
#  '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__',
#  '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
#  '__str__', '__subclasshook__', 'catogary', 'sub_catogary']

print(f.__annotations__)
print(f.__name__)
print(apply_func.__name__)  # <lambda> =>lambda func
print(apply_func.__annotations__)  # apply_func => def func
print(f.__defaults__)  # (30,)  tuple => bcz y=30
print(f.__kwdefaults__)


from inspect import isfunction, ismethod

print(isfunction(f))  # True
print(ismethod(f))  # False

# print(f.__code__)
# print(dir(f.__code__))
# print(dir(f.__code__.co_name))
# print(dir(f.__code__.co_varnames))


# callables => ANY OBJECT THAT can be called using () not jus methods or func but more than that like below
#  returns something
print(callable(print))  # True
print(callable('abc'.upper))  # TRue
print(callable(10))  # False

# diff types of callables
# built-in func => print len callable
# built-in methods=>a_str.upper  a_list.append
# user defined func => using def or lambda
# methods bound to obj
# classes


