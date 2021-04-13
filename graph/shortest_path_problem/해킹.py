# 출발점 -> 각 점까지의 최단 경로 => 다익스트라
# 답: 최소 비용 테이블의 max
import heapq
import sys


# 최소 비용 테이블 갱신 -> 가까운 곳부터 멀리 퍼진다. 최소 비용부터 고려한다
# 최소 비용을 꺼낸다(힙) -> 최소 비용으로 갱신됐을 경우 힙에 넣는다.
def dijkstra(start):
    d[start] = 0
    h = []
    heapq.heappush(h, (d[start], start))
    while h:
        dist, now = heapq.heappop(h)  # dist: 누적 비용
        # 이제, now에서 dist를 가지고 갱신한다.
        if d[now] < dist:  # 이미 더 최소로 갱신 된 경우, 예전에 넣는 값이 뒤늦게 나온 경우
            continue
        for next, cost in graph[now]:
            next_dist = dist + cost  # now까지 비용+next로 가는 비용
            if d[next] > next_dist:
                d[next] = next_dist
                heapq.heappush(h, (next_dist, next))


INF = int(1e9 + 1)
t = int(input())
for _ in range(t):
    n, m, start = map(int, sys.stdin.readline().split())
    # 연결 관계를 표현할 인접리스트
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        to, frm, s = map(int, sys.stdin.readline().split())
        graph[frm].append((to, s))

    # 최소 비용 테이블에 출발점부터 각 정점까지의 최소 비용 기록
    d = [INF] * (n + 1)
    # 갱신
    dijkstra(start)

    com = time = 0
    for c in d:
        if c != INF:
            com += 1
            time = max(time, c)
    print(com, time)
