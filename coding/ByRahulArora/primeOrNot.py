#
# # . A prime number is a natural number greater than 1 that has no positive
# # divisors other than 1 and itself
# num = 67
# # Negative numbers, 0 and 1 are not primes
# if num > 1:
#
#     # Iterate from 2 to n // 2
#     # num is divided by 2, and the result is rounded down to the
#     # nearest whole number (if it's not already an integer).
#     for i in range(2, (num // 2) + 1):
#
#         # If num is divisible by any number between
#         # 2 and n / 2, it is not prime
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")


def is_prime(n):
    if n < 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        else:
            return True


print(is_prime(2))

# x = lambda a: a+10
# print(x(1))


# mul = lambda a, b: a*b
# print(mul(2, 10))
#
#
# def func(n):
#     return lambda a: a*n
#
# myDoubler = func(2)
# print(myDoubler(19))
#
# newlist = [x**2 for x in range(10) if x%2==0]
# print(newlist)


def primeOrNot(n):
    if n<1:
        return False
    else:
        for i in range(2, n+1):
            if n % i == 0:
                print(n, i)
                return False
            else:
                return True

print(primeOrNot(10))