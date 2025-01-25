import time

from selenium.webdriver.common.by import By

str1 = "python"
ch = "o"

print(str1.replace(ch, " "))
print(str1)

# 2. Python Program to count occurrence of characters in string

string = "python"
char = "y"

count = 0

for i in string:
    if i == char:
        count += 1
print(count)

# 3. Python program in to check string is anagrams or not
string1 = "ypothn"
if sorted(string1) == sorted(string):
    print("anagram")
else:
    print("not an anagram")

# 4. Python program to check string is palindrome or not
string = "madam"
if string == string[::-1]:
    print("palindrome")

s= ''
for i in range(len(string)-1, -1, -1):
    s += string[i]
if s == string:
    print("palindrome")

# 5. Python code to check given character is digit or not
ch = 'a'

if ch >= '0'  or ch <= '9':
    print("digit")
else:
    print("not a digit")

# 6. Program to replace the string space with any given character
string = "m d m"
ch = "a"

result = ''
for i in string:
    if i == ' ':
        i=ch
    result+=i
print(result)

# 7. Counting Vowels in a Given Word
word = "programming"
vowels = ['a', 'e', 'i', 'o', 'u']

count = 0
for i in word:
    if i in vowels:
        count+=1
print(count)

# 5. Counting Consonants in a Given Word
countCon=0
for i in word:
    if i not in vowels:
        countCon +=1
print(countCon)

# 6. Counting the Number of Occurances of a Character in a String
word = "pythonp"
character = "p"

count = 0
for i in word:
    if i == character:
        count += 1
print(count)


# 7. Writing Fibonacci Series

fib = [0, 1]
n = 5

for i in range(5):
    next_value = fib[-1] + fib[-2]
    fib.append(next_value)
print(fib)
print(", ".join(str(e) for e in fib))

# 8. Finding the Maximum Number in a List
numberList = [15, 85, 35, 89, 125]
maxnum = numberList[0]

for i in numberList:
    if i > maxnum:
        maxnum = i
print(maxnum)

# 10. Finding the Middle Element in a List
numList = [1, 2, 3, 4, 5]

middle = int(len(numList)/2)
print(numList[middle])

# 11. Converting a List into a String
lst = ["P", "Y", "T", "H", "O", "N"]

str1 = "".join(lst)
print(str1.split(" "))
print(str1)

 # Adding Two List Elements Together
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

lst3 = []

for i in range(0, len(lst1)):
    lst3.append(lst1[i] + lst2[i])
print(lst3)

# 15. Counting the White Spaces in a String
string = "P r ogramm in g "
print(string.count(" "))

# reverse an arr

arr = [1, 2,3,4]
print(arr[::-1])

for i in range(len(arr)-1,-1, -1):
    print(arr[i])

# Given an array, the task is to cyclically rotate the array clockwise by one time.

# Input: arr[] = {1, 2, 3, 4, 5}
# Output: arr[] = {5, 1, 2, 3, 4}

# Assign every element with its previous element and first element with the last element .
arr = [1, 2, 3, 4, 5]
last_ele = arr[-1]
# for i in range(len(arr)-1, 0, -1):
#     arr[i] = arr[i-1]
#
# arr[0] = last_ele

print(arr)

l = arr[len(arr)-1]
for i in range(len(arr)-1, 0, -1):
    arr[i] = arr[i-1]
arr[0] = l
print(arr)

# duplicate char

str1 = "NAINAE"
str2 = "REENE"

str3=''
for i in str1:
    for j in str2:
        if i==j:
            if i not in str3:
                str3 +=i

print(str3)

# sum eq to two nos in arr

arr = [5, 7, 4, 3, 9, 8, 19, 21, 10]
sum1 = 17

arr.sort()
print(arr)

sumarr = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == sum1:
            sumarr.append([arr[i], arr[j]])
print(sumarr)


# smallest diff in an arr
arr = [5, 32,45, 12, 18,25]

arr.sort(reverse=True)
print(arr)
diff = arr[0]-arr[1]

print(diff)

for i in range(1, len(arr)-1):
    a=min(diff, arr[i]-arr[i+1])
print(a)


class BasePage:

    def click(self, by, value):
        # self.driver.find_element(by, value)
        print(by, value)

class MethodOverriding(BasePage):
    def click(self, by, value):
        print("clicking login element")
        super().click(by, value)

m = MethodOverriding()
m.click(By.NAME, "q")

print(time.asctime())