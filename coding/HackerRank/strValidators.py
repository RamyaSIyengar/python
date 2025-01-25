s = 'qA2'

print(bool([[i] for i in s if i.isalnum()]))
print(bool([[i] for i in s if i.isalpha()]))
print(bool([[i] for i in s if i.isdigit()]))
print(bool([[i] for i in s if i.islower()]))
print(bool([[i] for i in s if i.isupper()]))


print(list(i**2 for i in range(5)))