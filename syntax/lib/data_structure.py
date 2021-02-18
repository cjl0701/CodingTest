# collections 모듈
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])  # type name, data
p = Point(11, y=22)
print(p[0] + p.y)  # 33
print(Point(x=1, y=2))  # Point(x=1, y=2)

"""
from collections import OrderedDict
from collections import defaultdict

d = defaultdict(object)  # Default dictionary 생성. int, list, set 등 설정 가능
d = defaultdict(lambda: 0)  # default 값을 0으로 설정
print(d["something"])  # {"something":0}이 생성된다.

# 갯수 셀 때 유용
text = "a b a c b a".split()
for word in text:
    # if not word in d: d[word]=0
    d[word] += 1
for i, v in OrderedDict(sorted(d.items(), key=lambda t: t[1], reverse=True)).items():
    print(i, v)

# defaultdict(list) 활용 예
word_list = [('a', 'apple'), ('a', 'age'), ('b', 'big')]
wdict = defaultdict(list)  # key에 대해 value가 list 타입이 기본값
for w, word in word_list:
    wdict[w].append(word)
print(wdict)  # {'a': ['apple', 'age'], 'b': ['big']}
"""
"""
from collections import OrderedDict

# Dict와 달리, 데이터를 입력한 순서대로 반환
d = OrderedDict()
d['x'] = 300
d['y'] = 200
d['z'] = 100
# Dict type의 값을 value 또는 key 값으로 정렬할 때 유용
# key 값을 기준으로 정렬
for k, v in OrderedDict(sorted(d.items(), key=lambda t:t[0])).items(): # t:tuple, t[0]:key, t[1]:value
    print(k,v)
# value 값을 기준으로 정렬
for k, v in OrderedDict(sorted(d.items(), key=lambda t:t[1])).items():
    print(k,v)
for k, v in OrderedDict(sorted(d.items(), reverse=True, key=lambda t:t[1])).items():
    print(k,v)
"""
"""
# deque
from collections import deque

deq = deque()
for i in range(5):
    deq.append(i)  # 오른쪽 삽입
deq.appendleft(-1)
print(deq)  # deque([-1, 0, 1, 2, 3, 4])

# 기존 list 형태의 함수를 모두 지원
deq.extend([5,6])
deq.extendleft([-2,-3]) #왼쪽으로 차례대로 붙음
print(deq) # deque([-3, -2, -1, 0, 1, 2, 3, 4, 5, 6])

# rotate, reverse 등 Linked List의 특성을 지원.
deq.rotate(2) # 2칸 움직임
print(deq) # deque([5, 6, -3, -2, -1, 0, 1, 2, 3, 4])
print(deque(reversed(deq))) # deque([4, 3, 2, 1, 0, -1, -2, -3, 6, 5])
"""
"""
# 리스트를 사용해 스택 , 큐 구조를 활용
a = [1, 2]
a.append(3)
a.append(4)
# 스택
print(a.pop())
# 큐
print(a.pop(0))
# print(a)

"""
