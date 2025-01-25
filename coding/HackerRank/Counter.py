
from collections import Counter

x = 10
myList = [2, 3, 4, 5, 6, 8, 7, 6, 5 ,18
]
# myList = input().split()
myListCounter = Counter(myList)
N = 3
# N = int(input())
# print(Counter(myList).items())
money = 0
for _ in range(N):
        shoeSize, price = input().split()
        """
6 55
6 45
6 55
4 40
18 60
10 50
        """
        if str(shoeSize) in myListCounter:
            if (myListCounter[shoeSize]) >=1:
                money += int(price)
                myListCounter[shoeSize] -= 1
            else:
                continue

print(money)

#
#
#
#
# Task
#
#  is a shoe shop owner. His shop has  number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.
#
# Your task is to compute how much money  earned.
#
# Input Format
#
# The first line contains , the number of shoes.
# The second line contains the space separated list of all the shoe sizes in the shop.
# The third line contains , the number of customers.
# The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.
#
# Output Format
#
# Print the amount of money earned by .
#
# Sample Input
#
# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50
# Sample Output
#
# 200
# Explanation
#
# Customer 1: Purchased size 6 shoe for $55.
# Customer 2: Purchased size 6 shoe for $45.
# Customer 3: Size 6 no longer available, so no purchase.
# Customer 4: Purchased size 4 shoe for $40.
# Customer 5: Purchased size 18 shoe for $60.
# Customer 6: Size 10 not available, so no purchase.



# Enter your code here. Read input from STDIN. Print output to STDOUT

