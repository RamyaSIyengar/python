# Remove Duplicate Characters in a String


def remove_duplicates(str):
    result = ''
    for i in str:
        if i not in result:
            result+=i
    return result


input_str = "Automation Testing"
print(remove_duplicates(input_str))