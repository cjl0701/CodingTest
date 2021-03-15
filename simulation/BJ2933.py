# 미네랄
# 간단하게, 그냥 매번 모든 연결요소를 하나씩 내린다.
import sys

sys.setrecursionlimit(100 * 100)
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)


def dfs(x, y, group, check):
    if a[x][y] == '.' or check[x][y]:
        return
    check[x][y] = True
    group.append((x, y))
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < r and 0 <= ny < c:
            dfs(nx, ny, group, check)


# 모든 연결 요소를 내린다. (사실은 최대 한 개의 연결요소만 내려가지만)
def simulate():
    check = [[False] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if a[x][y] == '.':
                continue
            if check[x][y]:  # 손 댄건 또 건드리지 않는다.
                continue
            group = []
            dfs(x, y, group, check) # dfs의 결과를 group에 넣으면 또 찾지 않아도 된다!
            # 블록의 행마다 가장 낮은 높이를 기록
            low = [-1] * c
            for gx, gy in group:
                low[gy] = max(low[gy], gx)
                a[gx][gy] = '.'  # 어차피 옮기니까
            # 최소 갭을 구한다.
            gap = r
            for j in range(c):
                if low[j] == -1:  # 변화 없는 열
                    continue
                i = low[j]
                while i < r and a[i][j] == '.':
                    i += 1
                gap = min(gap, i - low[j] - 1)
            # 최소 갭 만큼 내린다.
            for gx, gy in group:
                a[gx + gap][gy] = 'x'
                check[gx + gap][gy] = True


r, c = map(int, input().split())
a = [list(input()) for _ in range(r)]
n = int(input())
heights = list(map(int, input().split()))  # h = r-idx
# 막대기를 던진다
for k, i in enumerate(heights):
    i = r - i  # n-i라고 잘못 썼다... 변수명 길더라도 헷갈리지 않는 것으로
    # 부순다
    if k % 2 == 0:
        for j in range(c):
            if a[i][j] == 'x':
                a[i][j] = '.'
                break
    else:
        for j in range(c - 1, -1, -1):
            if a[i][j] == 'x':
                a[i][j] = '.'
                break
    # 단순하게 매번 부순 후 내린다.
    simulate()
for row in a:
    print(''.join(row))
"""
# dfs로 쭉 가서 바닥(r-1)과 연결되면 됨
def check_cluster(x, y):
    check[x][y] = True
    if x == r - 1:
        return True
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < r and 0 <= ny < c and a[nx][ny] == 'x' and not check[nx][ny]:
            if check_cluster(nx, ny):
                return True
    return False


def drop():
    # 범위
    left, right = c - 1, 0
    for i in range(r):
        for j in range(c):
            if check[i][j]:
                if j < left:
                    left = j
                if j > right:
                    right = j
    # 차이
    diff = r
    for j in range(left, right + 1):
        for i in range(r - 1, -1, -1):
            if check[i][j]:
                ni = i + 1
                while ni < r and a[ni][j] == '.':
                    ni += 1
                diff = min(diff, ni - i - 1)
                break
    # 그린다
    for j in range(left, right + 1):
        for i in range(r - 1, -1, -1):
            if check[i][j]:
                a[i][j] = '.'
                a[i + diff][j] = 'x'
"""
