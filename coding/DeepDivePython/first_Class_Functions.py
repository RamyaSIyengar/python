# docString
cache = {}
def fact(n):
    """
    Calculates n! factorial function
    :param n: non-negative number
    :return: the factorial of n
    """
    if n == 0 or n == 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print("getting factorial of {0}".format(n))
        cache[n] = n*fact(n-1)
        return cache[n]

print(fact.__doc__)
help(fact)
print(fact(8))

# Function Annotation
# it gives us to additional way an additional document our functions

# def my_func(a: <expression>, b: <expression>) -> <expression>:
#     pass

def my_func(a: "str", b: "int>0") -> "returns string":
    return a*b

help(my_func)  # my_func(a: 'a string', b: 'a string') -> 'returns string'
print(my_func.__doc__)

print(my_func('ram', 2))


# with args and kwargs
def my_func(a: str = "ram",
            *args: 'additional parameters',
            b: int = 1,
            **kwargs: 'additional keyword only params') -> str:
    return a*b*args[0]

print(my_func("sham",2,3))

print(my_func.__annotations__)
# {'a': <class 'str'>, 'args': 'additional parameters', 'b': <class 'int'>,
# 'kwargs': 'additional keyword only params', 'return': <class 'str'>}


a = 3
b = 5


def maxrepeat(x: 'some character') -> 'character x repeated ' + str(max(a,b)) + " times":
    return x * max(a,b)


print(maxrepeat("a"))
print(maxrepeat.__annotations__)


# lambda

# lambda [parameter list] : expression

l = lambda s: s.upper()+"-"+s[::-1].upper()
print(l("python")) # PYTHON-NOHTYP
print(type(l))  # <class 'function'>


# PASSING LAMBDA AS another func
def apply_func(x, fn):
    return fn(x)


print(apply_func(x=3, fn = lambda x: x**2))
print(apply_func(2, lambda y: y+4))
print(apply_func())
