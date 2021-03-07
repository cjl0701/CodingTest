# 뮤탈리스크
from itertools import permutations

n = int(input())
scv = list(map(int, input().split()))
while len(scv) < 3:  # 편의를 위해 무조건 3개로
    scv.append(0)
d = [[[-1] * 61 for _ in range(61)] for _ in range(61)]  # d[a][b][c]: 체력이 a,b,c일 때 최소 공격 횟수


def f(a, b, c):
    if a < 0: a = 0  # 특별 조건
    if b < 0: b = 0
    if c < 0: c = 0
    if a + b + c == 0:  # 목표
        return 0
    if d[a][b][c] == -1:  # 메모
        ans = 61
        for attack in permutations([9, 3, 1], 3):
            ans = min(ans, f(a - attack[0], b - attack[1], c - attack[2]))
        d[a][b][c] = ans + 1
    return d[a][b][c]


print(f(*scv))

""" bfs 버전
from collections import deque

attack = ((9, 3, 1), (9, 1, 3), (3, 1, 9), (3, 9, 1), (1, 3, 9), (1, 9, 3))
n = int(input())
scv = [0, 0, 0]
for i, x in enumerate(map(int, input().split())):
    scv[i] = x
LIMIT = 61
dist = [[[-1] * LIMIT for _ in range(LIMIT)] for _ in range(LIMIT)]  # d[s1][s2][s3]
dist[scv[0]][scv[1]][scv[2]] = 0
q = deque()
q.append(tuple(scv))
while q:
    x, y, z = q.popleft()
    for d in attack:
        nx, ny, nz = map(lambda x: x if x >= 0 else 0, [x - d[0], y - d[1], z - d[2]])
        if dist[nx][ny][nz] != -1:
            continue
        dist[nx][ny][nz] = dist[x][y][z] + 1
        q.append((nx, ny, nz))
print(dist[0][0][0])
"""
