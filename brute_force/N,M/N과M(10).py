# N개의 자연수 중 M개를 고른 수열 (비 내림차순, 중복x)
import sys
from itertools import combinations

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

for c in sorted(set(combinations(data, m))):
    sys.stdout.write(' '.join(map(str, c)) + "\n")
# s = set()
# arr = [0] * m
#
#
# def func(idx, start):
#     if idx == m:
#         s.add(tuple(arr))
#         return
#     for i in range(start, n):
#         arr[idx] = data[i]
#         func(idx + 1, i + 1)
#
#
# func(0, 0)
# for a in sorted(s):
#     sys.stdout.write(' '.join(map(str, a)) + "\n")
