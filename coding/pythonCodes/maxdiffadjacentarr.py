
# Max difference between any adjacent index in array
a = [1,4,8,15,17];
diff = 0
for i in range(len(a)-1):
    if a[i+1] - a[i] > diff:
        diff = a[i+1] - a[i]

print(diff)

# -------------------------compare 2 arrays
# compare same indexes of 2 different arrays and create anotherarray for matching values

a = [1,4,8,15,17];
b = [1,3,4,5,17]
a1=[]
for i in range(len(a)):
    if a[i] == b[i]:
        a1.append(a[i])
print(a1)
