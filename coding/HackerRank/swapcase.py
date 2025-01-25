def swap_case(s):
    s2 = ''
    # for i in range(len(s)):
    #     if s[i].isupper():
    #         s2 += s[i].lower()
    #     else:
    #         s2 += s[i].upper()

    return s.swapcase()

def mutate_string(string, position, character):
    s = list(string)
    s[position] = character
    s1 = ('').join(s)
    return s1

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

