my_name = "Ramya"


def count_char(name):
    count = 0
    for i in range(len(name)):
        if name[i] == ' ':
            continue
        count += 1
    return count


print(count_char("Ramya "))
print(len("Ramya "))