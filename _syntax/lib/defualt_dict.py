from collections import defaultdict

d = defaultdict(list)
print(d[1])  # []
d[1].append("first")
print(d[1])  # ['first']
d[1].pop()
print(d[1])  # [] 리스트는 이미 생성되어 버렸다.
"""초기값이 주어지지않을때만 default값으로 생성"""
# print(d[2][0]) #error 빈 리스트니까..
d[2] = "new"
print(d[2])  # 참조값을 리스트가 아닌 문자열로.

print(d.items()) # dict_items([(1, []), (2, 'new')])