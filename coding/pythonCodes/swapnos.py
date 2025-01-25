my_list = [10, 20, 30, 40, 50]

# Swap elements at index 1 and 3
pos1, pos2 = 1, 3


my_list[pos1], my_list[pos2] = my_list[pos2], my_list[pos1]

print(my_list)

# --------------------------------
my_list = [10, 20, 30, 40, 50]

temp = my_list[1]
my_list[1] = my_list[3]
my_list[3] = temp

print(my_list)


