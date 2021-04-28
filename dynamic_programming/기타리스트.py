# https://www.acmicpc.net/problem/1495
# 이차 확산표 => 1의 확산
n, s, m = map(int, input().split())
v = list(map(int, input().split()))
check = [[False] * (m + 1) for _ in range(n + 1)]
check[0][s] = True
for i in range(n):
    for j in range(m + 1):
        if check[i][j]:
            if j - v[i] >= 0:
                check[i + 1][j - v[i]] = True
            if j + v[i] <= m:
                check[i + 1][j + v[i]] = True

for vol in range(m, -1, -1):
    if check[n][vol]:
        print(vol)
        break
else:
    print(-1)
