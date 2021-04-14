# 노드와 간선(union 연산)의 개수 입력 받기
v, e = map(int, input().split())
# 부모(대표) 테이블 초기화
parent = [i for i in range(v + 1)]  # 최초엔 자신의 부모는 자신
cycle = False  # 사이클 발생 여부


def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    pa, pb = find_parent(parent, a), find_parent(parent, b)
    if pa < pb:
        parent[pb] = pa  # 대표를 갱신해야
    else:
        parent[pa] = pb


for _ in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):  # 같은 소속이라면 사이클
        cycle = True
        break
    # 사이클이 발생하지 않았다면 합집합 연산 수행
    else:
        union_parent(parent, a, b)

print(cycle)

"""
3 3
1 2
2 3
1 3
"""
