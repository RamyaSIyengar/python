class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        elif str(x) == str(x)[::-1]:
            return True
        else:
            return False

s = Solution()
print(s.isPalindrome(-121))

s1 = 'amRay'
s2=''
for i in range(len(s1)):
    if s1[i].isupper():
        s2 += s1[i].lower()
        s1[i].lower()
    else:
        s2 += s1[i].upper()
print(s2)
