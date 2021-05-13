# https://www.acmicpc.net/problem/1915
""" DP 문제는 점화식 정의 방법이 가장 중요하다
1. 최종 답을 구하기 쉬운 점화식
2. 이전 단계의 답으로 이뤄지는 점화식
"""
import sys

n, m = map(int, input().split())
n, m = n + 1, m + 1
arr = ['0' * m]
for _ in range(n - 1):
    arr.append('0' + sys.stdin.readline().rstrip())

# d[i][j]: i,j를 끝으로, 가능한 정사각형의 길이
d = [[0] * m for _ in range(n)]
ans = 0
for i in range(1, n):
    for j in range(1, m):
        # 끝 점에서 (가로, 세로, 대각선) 중 최소 길이를 구하자.
        if arr[i][j] == '1':
            d[i][j] = min(d[i - 1][j - 1], d[i][j - 1], d[i - 1][j]) + 1
        if ans < d[i][j]:
            ans = d[i][j]

print(ans ** 2)
