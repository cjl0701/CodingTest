""" union find: 서로소 집합 자료구조
    서로소 부분 집합들을 합치고, 같은 집합에 속하는지 찾는데 사용
    서로소 집합: 공통 원소가 없는 두 집합
    대표(부모)가 곧 소속을 나타낸다!"""


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

# union 연산을 각각 수행
for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
for i in range(1, v + 1):
    print(i, find_parent(parent, i))

# 부모 테이블의 내용 출력
print(parent)

"""
6 4
1 4
2 3
2 4
5 6
"""
