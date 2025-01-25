import os

f = open("file.txt", "r")
# print(f.read())
# print(f.readline())
# print(f.readline())
# print(os.getcwd())

# by this you don't need to add file.close()
with open("file.txt", "r") as file:
    print(file.read())




# to read all line in file with readline method
# line = f.readline()
# while line != "":
#     print(line)
#     line = f.readline()
#
#
# f.close()

# readlines

# lines = f.readlines()
# print(lines)  # ['This is a text file\n', 'sec line\n', '3 line\n', 'fourth']

for l in f.readlines():
    print(l)
f.close()


