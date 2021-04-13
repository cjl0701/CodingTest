# 모든 점 ~ 모든 점까지의 최단 거리를 2차원 배열에 기록. O(N^3)
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정
# 노드의 개수 및 간선의 갯수 입력 받기
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고, 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]  # 플로이드 워셜은 인접 행렬에 기록
for v in range(1, n + 1):
    graph[v][v] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c  # a->b 가는 비용 c

""" 점화식에 따라 플로이드 워셜 알고리즘을 수행
    D[a][b]=min(D[a][b], D[a][k]+D[k][b]) """
for k in range(1, n + 1):  # 경유 정점
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("Not Reachable", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
