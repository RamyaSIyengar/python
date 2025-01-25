def countVowels(string):
    string = string.lower()
    vowels = 'aeiou'
    count = {v.lower(): 0 for v in vowels}

    for i in string:
        if i in vowels:
            count[i] += 1
    return count


print(countVowels("Quality Assurance"))