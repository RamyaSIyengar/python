arr = [10, 20, 4]
Output = 20

larg = arr[0]
for i in range(1, len(arr)):
    if arr[i] > larg:
        larg = arr[i]
print(larg)


# # Max difference between any adjacent index in array
arr = [1, 4, 8, 15, 17]

diff = 0

for i in range(0, len(arr) - 1):
    print(i)
    if arr[i + 1] - arr[i] > diff:
        diff = arr[i + 1] - arr[i]

print(diff)

# compare same indexes of 2 different arrays and create another array for matching values

a = [1, 4, 8, 15, 17]
b = [1, 3, 4, 5, 17]

c = []
for i in range(len(a)):
    if a[i] == b[i]:
        c.append(a[i])
print(c)

#
str1 = "aabaab"
low = 0
high = len(str1) - 1

while low < high:
    if str1[low] != str1[high]:
        print("not a palindrome")
        break
    low = low + 1
    high = high - 1

else:
    print("palindrome")

# symetry
half = len(str1) // 2
fh = str1[:half]
lh = str1[half:]
print(fh, lh)
if fh == lh:
    print("symm")

num = 12321
temp = num
rev = 0
while temp != 0:
    rem = temp % 10
    rev = (rev * 10) + rem
    temp = temp // 10
print(rev, num)
if rev == num:
    print("palin")
else:
    print("no")

# Initializing String
test_str = "GeeksForGeeks"

rev = ''
for i in test_str:
    rev = i + rev
print(rev)

# --substring
Substring = "geeks"
String = "geeks for geeks"

s = String.split()
print(s)
if Substring in s:
    print('yes')

# substr count String
test_str = "GeeksForGeeks"
sub_str = 'ek'

c = 0
for i in range(len(test_str)):
    if test_str[i:i + len(sub_str)] == sub_str:
        c += 1
print(c)

# swapping positions
my_list = [10, 20, 30, 40, 50]

i2 = 2
i4 = 4

my_list[i2], my_list[i4] =  my_list[i4],  my_list[i2]
print(my_list)

temp = my_list[1]
my_list[1] = my_list[3]
my_list[3] = temp
print(my_list)

# word occurenance and elements in array occurance

# find occurance of elements in array
a = [1, 2, 3, 4, 5, 1, 2, 3]
test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'

# from collections import Counter
#
# print(Counter(a))

# using dict
occurance = {}
for ele in test_str.split():
    if ele in occurance:
        occurance[ele] += 1
    else:
        occurance[ele] = 1

print(occurance)

# separate digits and alphabets from a string

input_str = "A678das%@"

digits = "".join([i for i in input_str if i.isdigit()])
alpha = "".join([i for i in input_str if i.isalpha()])
special_char = "".join([i for i in input_str if not i.isalnum()])

print(digits)
print(alpha)
print(special_char)


#  AAABBCC to A3B2C2

s = "AAABBCC"

res = ''
count = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count+=1
    else:
        res += s[i-1]+str(count)
        count = 1
# Append the last character and its count
last = s[-1]+str(count)
print(res)
print("".join(res+last))


# add digits in string

# Example usage
input_string = "AB150CCD230"

current_num = ''
res = 0

for i in input_string:
    if i.isdigit():
        current_num += i
    else:
        if current_num:
            res += int(current_num)
            current_num = ''

if current_num:
    res += int(current_num)

print(current_num)
print(res)


#
a = [1, 2, 3, [4, 5], 6, [7, 8]]

a1 = []
for i in a:
    if isinstance(i, int):  # Check if i is an integer
        a1.append(i)
    else:
        for j in i:
            a1.append(j)

print(a1)


#['mlk', 'zyx', 'cba']
input_list = ["abc", "xyz", "klm"]

l =[]
for i in input_list:
    l.append(i[::-1])

print(l[::-1])


# duplicate char in string

input_string = "programming"

char_count = {}
duplicates = set()

for char in input_string:
    if char in char_count:
        char_count[char] += 1
        duplicates.add(char)
    else:
        char_count[char] = 1  # Initialize count for new character

print(duplicates)
