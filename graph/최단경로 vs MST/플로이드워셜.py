n = 4
edges = [[1, 2, 3]]

# 최단 거리 테이블
INF = 1e9
dist = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dist[i][i] = 0
for frm, to, cost in edges:
    dist[frm][to] = cost  # 방향 그래프

# 플로이드 워셜
for k in range(1, n + 1):  # d[i][j]를 먼저 바꿔야 선한 영향력을 전파할 수 있다
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # for k in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            # 결국 dist[i][j]는 n번 호출된다!
