str1 = "RAMYA"
str2 = "RASHMI"
#
# # my attempt
# duplicate = ""
# for i in str1:
#     for j in str2:
#         if i == j:
#             if i not in duplicate:
#                 duplicate+=i
# print(duplicate)

# 2nd attempt
newstr1 = set(str1)
newstr2 = set(str2)
print(newstr1, newstr2)

d=''
for i in newstr1:
    for j in newstr2:
        if i==j:
            d = d + i

print((', ').join(d))


# function and using set approach

def common_letters(s1, s2):
    # s1 = input("Enter first string:").lower()
    # s2 = input("Enter Second string:").lower()

    s1 = set(s1)
    s2 = set(s2)

    lst = s1.intersection(s2)
    lst1 = s1.union(s2)
    print(lst)
    print(lst1)


common_letters(str1, str2)
