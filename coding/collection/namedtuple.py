from collections import namedtuple

xl = namedtuple('course', ['framework', 'language'])

x = xl('selenium', 'python')
print(x)   # course(framework='selenium', language='python')

print(x.framework)  # selenium

# converting it to tuple
print(x._asdict())  # {'framework': 'selenium', 'language': 'python'}

new = ['pytest', 'python']

print(x._make(new))
print(x)