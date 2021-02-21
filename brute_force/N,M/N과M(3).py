# 1~N 자연수 중 M개 고른 수열(중복 허용)
import sys
from itertools import product

n, m = map(int, input().split())
arr = list(range(1, n + 1))
for p in product(arr, repeat=m):
    sys.stdout.write(' '.join(map(str, p)) + "\n")

# arr = [0] * m
# def func(idx, n, m):
#     if idx == m:
#         sys.stdout.write(' '.join(map(str, arr)) + "\n")
#         return
#     for i in range(1, n + 1):
#         arr[idx] = i
#         func(idx + 1, n, m)
#
#
# func(0, n, m)
