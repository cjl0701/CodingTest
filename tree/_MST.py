# 최소 스패닝 트리 https://www.acmicpc.net/problem/1197
# kruskal


# 대표 찾아 반환
def find_parent(parent, x):
    if x != parent[x]:  # 대표는 자신 = 부모
        parent[x] = find_parent(parent, parent[x])  # 거슬러 올라가 찾음, 경로압축
    return parent[x]  # 대표를 가리킴


# 대표 번호가 작은 쪽 밑으로 들어감
def union_parent(parent, v1, v2):
    p1, p2 = parent[v1], parent[v2]
    if p1 < p2:
        parent[p2] = p1  # parent[p2]==p2 -> p1
    else:
        parent[p1] = p2


v, e = map(int, input().split())
edges = []
for _ in range(e):
    v1, v2, cost = map(int, input().split())
    edges.append((cost, v1, v2))

# 사이클을 생성하지 않는 최소 간선 v-1개 선택하면 됨 (사이클 형성하면 최소 비용 아님)
edges.sort()
result = 0
parent = [i for i in range(v + 1)]

for cost, v1, v2 in edges:
    # 서로소 집합이면(소속이 다르면), 사이클 형성 x
    if find_parent(parent, v1) != find_parent(parent, v2):
        result += cost
        union_parent(parent, v1, v2)

print(result)
