# 적록색약
# 재귀 쓸 때 항상 sys.setrecursionlimit 셋팅
# 배열 2개 만들지 말고, valid 함수를 만들면 된다.
import sys

sys.setrecursionlimit(100 * 100)
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)


def can(cur, prev, blind):
    if prev == cur:
        return True
    if blind:
        if (prev == 'R' and cur == 'G') or (prev == 'G' and cur == 'R'):
            return True
    return False


def dfs(x, y, blind, check):
    check[x][y] = True
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if not check[nx][ny]:
                if can(a[nx][ny], a[x][y], blind):
                    dfs(nx, ny, blind, check)


# 중복되는 코드 => 함수화
def go(blind):
    ans = 0
    check = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not check[i][j]:
                dfs(i, j, blind, check)
                ans += 1
    return ans


n = int(input())
a = [input() for _ in range(n)]
print(go(False), go(True))
