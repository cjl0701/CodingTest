# https://www.acmicpc.net/problem/14225
# def go(idx, s):
#     if idx == n:
#         check[s] = True
#         return
#     go(idx + 1, s + a[idx])  # 선택
#     go(idx + 1, s)  # 선택 x


LIMIT = 100000 * 20 + 1
n = int(input())
a = list(map(int, input().split()))
check = [False] * LIMIT

# go(0, 0)
""" 비트마스크 버전 """
for bm in range(1 << n):  # 0000..~1111..(n자리)
    sum = 0
    for i in range(n):
        if bm & (1 << i) != 0:
            sum += a[i]
    check[sum] = True
for x in range(1, LIMIT + 1):
    if not check[x]:
        print(x)
        break
