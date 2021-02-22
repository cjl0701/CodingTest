# N개의 자연수 중 M개 고른 수열 (오름차순)
import sys
from itertools import combinations

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
# 오름차순-> 순서 정해짐 -> 조합
for c in combinations(data, m): # c:tuple
    sys.stdout.write(' '.join(map(str, c)) + "\n")

# arr = [0] * m
#
#
# # 재귀 설계
# # 탈출, 성공: idx==m
# # 연산: 하나씩 선택해봄
# # 반환: x, 성공시 출력
# def func(idx, start, n, m):
#     if idx == m:
#         sys.stdout.write(' '.join(map(str, arr))+"\n")
#         return
#     for i in range(start, n):
#         arr[idx] = data[i]
#         func(idx + 1, i + 1, n, m)
#
#
# func(0, 0, n, m)
