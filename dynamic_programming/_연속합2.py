# 연속합 2 https://www.acmicpc.net/problem/13398
n = int(input())  # n<=100000 -> n^2은 무리. 선형 탐색 => dp(메모)
arr = list(map(int, input().split()))
d = arr.copy()  # d[i]: i 포함 최대 연속합
dr = arr.copy()  # d를 오른쪽에서 부터 구하기.
for i in range(1, n):
    if d[i - 1] + arr[i] > d[i]:
        d[i] += d[i - 1]
# d[i]를 오른쪽 부터 구한 버전
for i in range(n - 2, -1, -1):
    if dr[i] < dr[i + 1] + arr[i]:
        dr[i] += dr[i + 1]

ans = max(d)
for i in range(1, n - 1):
    if ans < d[i - 1] + dr[i + 1]:
        ans = d[i - 1] + dr[i + 1]
print(ans)
""" 너무 어렵게 풀었다. dp 문제 => dp 기본 문제들로 나눌 수 있다. 2차원 배열 말고 1차원 2개써라.
d = [arr.copy()]  # d[i]: i 포함 최대 연속합. d[i][0]: i 포함 / d[i][1]: 하나 뺀 상태
d.append([0] * n)
for i in range(1, n):
    if d[0][i - 1] + arr[i] > d[0][i]:
        d[0][i] += d[0][i - 1]  # 연속으로 갱신
    d[1][i] = max(d[0][i - 1], d[1][i - 1] + arr[i])  # 새로 빼기 or 뺀 상태 연속
d[1][0] = -1000 * 100000  # d[1][0]이 예외. 하나 이상 포함해야 하므로.
print(max(max(d[0]), max(d[1])))
# print(d[0]) 답을 제출하기 전에 중간 답을 찍어 검증하자..
# print(d[1])
"""
