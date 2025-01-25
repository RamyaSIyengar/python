s1 = "malayalam"



def reverse_str(s):
    s2 = ''
    for i in range(len(s)-1, -1, -1):
        s2 += s[i]
    return s2

print(reverse_str(s1))
print(s1[::-1])
if s1 == s1[::-1]:
    print("palindrome")
else:
    print("not a palindrome")




print(8**0.5)
print(8/4)
print(range(2, int(8**0.5) + 1))
