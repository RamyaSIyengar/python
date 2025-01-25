# Method #1: Using dictionary comprehension + count() + split()
from collections import Counter, defaultdict

# The combination of the above functions can be used to solve this problem.
# In this, we first split all the words and then perform a count of them using count() method.

test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'

res = {key: test_str.count(key) for key in test_str.split()}
print(str(res))

# --------------------------------------------------------------------

# Method #2: Using Counter() + split()
# we perform the task of counting using Counter() and separation of words using split().

test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'

res = Counter(test_str.split())
print(res)
print(dict(res))
print(str(dict(res)))


# ---------------------------------------------

# Method #4: Using defaultdict

test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'

listStr = test_str.split()

freq = defaultdict(int)

for word in listStr:
    freq[word] +=1

print(str(dict(freq)))

