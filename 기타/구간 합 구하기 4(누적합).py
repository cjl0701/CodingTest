# BJ 11659 : 수 n개가 주어졌을 때 i번째~j번째 수까지 합
""" 누적합 => 메모. 중복 계산을 피한다.
    편의를 위해 s[0] 비워두기! """
# S[i] = A[1]+A[2]+...+A[i] / S[i] = S[i-1]+A[i]
import sys

n, m = map(int, sys.stdin.readline().split())
a = [0] + list(map(int, sys.stdin.readline().split()))
s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = s[i - 1] + a[i]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(s[j] - s[i - 1]) + "\n")
