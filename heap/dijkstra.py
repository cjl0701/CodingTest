# 우선순위 큐를 이용해 개선 O(ElogV)
import heapq

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드, 간선의 개수 입력받기
n, m = map(int, input().split())
start = int(input())
# 각 노드에 연결되어 있는 노드들을 표현할 인접리스트
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # a번 노드에서 b번 노드로 가는 비용이 c

# 작은 것부터 거쳐 최소를 만들어본다 
def dijkstra(start):
    h = []
    distance[start] = 0  # 시작 노드에 대해서 초기화
    heapq.heappush(h, (distance[start], start))  # tuple[0]을 기준으로 우선순위 결정
    while h:
        dist, now = heapq.heappop(h)  # 가장 짧은 지점을 선택
        if distance[now] < dist:  # 이전 경로가 더 짧다면 이것으로 갱신 x
            continue
        for next in graph[now]:  # now를 거쳐가는 게 더 최소면 최단 거리 갱신
            cost = dist + next[1]
            if distance[next[0]] > cost: # 갱신 했으면 힙에 넣는다
                distance[next[0]] = cost
                heapq.heappush(h, (cost, next[0]))


dijkstra(start)

# 모든 노드로의 최단 거리 출력
for i in range(1, n + 1):
    if distance[i] == INF:
        print("UNREACHABLE")
    else:
        print(distance[i])
