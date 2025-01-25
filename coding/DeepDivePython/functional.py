import datetime

l = [1,2,3,4,5]

a = l[0]
b = l[1:]
print(a)  # 1
print(b)  # [2, 3, 4, 5]


a, b = l[0], l[1:]
print(a)  # 1
print(b)  # [2, 3, 4, 5]

a, *b = l
print(a)  # 1
print(b)  # [2, 3, 4, 5]

# cant do in sets, sets do not have a concept of ordering.
s = {1,2,3,4}
# print(s[0]) TypeError: 'set' object is not subscriptable
# print(s[1:])

# string
st = 'python'
a, *b = st
print(a)
print(b)
# p
# ['y', 't', 'h', 'o', 'n']


# tuple
t = (1,2,3,5)
a, *b = t
print(a)  # 1
print(b)  # [2, 3, 5] list not a tuple

a,b,c ='xyz'
print(a,b,c)

a,*b,c = st
print(a, b, c)  # p ['y', 't', 'h', 'o'] n

a,b,c = st[0], st[1:-1], st[-1]
print(a,b,c)


l1 = [1,2,3]
l2 = [4,5,6]
t1 = (23, 45)
s1 = {'x','z','a'}
l3 = [*l1, *l2, *s1, *t1]  # [1, 2, 3, 4, 5, 6, 'a', 'x', 'z', 23, 45]


print(l3)

s2 = {9,8,7}
s3 = {6,5,4}
# print(s1 + s2)  # TypeError: unsupported operand type(s) for +: 'set' and 'set'
print(s1.union(s2))
s123 = [*s1, *s2, *s3]
s123 = {*s1, *s2, *s3}
print(s123)


d1 = {'key1': 1, 'key2': 2}
d2 = {'key3': 3, 'key4': 4}
print({*d1, *d2})  # {'key1', 'key3', 'key2', 'key4'}
print({**d1, **d2})  # {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4}

l = [1,2,3,4,5,'python']
a, *b, (c,*d) = l
print(a)  # 1
print(b)  # [2, 3, 4, 5]
print(c)  # p
print(d)  # ['y', 't', 'h', 'o', 'n']

print(l[0], l[1:-1], l[-1][0], list(l[-1][1:]))  # 1 [2, 3, 4, 5] p ['y', 't', 'h', 'o', 'n']
a, b,c,d = l[0], l[1:-1], l[-1][0], list(l[-1][1:])

print(a)  # 1
print(b)  # [2, 3, 4, 5]
print(c)  # p
print(d)  # ['y', 't', 'h', 'o', 'n']


def func(a,b,c):
    print(a,b,c)


l=[1,2,3]
func(*l) #unpacking

def func1(a,b, *args):
    print(args)

func1(1,2,3,4,5,6)  # (3, 4, 5, 6)


def func2(*args, d):
    print(args, d)

func2(1,2,3, 4, 5, d=6)
func2(d=1)  # () 1

def func3(*, d):
    print(d)

# func3(1,2,d=1)
# TypeError: func3() takes 0 positional arguments but 2 positional arguments (and 1 keyword-only argument) were given

func3(d=1)

def func4(a, b, *, d):
    print(a, b, d)

func4(1,2,d=12)

# --- **kwargs**---------
def func5(*, d, **kwargs):
    print(d, kwargs)

func5(d=1, host = 'localhost', user='user', passwd='root')
# 1 {'host': 'localhost', 'user': 'user', 'passwd': 'root'}

def func6(*args, **kwargs):
    print(args)  # tuple  (1, 2, 3)
    print(kwargs)  # dict {'name': 'ram', 'gender': 'male'}

func6(1,2,3,name='ram', gender = 'male')
func6()
# ()
# {}

print(1,2,3, sep='*', end='\t')  # 1*2*3	1
print(1)

print(int(bool([1,2])))  # 1
print(int(bool()))  # 0

def cal_hi_low_avg(*args, log_to_console=False):
    hi = int(bool(args)) and max(args)  # if args are present it will be 1 and max() or it will return 0
    lo = min(args) if len(args)>0 else 0

    avg = (hi+lo)/2
    if log_to_console:
        print("high:{0}, low:{1}, avg:{2}".format(hi, lo, avg))

    return avg

is_debug = True
avg = cal_hi_low_avg(1,2,5,4,5,6,7)
print(avg)

def time_it(fn, *args, **kwargs):
    fn(*args, **kwargs)

time_it(print, 1,2,3,4,sep='*', end='\n')


def log(msg, *, dt=None):
    dt = dt or datetime.datetime.now()
    print("{0}:{1}".format(dt, msg))

log("msg1", dt='2024-10-1 13:20:30.6723')
log("msg2")
log('msg3')