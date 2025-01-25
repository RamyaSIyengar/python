# Reverse Words in a Given String in Python


# Input : str =" geeks quiz practice code"
# Output : str = code practice quiz geeks

# Method

# Separate each word in a given string using split() method of string data type in python.
# Reverse the word separated list.
# Print words of the list, in string form after joining each word with space using
# ” “.join() method in python.


# Using Split, Reverse and Join
str =" geeks quiz practice code"


strList = str.split()
reverse = []

for i in range(len(strList)-1, -1, -1):
    reverse.append(strList[i])

print(" ".join(reverse))
# code practice quiz geeks

str1 = "geeks"
print(str1[::-1])

# ------------------------------------

string = "hello"
reversed_string = ''
for i in string:
    reversed_string = i + reversed_string
print(reversed_string)