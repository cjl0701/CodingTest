# 1부터 n까지의 자연수 중 중복없이 m개 고른 수열
# 재귀 함수로 하나하나 선택 or 순열 api

import sys
from itertools import combinations, permutations

n, m = map(int, input().split())
arr = list(range(1, n + 1))
for tp in permutations(arr,m):
    sys.stdout.write(' '.join(map(str,tp))+"\n")
"""
check = [False] * (n + 1)
arr = [0] * m


def func(idx, n, m):
    if idx == m:
        sys.stdout.write(' '.join(map(str, arr)) + '\n')
        return
    for i in range(1, n + 1):
        if check[i]:
            continue
        check[i] = True
        arr[idx] = i
        func(idx + 1, n, m)
        check[i] = False


func(0, n, m)
"""
