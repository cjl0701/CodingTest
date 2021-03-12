# 플로이드
import sys

INF = int(1e9)
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0
for _ in range(m):
    a, b, c, = map(int, sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] >= INF:
            sys.stdout.write("0 ")
        else:
            sys.stdout.write(str(graph[a][b]) + " ")
    sys.stdout.write("\n")
