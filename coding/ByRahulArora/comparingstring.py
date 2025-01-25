
str1 = "welcome"
str2 = "Ramya"

if len(str1) != len(str2):
    print("not equal")
else:
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            print("not equal")
            break
    else:
        print("equal")


print(str1 == str2)
print(id(str1))
print(id(str2))


# reverse a string

print(str1[::-1])

s2=''
for i in range(len(str1)-1, -1, -1):

    # print(i)
    s2 += str1[i]

print(s2)




