# https://www.acmicpc.net/problem/3085
def count_row(i):
    maximum = cnt = 1
    for j in range(n - 1):
        if a[i][j] == a[i][j + 1]:
            cnt += 1
        else:
            maximum = max(maximum, cnt)
            cnt = 1
    maximum = max(maximum, cnt)  # 이거 빼먹어서 틀림
    return maximum


def count_col(j):
    maximum = cnt = 1
    for i in range(n - 1):
        if a[i][j] == a[i + 1][j]:
            cnt += 1
        else:
            maximum = max(maximum, cnt)
            cnt = 1
    maximum = max(maximum, cnt)
    return maximum


dx = (0, 1) # 2 방향만 고려하면 된다!(jump)
dy = (1, 0)
n = int(input())
a = [list(input()) for _ in range(n)]
answer = 0
for i in range(n):
    answer = max(answer, count_row(i))
for j in range(n):
    answer = max(answer, count_col(j))

for i in range(n):
    for j in range(n):
        for k in range(2):
            ni, nj = i + dx[k], j + dy[k]
            if not (ni < n and nj < n) or a[i][j] == a[ni][nj]:
                continue
            a[i][j], a[ni][nj] = a[ni][nj], a[i][j]
            for x in (i, ni):
                answer = max(answer, count_row(x))
            for y in (j, nj):
                answer = max(answer, count_col(y))
            a[i][j], a[ni][nj] = a[ni][nj], a[i][j]

print(answer)
