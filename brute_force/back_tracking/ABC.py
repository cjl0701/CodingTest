# https://www.acmicpc.net/problem/12969
"""경우의 수가 커도 백트래킹으로 해결 가능할 수 있다"""


def dfs(l, a, b, left):
    # 실패 조건
    if left < 0 or l > n or check[l][a][b][left]:
        return False
    check[l][a][b][left] = True

    # 탈출 조건
    if l == n:
        return left == 0

    # 진행
    global ans
    # A 추가
    if dfs(l + 1, a + 1, b, left):
        ans = 'A' + ans
        return True
    # B 추가
    if dfs(l + 1, a, b + 1, left - a):
        ans = 'B' + ans
        return True
    # C 추가
    if dfs(l + 1, a, b, left - a - b):
        ans = 'C' + ans
        return True

    return False


ans = ""
n, k = map(int, input().split())
check = [[[[False] * (k + 1) for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]

if dfs(0, 0, 0, k):
    print(ans)
else:
    print(-1)