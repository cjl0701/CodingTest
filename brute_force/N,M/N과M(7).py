# N개 중 M개 고른 수열(중복 가능, 증가하는 순서로 출력 -> 정렬)
import sys
from itertools import product

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

for p in product(data, repeat=m):
    sys.stdout.write(' '.join(map(str, p)) + "\n")
# arr = [0] * m
#
#
# def func(idx, n, m):
#     if idx == m:
#         sys.stdout.write(' '.join(map(str, arr)) + "\n")
#         return
#     for i in range(n):
#         arr[idx] = data[i]
#         func(idx + 1, n, m)
#
#
# func(0, n, m)
