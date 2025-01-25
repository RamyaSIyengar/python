# The first line of input contains the original string. The next line contains the substring.
# Each character in the string is an ascii character.
#
# Output Format
# Output the integer number indicating the total number of occurrences of the substring in the original string.


def count_substring(string, sub_string):
    occurrence = 0
    # print(string.count(sub_string))
    string = string.strip()
    sub_string = sub_string.strip()

    for i in range(len(string)):  # 7-3 = 4   +1 bcz its exclusive
        if string[i:i+len(sub_string)] == sub_string:
            print(string[i:i+len(sub_string)], sub_string)
            occurrence += 1
    print(occurrence)


# Step 1: The loop starts with i = 0. It extracts original_string[0:3] which is "ABC". This is not equal to "CDC", so the count is not incremented.
# Step 2: The loop continues with i = 1. It extracts original_string[1:4] which is "BCD". This is also not equal to "CDC".
#
# Step 3: For i = 2, the slice is original_string[2:5] which is "CDC". This matches the substring, so occurrences is incremented to 1.
#
# Step 4: The loop continues with i = 3, extracting "DCD". This is not equal to "CDC".
#
# Step 5: For i = 4, the slice is original_string[4:7] which is "CDC". This matches the substring, so occurrences is incremented to 2.
#
count_substring('ABCDCDC', 'CDC')
string = "dasara"
sub = "as"
count = 0
for i in range(len(string)):
    if string[i:i+len(sub)] == sub:
        count += 1
print("count", count)