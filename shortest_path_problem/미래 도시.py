# 시작점,도착점이 여러개 & 제한이 작음=> 플로이드 워셜
INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]  # 플로이드 워셜은 인접 행렬에 기록
for v in range(1, n + 1):
    graph[v][v] = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1  # 양방향
x, k = map(int, input().split())


# 1->k->x 비용 = graph[1][k]+graph[k][x]
# d[a][b]=min(d[a][b], d[a][k]+d[k][b]) k를 거려차는게 더 빠르면 갱신
def floyed_warshall():
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


floyed_warshall()
ans = graph[1][k] + graph[k][x]
print(ans if ans < INF else -1)

"""
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

3
"""
