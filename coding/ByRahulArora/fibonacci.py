# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# 0+1=1, 1+1=2 2+3=5

a = 0
b = 1
sum = 0


def fibonacci(n):
    fib_series = [0, 1]
    a=0
    b=1


    for i in range(2, n):
        # next_value = fib_series[-1] + fib_series[-2]
        # fib_series.append(next_value)
        sum = a+b
        print(sum)
        a = b
        b = sum

    # return fib_series
    # return sum


fibonacci(10)

# def fibonacci_recursive(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         fib_series = fibonacci_recursive(n-1)
#         fib_series.append(fib_series[-1] + fib_series[-2])
#         return fib_series
#
#
# print(fibonacci_recursive(10))
#
# # generator
# def fib(limit):
#     a1, b1 = 0, 1
#     while b1 < limit:
#         yield b1
#         a1, b1 = b1, a1+b1
#
#
# x = fib(200)
# # print(next(x))
# for i in x:
#     print(i)
#
#
#

