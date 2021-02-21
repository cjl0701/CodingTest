# N개의 자연수 중에서 M개를 고른 수열 (중복 허용x)
import sys
from itertools import permutations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for p in permutations(arr,m):
    sys.stdout.write(' '.join(map(str, p)) + "\n")

# ans = [0] * m
# check = [False] * (len(arr))
#
#
# def func(idx, n, m):
#     if idx == m:
#         sys.stdout.write(' '.join(map(str, ans)) + "\n")
#         return
#
#     for i in range(len(arr)):
#         if check[i]: continue
#         check[i] = True
#         ans[idx] = arr[i]
#         func(idx + 1, n, m)
#         check[i] = False
#
#
# func(0, n, m)
