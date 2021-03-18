""" 그리디: 싸이클이 발생하지 않는 작은 간선 부터 넣는다.
    같은 집합인지, 사이클을 형성하는지 파악하기 위해 union_find 활용
"""


# 특정한 원소가 속한 집합이 어떤 집합인지 알려준다.
def find_parent(parent, x):
    # 거슬러 올라가 대표를 찾는다.
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])  # 바로 대표를 가리키도록 갱신(경로 압축)
    return parent[x]


# 두 개의 원소가 포함된 집합을 하나의 집합으로 합친다.
def union_parent(parent, a, b):
    ap = find_parent(parent, a)
    bp = find_parent(parent, b)
    if ap < bp:  # 대표의 번호가 작은 쪽에 맞추는 게 관례
        parent[bp] = ap
    else:
        parent[ap] = bp


# 노드와 간선(union 연산)의 개수 입력 받기
v, e = map(int, input().split())
# 노드 개수 크기의 부모 테이블을 초기화. 부모 테이블을 거슬러 올라가면 대표가 나온다.
parent = [0] * (v + 1)
# 최초엔 자신의 부모는 자신이다.
for i in range(1, v + 1):
    parent[i] = i

edges = []  # 모든 간선을 담을 리스트
result = 0  # 최종 비용을 담을 변수

# 간선 정보 입력 받기
for _ in range(e):
    cost, a, b = map(int, input().split())
    # cost 순으로 정렬하기 위해, 튜플의 첫 원소를 cost로 설정.
    edges.append((cost, a, b))

# 간선을 비용 순으로 정렬
edges.sort()

# 간선을 하나씩 확인
for cost, a, b in edges:
    # 사이클을 형성하지 않으면 간선으로 채택
    if find_parent(parent, a) != find_parent(parent, b):
        result += cost
        union_parent(parent, a, b)
        print(cost)

print(result)

"""
7 9
29 1 2
75 1 5
35 2 3
34 2 6
7 3 4
23 4 6
13 4 7
53 5 6
25 6 7
"""
