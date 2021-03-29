# BJ 12969
# 틀린 이유:check[l][a][b][c] => l,a,b,c일때 cnt가 다를 수 있다..
n, k = map(int, input().split())
LIMIT = int(30 * 29 / 2 + 1)  # 436
check = [[[[False] * LIMIT for _ in range(31)] for _ in range(31)] for _ in range(31)]


def dfs(i, a, b, cnt):
    if i == n:
        return True if cnt == k else False
    if check[i][a][b][cnt]:  # check[l][a][b][c]는 틀림!
        return False
    check[i][a][b][cnt] = True
    global ans
    temp = ans
    # i번째에 a 추가
    ans = temp + "A"
    if dfs(i + 1, a + 1, b, cnt):
        return True
    # i번째에 b 추가
    ans = temp + "B"
    if dfs(i + 1, a, b + 1, cnt + a):
        return True
    # i번째에 c 추가
    ans = temp + "C"
    if dfs(i + 1, a, b, cnt + a + b):
        return True
    return False


ans = ""
if dfs(0, 0, 0, 0):
    print(ans)
else:
    print(-1)
