# Counter: iterable한 객체가 주어졌을 때 내부 원소의 등장 횟수를 세는 기능

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue'])  # 3
print(dict(counter))  # {'red': 2, 'blue': 3, 'green': 1}

# dict의 확장형. key 값에 대한 갯수
c = Counter()  # a new, empty counter
c = Counter('hello world')  # a new counter from an iterable
print(c)  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
print(c['l'])  # 3
print(list(c.elements()))  # ['h', 'e', 'l', 'l', 'l', 'o', 'o', ' ', 'w', 'r', 'd']

# 집합 연산
c = Counter(a=4, b=2, c=0)
d = Counter(a=1, b=2, c=3)
print(c - d)  # {'a': 3}. 차집합
c.subtract(d)
print(c)  # {'a': 3, 'b': 0, 'c': -3}
print(c & d)  # {'a': 1}
print(c | d)  # 'a': 3, 'c': 3, 'b': 2. 큰걸 취함
