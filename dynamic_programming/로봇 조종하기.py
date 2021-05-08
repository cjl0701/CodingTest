# https://www.acmicpc.net/problem/2169
# (i,j)까지 최대는 (i,j-1), (i-1,j), (i,j+1) 중 하나
# 근데 방향이 겹치면 안돼.. => 상태로 관리
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
INIT = -100 * 1000 * 1000  # 조건을 놓침
d = [[[INIT] * 3 for _ in range(m)] for _ in range(n)]
# 초기 세팅
d[0][0][0] = d[0][0][1] = a[0][0]  # 여유롭게 전부 세팅했어야.. 이런 사소한 조건때문에 예외에 걸린다고..
for j in range(1, m):
    d[0][j][1] = d[0][j - 1][1] + a[0][j]
# 0,1 방향 먼저. 2번 방향은 반대로 진행해야 해서
for i in range(1, n):
    d[i][0][0] = max(d[i - 1][0][0], d[i - 1][0][2]) + a[i][0]
    for j in range(1, m):
        d[i][j][0] = max(d[i - 1][j]) + a[i][j]
        d[i][j][1] = max(d[i][j - 1][0], d[i][j - 1][1]) + a[i][j]
    for j in range(m - 2, -1, -1):
        d[i][j][2] = max(d[i][j + 1][0], d[i][j + 1][2]) + a[i][j]
print(max(d[n - 1][m - 1]))
