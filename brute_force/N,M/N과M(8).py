# N개 중 M개 고른 수열 (중복 허용, 비 내림차순)
import sys
from itertools import combinations_with_replacement

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()  # 문자열 정렬은 '100' <'20'
# (중복 허용, 비 내림차순) => 중복 조합
for c in combinations_with_replacement(num, m):
    sys.stdout.write(' '.join(map(str, c)) + "\n")
# arr = [0] * m
#
# 재귀 설계
# 성공, 탈출: idx==m
# 연산: idx 선택
# 반환: x, 성공마다 출력
# def func(idx, start, n, m):
#     if idx == m:
#         sys.stdout.write(' '.join(map(str, arr)) + '\n')
#         return
#     for i in range(start, n):
#         arr[idx] = num[i]
#         func(idx + 1, i, n, m)
#
#
# func(0, 0, n, m)
# cnt = [0] * n
#
#
# def func2(idx, selected, n, m):
#     if selected == m:  # 성공
#         for i in range(n):
#             for _ in range(cnt[i]):
#                 sys.stdout.write(str(num[i]) + " ")
#         sys.stdout.write("\n")
#         return
#     if idx == n:  # 탈출
#         return
#
#     for i in range(m - selected, -1, -1):
#         cnt[idx] = i
#         func2(idx + 1, selected + i, n, m)
#
# func2(0,0,n,m)
