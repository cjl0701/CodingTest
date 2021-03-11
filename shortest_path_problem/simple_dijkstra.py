"""O(V^2)이므로 노드 개수가 5000개 이하라면 활용 가능.
10000이상 이라면 우선순위 큐를 활용해 업그레이드 시켜야 함"""
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드, 간선의 개수 입력받기
n, m = map(int, input().split())
start = int(input())
# 각 노드에 연결되어 있는 노드들을 표현할 인접리스트
graph = [[] for i in range(n + 1)]
# 방문한 적이 있는지 체크하는 리스트
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # a번 노드에서 b번 노드로 가는 비용이 c


# 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환
def get_shortest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if min_value > distance[i] and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0  # 시작 노드에 대해서 초기화
    for _ in range(n):
        now = get_shortest_node()  # 가장 짧은 지점을 선택
        visited[now] = True  # 방문 처리. fix
        for next in graph[now]:  # 최단 거리 갱신
            if distance[next[0]] > distance[now] + next[1]:
                distance[next[0]] = distance[now] + next[1]


dijkstra(start)

# 모든 노드로의 최단 거리 출력
for i in range(1, n + 1):
    if distance[i] == INF:
        print("UNREACHABLE")
    else:
        print(distance[i])
