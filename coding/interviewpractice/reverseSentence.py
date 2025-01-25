sen = "Ramya is awesome"

# s = sen.split(" ")
# print(sen)
# print(s)
#
# s1 = ""
#
# for i in s:
#     rev = i[::-1]
#     s1 = s1 + rev + " "
# print(s1)


def reverse_sentence(sentence):

    if len(sentence) == 1:
        return sentence
    else:
        s = sentence.split(" ")
        s1 = ""

        for i in s:
            rev = i[::-1]
            s1 = s1 + rev + " "
        print(s1)
        print(s1[::-1].strip())


reverse_sentence(sen)
