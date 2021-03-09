# 드래곤 커브
dx = (0, -1, 0, 1)
dy = (1, 0, -1, 0)

arr = [[False] * 101 for _ in range(101)]
n = int(input())


# 드래곤 커브를 그린다.
def curve(d):
    dirs = [d]  # 0세대
    for _ in range(1, g + 1):
        for dir in dirs[::-1]:
            dirs.append((dir + 1) % 4)
    return dirs


for _ in range(n):
    y, x, d, g = map(int, input().split())
    dirs = curve(d)
    arr[x][y] = True
    for dir in dirs:
        x, y = x + dx[dir], y + dy[dir]
        arr[x][y] = True

# 한 칸씩 전부 검사
ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i + 1][j] and arr[i][j + 1] and arr[i + 1][j + 1]:
            ans += 1
print(ans)
