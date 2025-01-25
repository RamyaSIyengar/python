num1 = 2
num2 = 3


sum = num1+num2
print(sum)

# num1 = int(input("num1:"))
# num2 = int(input("num2:"))
#
# print(num1+num2)
def addNum(a, b):
    return a+b

print(addNum(11,9))


sum =lambda a, b: a+b
print(sum(2,2))