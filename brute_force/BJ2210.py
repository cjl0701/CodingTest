# 숫자판 점프
# 문자열을 구하는 게 아니라 갯수만 알면 되므로, 숫자를 넣어도 된다.
dx = (0, 0, 1, -1)
dy = (-1, 1, 0, 0)
a = [list(map(int, input().split())) for _ in range(5)]
s = set()


def go(cnt, x, y, num):
    if cnt == 5:
        s.add(num)
        return
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < 5 and 0 <= ny < 5:
            go(cnt + 1, nx, ny, num * 10 + a[nx][ny])


for x in range(5):
    for y in range(5):
        go(0, x, y, a[x][y])

print(len(s))
