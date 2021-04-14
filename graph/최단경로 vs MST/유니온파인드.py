"""
경로 압축
before: 5->4->3->2->1-1 끝
after: 5->1-1 끝(경로압축)
"""


def find_parent(parent_table, e):
    # 대표를 찾아 거슬러 올라간다.
    if e != parent_table[e]:
        parent_table[e] = find_parent(parent_table, parent_table[e])  # 부모 테이블을 대표 테이블로
    return parent_table[e]


def union_parent(parent_table, a, b):
    s1, s2 = find_parent(parent_table, a), find_parent(parent_table, b)
    if s1 < s2:  # 대표의 번호가 작은 쪽에 맞추는 게 관례
        parent_table[b] = s1
    else:
        parent_table[a] = s2


parent_table = [i for i in range(5)]
union_parent(parent_table, 1, 4)
union_parent(parent_table, 3, 2)
union_parent(parent_table, 2, 4)
print("원소 - 소속")
# 1:1,4,2,3
for i in range(1, 5):
    print(f"{i} - {find_parent(parent_table, i)}")
