# https://www.acmicpc.net/problem/10986
import sys

n, m = map(int, input().split())
s = [0]  # 구간합은 빼기 편의를 위해 첫칸을 비운다. s[i~j]=s[i]-s[j-1]이므로
for num in map(int, sys.stdin.readline().split()):
    s.append((s[-1] + num) % m)

answer = 0
cnt = [0] * m  # s[i]의 범위
cnt[0] = 1  # j는 1부터지만 실제 구하는 건 j-1부터니까.
for i in range(1, n + 1):  # i는 1부터
    answer += cnt[s[i]]
    cnt[s[i]] += 1  # 하나하나 갯수를 기록해가며 진행

print(answer)
""" 원리
(s[i] - s[j - 1]) % m == 0
=> s[i]%m == s[j-1]%m  나눠서 넣었으므로
   s[i] == s[j-1]인 i,j를 찾으면 된다.
"""
