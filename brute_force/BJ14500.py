# 테트로미노
# 1. 가능한 경우의 수부터 따져봤어야 했다.
# 2. 테트로미노를 분석해서 규칙을 찾아야 했다.


def go(x, y, cnt, s):
    if cnt == 4:
        global ans
        ans = max(ans, s)
        return
    if not (0 <= x < len(a) and 0 <= y < len(a[0])):
        return
    if check[x][y]:
        return
    check[x][y] = True
    for k in range(4):
        go(x + dx[k], y + dy[k], cnt + 1, s + a[x][y])
    check[x][y] = False


dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
check = [[False] * m for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        go(i, j, 0, 0)
        # 예외처리 - 그냥 하지말고 머리를 쓰자..
        if j + 2 < m:
            common = a[i][j] + a[i][j + 1] + a[i][j + 2]
            if i - 1 >= 0:
                ans = max(ans, common + a[i - 1][j + 1])
            if i + 1 < n:
                ans = max(ans, common + a[i + 1][j + 1])
        if i + 2 < n:
            common = a[i][j] + a[i + 1][j] + a[i + 2][j]
            if j - 1 >= 0:
                ans = max(ans, common + a[i + 1][j - 1])
            if j + 1 < m:
                ans = max(ans, common + a[i + 1][j + 1])
print(ans)
""" 이 짓거리 하고 있으면 이미 틀린 것이다.. 오타 찾느라 정신병 걸림
tetromino = [
    ((0, 0), (0, 1), (0, 2), (0, 3)),  # ㅡ
    ((0, 0), (1, 0), (2, 0), (3, 0)),  # ㅣ
    ((0, 0), (0, 1), (1, 0), (1, 1)),  # ㅁ
    ((2, 0), (2, 1), (1, 1), (0, 1)),  # L
    ((0, 0), (1, 0), (2, 0), (2, 1)),
    ((0, 0), (0, 1), (0, 2), (1, 0)),
    ((0, 0), (0, 1), (1, 1), (1, 2)),
    ((1, 0), (1, 1), (1, 2), (0, 2)),
    ((1, 0), (2, 0), (1, 1), (0, 1)),  # ㄹ
    ((0, 0), (1, 0), (1, 1), (2, 1)),
    ((0, 1), (0, 2), (1, 0), (1, 1)),
    ((0, 0), (0, 1), (0, 2), (1, 1)),  # ㅜ
    ((1, 0), (1, 1), (0, 1), (2, 1)),
    ((1, 0), (1, 1), (1, 2), (0, 1)),
    ((0, 0), (1, 0), (2, 0), (1, 1)),
]

n, m = map(int, input().split())
arr = [[0, 0, 0] + list(map(int, input().split())) + [0, 0, 0] for _ in range(n)]
n += 6
m += 6
arr = [[0] * m] * 3 + arr + [[0] * m] * 3
ans = 0
# 모든 칸에 놓아본다.
for i in range(0, n):
    for j in range(0, m):
        for t in tetromino:  # 각 테트로미노에 대하여
            cur = 0
            for p in t:  # 테트로미노의 각 조각을 따져본다.
                x, y = i + p[0], j + p[1]
                if 0 <= x < n and 0 <= y < m:
                    cur += arr[x][y]
            ans = max(ans, cur)

print(ans)
"""
