# https://www.acmicpc.net/problem/16197
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
coin = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 'o':
            coin.append((i, j))
            board[i][j] = '.'

"""중복이 많으니까 그냥 재귀로 풀자."""


def dfs(turn, coin1, coin2):
    if turn > 10:  # 실패
        return -1

    ans = -1
    for k in range(4):  # 이동
        drop = []
        next = []
        for x, y in (coin1, coin2):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == '.':
                    next.append((nx, ny))
                else:
                    next.append((x, y))
            else:
                drop.append(True)
        if len(drop) == 1:  # 성공
            return turn
        elif len(drop) == 2:  # 실패
            continue
        else:  # 계속 진행
            temp = dfs(turn + 1, next[0], next[1])
            if temp != -1:
                if ans == -1 or ans > temp:
                    ans = temp
    return ans


print(dfs(1, coin[0], coin[1]))
