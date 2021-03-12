# 감시 피하기
from itertools import combinations

dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)
n = int(input())
a = []
teachers = []
candidates = []
for i in range(n):
    a.append(input().split())
    for j in range(n):
        if a[i][j] == 'T':
            teachers.append((i, j))
        elif a[i][j] == 'X':
            candidates.append((i, j))


def simulate():
    for t in teachers:
        for k in range(4):
            x, y = t[0], t[1]
            while True:
                nx, ny = x + dx[k], y + dy[k]
                if not (0 <= nx < n and 0 <= ny < n) or a[nx][ny] == 'O':
                    break
                if a[nx][ny] == 'S':
                    return False
                x, y = nx, ny
    return True


find = False
# 조합으로 3가지 경우를 선택. (순서 중요x)
for obstacles in combinations(candidates, 3):
    # 3개 고른 위치에 장애물 설치
    for x, y in obstacles:
        a[x][y] = 'O'

    # 탐색
    if simulate():
        find = True
        break

    # 되돌리기
    for x, y in obstacles:
        a[x][y] = 'X'

if find:
    print("YES")
else:
    print("NO")

""" 재귀로 3가지 선택
def setting(wall, idx):
    if wall == 3:
        return simulate()
    for i in range(idx, len(candidates)):
        a[candidates[i][0]][candidates[i][1]] = 'O'
        if setting(wall + 1, i + 1):  # wall+1이 아니라 wall, i가 아니라 idx+1을 전달했다..
            return True
        a[candidates[i][0]][candidates[i][1]] = 'X'
    return False
"""
