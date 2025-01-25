import array as arr

a = arr.array('i', [1,2,3,6])
b = arr.array('f', [2, 3, 4])
print(b)
print(type(a))

sumArr = 0
for i in a:
    sumArr+=i
print(sumArr)


l1 =[1,2,3,1]

s1 = {1,4,5,6}
print(s1)
for i in s1:
    print(i)

if 4 in s1:
    print('yes')

print(set(l1))


#  ------------------ assignment1 ---------


# have an arr and find which element is odd or even in the same

import array as arr

ar1 = arr.array('i', [22, 43, 69, 11, 43])

evenCount = 0
oddCount = 0

for i in ar1:
    if i%2==0:
        evenCount+=1
    else:
        oddCount+=1

print(oddCount, "odd nos")
print(evenCount, "even nos")