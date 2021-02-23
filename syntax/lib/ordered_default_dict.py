# OrderedDict: 데이터를 입력한 순서대로 반환하는 dict
# Dict type의 값을 value 또는 key 값으로 정렬할 때 유용
from collections import OrderedDict

d = OrderedDict()
d['x'] = 300
d['y'] = 200
d['z'] = 100

# key 값을 기준으로 정렬
for k, v in OrderedDict(sorted(d.items(), key=lambda t: t[0])).items():  # t:tuple, t[0]:key, t[1]:value
    print(k, v)
# value 값을 기준으로 정렬
for k, v in OrderedDict(sorted(d.items(), key=lambda t: t[1])).items():
    print(k, v)
for k, v in OrderedDict(sorted(d.items(), reverse=True, key=lambda t: t[1])).items():
    print(k, v)

"""
"""

# defaultdict: 기본 값을 설정할 수 있는 dict
# 갯수 셀 때 유용
from collections import defaultdict

d = defaultdict(object)  # Default dictionary 생성. int, list, set 등 설정 가능
d = defaultdict(lambda: 0)  # default 값을 0으로 설정
print(d["something"])  # {"something":0}이 생성된다.

""" 갯수 셀 때 활용 예 """
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
