# 1~N까지 자연수 중에서 중복 없이 M개를 고른 수열 (오름차순)
import sys
from itertools import combinations

n, m = map(int, input().split())
# 오름차순 -> 순서 정해짐 -> 순서 없는 조합!
arr = list(range(1, n + 1))
for c in combinations(arr, m):
    sys.stdout.write(' '.join(map(str, c)) + "\n")
# arr = [0] * m
# check = [False] * (n + 1)
#
#
# def func(idx, start, n, m):
#     if idx == m:
#         sys.stdout.write(' '.join(map(str, arr)) + "\n")
#         return
#
#     for i in range(start, n + 1):
#         if check[i]:
#             continue
#         check[i] = True
#         arr[idx] = i
#         func(idx + 1, i + 1, n, m)
#         check[i] = False
#
#
# func(0, 1, n, m)
