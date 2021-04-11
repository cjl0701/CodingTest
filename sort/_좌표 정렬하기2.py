# https://www.acmicpc.net/problem/11651
"""
from functools import cmp_to_key


def compare(p1, p2):
    if p1[1] == p2[1]:
        return p1[0] - p2[0]
    return p1[1] - p2[1]


n = int(input())
point = [tuple(map(int, input().split())) for _ in range(n)]
point.sort(key=cmp_to_key(compare))
for x, y in point:
    print(x, y)
"""

n = int(input())
point = [tuple(map(int, input().split())) for _ in range(n)]
point.sort(key=lambda t: (t[1], t[0]))
for x, y in point:
    print(x, y)
