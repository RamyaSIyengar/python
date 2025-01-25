def are_anagrams(str1, str2):
    # If lengths are not equal, they cannot be anagrams
    if len(str1) != len(str2):
        return False

    # Sort both strings and compare them
    return sorted(str1) == sorted(str2)

# Example Usage:
str1 = "listen"
str2 = "silent"
print(are_anagrams(str1, str2))  # Output: True

str1 = "hello"
str2 = "world"
print(are_anagrams(str1, str2))  # Output: False
