""" 위상 정렬: 선행 조건을 따라 정렬.
    진입 차수가 0이라면, 더 이상 선행조건이 없는 것이다! """
# 노드의 개수와 간선의 개수를 입력 받기
from collections import deque

v, e = map(int, input().split())
# 모든 노드에 대한 집입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # 정점 A에서 B로 이동 가능
    indegree[b] += 1


# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()
    # 처음 시작할 때는 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입 차수에서 1 빼기
        for vertex in graph[now]:
            indegree[vertex] -= 1
            # 새롭게 진입 차수가 0이 되는 노드를 큐에 삽입
            if indegree[vertex] == 0:
                q.append(vertex)

    print(result)

"""
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
"""
topology_sort()