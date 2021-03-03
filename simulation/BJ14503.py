# 로봇 청소기
steps = ((0, -1), (-1, 0), (0, 1), (1, 0))  # 북,동,남,서 -> 왼쪽 회전 후 진행 좌표
back = ((1, 0), (0, -1), (-1, 0), (0, 1))
n, m = map(int, input().split())
r, c, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
while True:
    # 현 위치 청소
    if a[r][c] == 0:
        a[r][c] = 2
    # 왼쪽부터 탐색 진행
    for k in range(4):
        # 왼쪽 회전 후 전진
        nr, nc = r + steps[d][0], c + steps[d][1]
        d = d - 1 if d != 0 else 3
        if not (0 <= nr < n and 0 <= nc < m):
            continue
        # 회전한 방향 앞에 청소하지 않은 공간이 있다면
        if a[nr][nc] == 0:
            r, c = nr, nc
            break
        # 청소할 공간이 없다면 계속 회전
    else:
        # 후진할 수 있다면 후진
        nr, nc = r + back[d][0], c + back[d][1]
        if 0 <= nr < n and 0 <= nc < m and a[nr][nc] != 1:
            r, c = nr, nc
        else:
            break
cnt = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 2:
            cnt += 1
print(cnt)
