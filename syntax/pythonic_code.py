# Split & Join
items = "zero,one,two,three"
l = items.split(",")  # ['zero', 'one', 'two', 'three']
a, b, c, d = items.split(",")  # 언패킹까지 한 번에
items2 = "-".join(l)  # zero-one-two-three

####################################################
# List comprehensions
result = [i for i in range(10) if i % 2]  # [1, 3, 5, 7, 9]

# 2중 포문도 간결하게!
result = [i + j for i in "abc" for j in "abc" if not i == j]  # ['ab', 'ac', 'ba', 'bc', 'ca', 'cb']

# 2차원 리스트
result = [[i + j for i in "abc"] for j in "xyz"]  # [['ax', 'bx', 'cx'], ['ay', 'by', 'cy'], ['az', 'bz', 'cz']]

# 2차원 -> 1차원 리스트로
list = [e for l in result for e in l]  # ['ax', 'bx', 'cx', 'ay', 'by', 'cy', 'az', 'bz', 'cz']

########################################################################################################
# Enumerate
for idx, value in enumerate(['a', 'b', 'c']):
    print(idx, value)  # 0 a / 1 b / 2 c
list = list(enumerate(["a", "b", "c", "d"]))  # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]

# dict type으로 변환
dict = {i: v for i, v in enumerate("I like apple".split())}  # {0: 'I', 1: 'like', 2: 'apple'} <class 'dict'>

####################################################
# Zip
list1 = ['1', '2', '3']
list2 = ['a', 'b', 'c']
for x, y in zip(list1, list2):
    print(x, y)  # 1 a / 2 b / 3 c

a, b, c = zip((1, 2, 3), (10, 20, 30), (100, 200, 300))
print(a, b, c)  # (1, 10, 100) (2, 20, 200) (3, 30, 300)

[sum(x) for x in zip((1, 2, 3), (10, 20, 30), (100, 200, 300))]  # [111, 222, 333]

dict = {i: (a, b) for i, (a, b) in enumerate(zip(list1, list2))}  # {0: ('1', 'a'), 1: ('2', 'b'), 2: ('3', 'c')}

####################################################
# Lambda
f = lambda x, y: x - y
print((lambda x, y: x + y)(1, 4))  # 5

# if filter는 뒤에 붙인다. 반드시 else 붙여줘야 함.
print((lambda x: x ** 2 if x % 2 == 0 else x)(3))  # 3

####################################################
# Map
mylist = [1, 2, 3, 4, 5]
type(map(lambda x: x ** 2, mylist))  # <class 'map'> generator 상태
list(map(lambda x: x ** 2, mylist))  # [1, 4, 9, 16, 25]

# 두 개 이상의 list에도 적용 가능
list(map(lambda x, y: x * y, mylist, mylist))  # [1, 4, 9, 16, 25]

####################################################
# Reduce
from functools import reduce  # 누적 계산 -> 하나로 줄임


def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


factorial(3)  # 6
reduce(lambda x, y: x + y, [1, 2, 3, 4])  # 10