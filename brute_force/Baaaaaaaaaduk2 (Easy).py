# https://www.acmicpc.net/problem/16988
""" 틀린이유
효율적으로 짜려다 일반적이지 못해 예외에서 걸림
예외를 잡으려면 => 로직을 코딩하기 전에 모든 케이스를 고려해야 하는데.. 
1. 적어도 그림, 예시는 살피자..
2. 극단적인 경우를 생각해본다.

+ 중간에 아니란걸 깨달아도 계속 진행해서 체크해야 한다.
"""
import sys
from collections import deque


def bfs(board):
    cnt = 0
    check = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == '2' and not check[i][j]:
                check[i][j] = True
                q = deque()
                q.append((i, j))
                cur = 0
                success = True
                while q:  # 틀린 이유: 중간에 아니란걸 깨달아도 계속 진행해서 체크해야 한다.
                    x, y = q.popleft()
                    cur += 1
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m:
                            if board[nx][ny] == '0':
                                success = False
                            elif board[nx][ny] == '2' and not check[nx][ny]:
                                check[nx][ny] = True
                                q.append((nx, ny))
                if success:
                    cnt += cur
    return cnt


dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)
n, m = map(int, input().split())
board = [sys.stdin.readline().split() for _ in range(n)]
ans = 0

for no1 in range(n * m):
    i1, j1 = no1 // m, no1 % m
    if board[i1][j1] != '0':
        continue
    board[i1][j1] = '1'
    for no2 in range(no1 + 1, n * m):
        i2, j2 = no2 // m, no2 % m
        if board[i2][j2] != '0':
            continue
        board[i2][j2] = '1'
        ans = max(ans, bfs(board))
        board[i2][j2] = '0'
    board[i1][j1] = '0'
print(ans)
