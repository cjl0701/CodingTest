# https://www.acmicpc.net/problem/9944
""" 틀린 이유
1. dfs 깊이가 최대 900인데 각 재귀마다 깊은 복사 4회씩.. 그냥 그렸다 지워라..
2. 끝에 도달해서 값 체크하는 것도 O(NM).. 그냥 매번 갯수 세면 된다..
"""

dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)


def go(x, y, left):
    # 끝에 도달하면 값 return
    if left == 0:
        return 0
    ans = -1
    # 이동 -> 그려본다
    for dir in range(4):
        # 이동할 수 있을 때까지 이동
        nx, ny = x + dx[dir], y + dy[dir]
        while 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == '.':
            arr[nx][ny] = '*'
            left -= 1
            nx, ny = nx + dx[dir], ny + dy[dir]
        nx, ny = nx - dx[dir], ny - dy[dir]

        # 이동했다면 dfs
        if x != nx or y != ny:
            temp = go(nx, ny, left)
            if temp != -1:
                if ans == -1 or ans > temp + 1:
                    ans = temp + 1

        # 그림 지운다
        while not (nx == x and ny == y):
            arr[nx][ny] = '.'
            left += 1
            nx, ny = nx - dx[dir], ny - dy[dir]

    # 받은 것 return
    return ans


tc = 1
while True:
    try:
        n, m = map(int, input().split())
    except:
        break
    arr = [list(input()) for _ in range(n)]
    room = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '.':
                room += 1

    ans = -1
    # 모든 점에서 dfs해본다
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '.':
                arr[i][j] = '*'
                temp = go(i, j, room - 1)
                arr[i][j] = '.'
                if temp != -1 and (ans == -1 or ans > temp):
                    ans = temp

    print(f"Case {tc}: {ans}")
    tc += 1
