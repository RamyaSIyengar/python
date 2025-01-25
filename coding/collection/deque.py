from collections import deque

list1 = ['a', 'd', 'c', 1, 90]
list1 = deque(list1)
print(type(list1))

list1.append('good')  # deque(['a', 'd', 'c', 1, 90, 'good'])

list1.appendleft('very') # deque(['very', 'a', 'd', 'c', 1, 90, 'good'])

list1.pop()  # deque(['very', 'a', 'd', 'c', 1, 90])

list1.popleft()  # deque(['a', 'd', 'c', 1, 90])

list1.extendleft([1, 3, 5])  # deque([5, 3, 1, 'a', 'd', 'c', 1, 90])

