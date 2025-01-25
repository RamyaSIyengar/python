# we can use a loop to compare characters from the start and end moving towards the middle.
# For checking symmetry, we split the string into two halves and compare them.
# Palindrome of string


# str1 = input("enter a string")
str1 = "aabbaa"
low = 0
high = len(str1)-1

while low < high:
    if str1[low] != str1[high]:
        print("Not a palindrome")
        break
    low = low+1
    high = high-1

else:
    print("palindrome")



# 2nd method

if str1 == str1[::-1]:
    print("palindrome")

# a string is said to be a palindrome string if one half of the string is the reverse of the
# other half or if a string appears the same when read forward or backward.

# A string is said to be symmetrical if both the halves of the string are the same

string = 'amaaama'

half = len(string)//2

print(string[:half])
print(string[half:])


# ----------------------------------------------------------
# Write a program to check if the given number is palindrome or not.
num = 12321

def check_palindrome(num):
    # Copy of the original number so that the original
    # number remains unchanged while finding the reverse
    temp = num
    reverse = 0
    while temp!=0:
        reminder = temp%10
        print(reminder)
        reverse = (reverse * 10) + reminder
        print(reverse)
        temp = temp //10
        print(temp)
    if num == reverse:
        print("palindrome")
    else:
        print("not a palindrome")

check_palindrome(12321)
