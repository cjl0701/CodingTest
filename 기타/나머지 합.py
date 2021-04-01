# BJ 10986
import sys

# n, m = map(int, sys.stdin.readline().split())
# a = [x % m for x in map(int, sys.stdin.readline().split())]
# cnt = [0] * m  # 누적 cnt
# cnt[0] = 1  # s[0]=0으로 비워둔다
# sum = 0
# for i in range(n):
#     sum = (sum + a[i]) % m
#     cnt[sum] += 1
# ans = 0
# for i in range(m):
#     ans += cnt[i] * (cnt[i] - 1) // 2  # 등차수열 합 공식
# print(ans)

n, m = map(int, sys.stdin.readline().split())
s = [0]  # 누적합은 첫 칸을 비운다
for x in map(int, sys.stdin.readline().split()):
    s.append((x + s[-1]) % m)

# 시간 초과 O(N^2) => 선형 탐색으로 바꿔보자 => 누적 카운트
# for i in range(1, n + 1):
#     for j in range(i, n + 1):
#         if (s[i] - s[j - 1]) % m == 0:
#             ans += 1
""" 원리
(s[i] - s[j - 1]) % m == 0
=> s[i]%m == s[j-1]%m  나눠서 넣었으므로
   s[i] == s[j-1]인 i,j를 찾으면 된다.
"""
ans = 0
cnt = [0] * m
for i in range(n + 1):
    ans += cnt[s[i]]  # i번째 일때 나머지가 s[i]인 것의 갯수
    cnt[s[i]] += 1  # 나머지 갯수 누적
print(ans)
