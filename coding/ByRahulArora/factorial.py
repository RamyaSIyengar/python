# 5! = 5*4*3*2*1

def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *=i
    return res

print(factorial(5))


def recursive_factorial(n):
    if n==0 or n==1:
        return 1
    else:
        print(n,(n-1))
        return n*recursive_factorial(n-1)

print(recursive_factorial(5))