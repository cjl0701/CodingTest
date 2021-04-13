import heapq

n, m, c = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n + 1)]  # 다익스트라는 연결리스트
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))  # x->y 까지 z 시간 걸림
distance = [INF] * (n + 1)


# 특정 지점에서 다른 지점으로의 최단 경로 => 다익스트라
def dijkstra(start):
    h = []  # 가장 가까운 곳을 꺼내기 위한 최소 힙
    distance[start] = 0
    heapq.heappush(h, (0, start))  # 거리 기준 정렬
    while h:
        dist, now = heapq.heappop(h)  # 가장 가까운 곳을 꺼낸다.
        # 지금까지의 최단 경로를 이용해 최단 경로 갱신
        if distance[now] < dist:  # 더 긴 경로라면 보지 않는다. 이미 최단 경로를 확립했다.
            continue
        for next in graph[now]:
            cost = dist + next[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우, 갱신
            if distance[next[0]] > cost:
                distance[next[0]] = cost
                heapq.heappush(h, (cost, next[0]))


dijkstra(c)
count = max_distance = 0
for i in range(1, n + 1):
    if distance[i] not in (0, INF): # 시작 노드는 거리가 0이므로
        count += 1
        time = max(max_distance, distance[i])
print(count, max_distance)
"""
3 2 1
1 2 4
1 3 2

2 4
"""
