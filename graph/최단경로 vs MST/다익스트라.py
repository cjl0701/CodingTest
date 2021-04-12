# 최단 경로: 두 정점 간에 최단 경로
# 다익스트라: '출발점'에서 각 점까지 최단 경로. (in 방향 그래프)
"""
원리: 최단 경로는 최단 경로로 이뤄진다 -> 갱신
가까운 것에서부터 최단 경로를 찾아가며 갱신 -> 갱신되면 이후 노드도 갱신할 수 있다.
"""
import heapq

n = 3
edges = [(0, 0, 0)]
graph = [[] for _ in range(n + 1)]
for frm, to, cost in edges:
    graph[frm].append((to, cost))
    # graph[to].append((frm, cost)) 다익스트라는 방향 그래프 알고리즘.

# 최단 거리 테이블
INF = 1e9
d = [INF] * (n + 1)
start = 1


# 출발점에서 각 점까지 최단 거리들을 기록
def 다익스트라(start):
    d[start] = 0

    # 최소 힙에 갱신된 노드 -> 이후 노드도 갱신한다.
    h = []
    heapq.heappush(h, (d[start], start))
    while h:
        # 갱신된 노드 중 최단 경로
        dist, now = heapq.heappop(h)  # dist: now 까지 경로 길이. 예전에 넣어둔 게 나올 수도.
        if d[now] < dist:  # 예전에 넣은 것은 최소가 아니다. 이 dist로 갱신 x
            continue
        # now까지 최단 경로 dist를 가지고 이후 노드를 갱신해본다.
        for next in graph[now]:
            cost = dist + next[1]  # now를 거쳐 next[0]까지 거리
            if d[next[0]] > cost:
                d[next[0]] = cost
                # 갱신되었으면 next를 이용해 또 갱신해야 함 -> 힙에 넣는다.
                heapq.heappush(h, (cost, next[0]))


다익스트라(start)
# 확인
for i in range(1, n + 1):
    if d[i] == INF:
        print("UNREACHABLE")
    else:
        print(d[i])
