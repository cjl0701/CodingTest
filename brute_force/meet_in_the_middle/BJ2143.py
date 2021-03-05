# 두 배열의 합
from bisect import bisect_right, bisect_left
from collections import Counter

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a_sum = list()
b_sum = list()
for i in range(n):
    s = 0
    for j in range(i, n):
        s += a[j]
        a_sum.append(s)

for i in range(m):
    s = 0
    for j in range(i, m):
        s += b[j]
        b_sum.append(s)
ans = 0
counter = Counter(b_sum)
for tpl in Counter(a_sum).items():
    ans += counter[t - tpl[0]] * tpl[1]
print(ans)
"""
# 이진 탐색으로 구간 => 갯수
ans = 0
b_sum.sort()
for num in a_sum:
    ans += bisect_right(b_sum, t - num) - bisect_left(b_sum, t - num)
print(ans)
"""
