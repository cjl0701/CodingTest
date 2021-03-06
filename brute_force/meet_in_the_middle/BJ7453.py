# 합이 0인 네 정수
import sys
from collections import Counter

n = int(sys.stdin.readline())
temp = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
a, b, c, d = zip(*temp)  # zip: 같은 인덱스에 있는 값들을 모아 튜플로 만듦

first = list()
second = list()
for i in range(n):
    for j in range(n):
        first.append(a[i] + b[j])
        second.append(c[i] + d[j])

ans = 0
counter = Counter(second)
# for tpl in Counter(first).items(): # 추가 비용이 됨
#    ans += counter[-tpl[0]] * tpl[1] # 중복되는 수가 많지 않아 효과가 적은 듯
for num in first:
    ans += counter[-num]
print(ans)
""" 파이썬은 이진 탐색보다 counter가 더 빠른 듯
ans = 0
second.sort()
for num in first:
    ans += bisect_right(second, -num) - bisect_left(second, -num)
print(ans)
"""
