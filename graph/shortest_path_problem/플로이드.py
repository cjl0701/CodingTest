# https://www.acmicpc.net/problem/11404
# '모든 도시의 쌍' (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값
import sys

n = int(input())
m = int(input())
# 최단 거리 테이블: 인접 행렬에 비용 표시
INF = int(1e9)
d = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    d[i][i] = 0
for _ in range(m):
    frm, to, cost = map(int, sys.stdin.readline().split())
    d[frm][to] = min(d[frm][to], cost)  # 최소값으로 입력받지 않아 틀림

# 원리: k를 거쳐가는 게 더 빠르면 갱신한다
# 점화식: d[i][j]=min(d[i][j], d[i][k]+d[k][j])
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        sys.stdout.write(str(d[i][j] if d[i][j] != INF else 0) + " ")  # write는 개행 x
    sys.stdout.write("\n")
