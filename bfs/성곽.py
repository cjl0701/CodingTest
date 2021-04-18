"""벽 하나 부수기 => 완전 탐색으로 하나하나 부숴본다"""
# bfs 기록해둔 것 활용하기 위해, 영역 번호와 넓이 기록
from collections import deque


def bfs(i, j, sect, sect_no):
    # check = [[False] * m for _ in range(n)] 있는 정보 활용해
    sect[i][j] = sect_no  # 영역 번호 새기기
    q = deque()
    q.append((i, j))
    space = 0

    while q:
        x, y = q.popleft()
        space += 1  # 넓이 측정
        # 4 방향으로 이동
        for k in range(4):
            # 이동하려는 방향에 벽이 있으면 불가
            if a[x][y] & (1 << k) > 0:
                continue
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and sect[nx][ny] == -1:
                sect[nx][ny] = sect_no  # 영역 번호 새기기
                q.append((nx, ny))
    return space


dx = (0, -1, 0, 1)  # 동북서남
dy = (-1, 0, 1, 0)

m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
sect = [[-1] * m for _ in range(n)]
sect_no = -1  # 0부터 센다
area = []

for x in range(n):
    for y in range(m):
        if sect[x][y] == -1:
            sect_no += 1
            area.append(bfs(x, y, sect, sect_no))

print(sect_no + 1)
ans = max(area)
print(ans)

# 벽을 하나씩 부숴 두 영역을 합친다.
for x in range(n):
    for y in range(m):
        for k in range(4):
            # 벽이 있으면 벽 너머의 두 영역을 합친다.
            if a[x][y] & (1 << k) > 0:
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if sect[x][y] != sect[nx][ny]:
                        ans = max(ans, area[sect[x][y]] + area[sect[nx][ny]])
print(ans)
