# 노드와 간선(union 연산)의 개수 입력 받기
v, e = map(int, input().split())
# 부모(대표) 테이블 초기화
parent = [0] * (v + 1)
# 최초엔 자신의 부모는 자신이다.
for i in range(1, v + 1):
    parent[i] = i

cycle = False  # 사이클 발생 여부


def union_parent(parent, a, b):
    ap = find_parent(parent, a)
    bp = find_parent(parent, b)
    if ap < bp:
        parent[bp] = ap
    else:
        parent[ap] = bp


def find_parent(parent, x):
    if parent[x] != x:  # 대표 찾을때까지 거슬러 올라감
        parent[x] = find_parent(parent, parent[x])  # 경로 압축
    return parent[x]


for _ in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 합집합 연산 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클 발생")
else:
    print("사이클 발생 x")

"""
3 3
1 2
2 3
1 3
"""
"""
6 4
1 4
2 3
2 4
5 6
"""