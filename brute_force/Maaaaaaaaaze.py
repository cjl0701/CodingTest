# https://www.acmicpc.net/problem/16985
"""
순서를 만들어야 한다 => 재귀 or 중첩 for문 (or 라이브러리)
깊이가 정해져 있으면 굳이 재귀x
"""
from collections import deque
from itertools import permutations


def bfs(maze):
    if maze[0][0][0] == 0 or maze[n - 1][n - 1][n - 1] == 0:
        return -1
    dist = [[[-1] * n for _ in range(n)] for _ in range(n)]
    dist[0][0][0] = 0
    q = deque()
    q.append((0, 0, 0))
    while q:
        x, y, z = q.popleft()
        for k in range(6):
            nx, ny, nz = x + dx[k], y + dy[k], z + dz[k]
            if 0 <= nx < n and 0 <= ny < n and 0 <= nz < n:
                if maze[nx][ny][nz] == 1 and dist[nx][ny][nz] == -1:
                    dist[nx][ny][nz] = dist[x][y][z] + 1
                    q.append((nx, ny, nz))

    return dist[n - 1][n - 1][n - 1]


# 90도 회전 시키기
def clockwise(prev):
    board = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            board[j][n - 1 - i] = prev[i][j]
    return board


n = 5
dx = (0, 0, 0, 0, 1, -1)
dy = (0, 0, 1, -1, 0, 0)
dz = (1, -1, 0, 0, 0, 0)
floor = [[] for _ in range(n)]
for k in range(n):
    board = [list(map(int, input().split())) for _ in range(n)]
    floor[k].append(board)
    for prev in range(3):
        floor[k].append(clockwise(floor[k][prev]))

ans = -1
for order in permutations([0, 1, 2, 3, 4], n):
    maze = [[] for _ in range(n)]
    for dir1 in range(4):
        maze[0] = floor[order[0]][dir1]
        for dir2 in range(4):
            maze[1] = floor[order[1]][dir2]
            for dir3 in range(4):
                maze[2] = floor[order[2]][dir3]
                for dir4 in range(4):
                    maze[3] = floor[order[3]][dir4]
                    for dir5 in range(4):
                        maze[4] = floor[order[4]][dir5]
                        ret = bfs(maze)
                        if ret != -1:
                            if ans == -1 or ans > ret:
                                ans = ret
print(ans)
