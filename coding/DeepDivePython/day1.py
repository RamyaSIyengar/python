# ternary operator
# X if (condition is true) else Y

a = 4

b = 'a < 5' if a < 5 else 'a >= 5'
print(b)

# function

def func(x: int, y:int):
    return x*y

print(func(3, 2))
print(func('a', 5))
res = func([1,2,4,6], 2)
print(res)
print(type(res))


# Reference counting
import sys
ar = [1,2,3]
print(id(ar))
print(sys.getrefcount(ar)-1)

def process(t):
    t[0].append(2)
    print(t)

tupl = ([1,2], 'a')
process(tupl)  #([1, 2, 2], 'a')


# ---------------------------string
my_var = 'hello'
print("Id of my_var {0}".format(id(my_var)))  # 3133646365104

def process(s:str):
    print("initial string s:{0}".format(id(s))) # 3133646365104
    s += ' world'
    print("modified string s:{0}".format(id(s))) # 3133646394672


process(my_var)

# -----------list---
def modify_lst(l):
    print("initial list:{0}".format(id(l))) #2857795996672
    l.append(4)
    print(l)
    print("modified list:{0}".format(id(l))) #2857795996672


ls = [1,2,3]
modify_lst(ls)

# ----------------tuple---
def modify_tuple(t):
    print("initial tuple:{0}".format(id(t)))  #
    t[0].append(10)
    print(t)
    print("modified tuple:{0}".format(id(t)))  #


t1 = ([1,2], 'a')
# you cannot add, remove or replace elements in the tuple.
# But if the element in the tuple is mutable, then you can certainly change
# its value in place.
# Immutability does not necessarily mean that nothing can change.
modify_tuple(t1)


# membership
def my_func(e):
    if e in [1,2,3]:
        pass


print(my_func.__code__.co_consts) #(None, (1, 2, 3))
# when we do list and sequence memberships, basically then the People Optimizer
# is going to transform any kind of mutable element into an immutable version
# of that element when it can.So in particular lists become tuples.
# if we use a set.Then when we look at the associated constants,the frozen set.


def my_func_set(e):
    if e in {1,2,3}:
        pass


print(my_func_set.__code__.co_consts) #(None, frozenset({1, 2, 3}))

# -------------

import string
import time

print(string.ascii_letters)

char_list = list(string.ascii_letters)
char_tuple = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)
print(char_list)

def membership_timetakes_test(n, container):
    for i in range(n):
        if 'm' in container:
            pass
strt = time.perf_counter()
membership_timetakes_test(10000000, char_list)
end = time.perf_counter()
print('list', end-strt)

strt_t = time.perf_counter()
membership_timetakes_test(10000000, char_tuple)
end_t = time.perf_counter()
print('tuple', end_t-strt_t)

strt_s = time.perf_counter()
membership_timetakes_test(10000000, char_set)
end_s = time.perf_counter()
print('set', end_s-strt_s)

# list 3.461554499983322
# tuple 3.5433188999886625
# set 0.6403787999879569
# set membership is faster than doing tuple or list membership.
# So whenever you can prefer using set membership.



