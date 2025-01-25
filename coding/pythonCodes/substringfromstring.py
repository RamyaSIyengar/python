Substring = "geeks"
String="geeks for geeks"

print(String.split())

for i in String.split():
    if i == Substring:
        print('yes')

# -----------------------------------
string = "Dasara festival"
substring = "as"

for i in range(len(string)):
    if string[i:i+len(substring)] == substring:
        print(i)

print(string.count(substring))
