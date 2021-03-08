# 사다리 조작
# 후보를 추려 건너뛰기!
n, m, h = map(int, input().split())
arr = [[0] * (n + 1) for _ in range(h + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[a][b + 1] = -1
# 탐색 줄이기 - jump!
candidates = list()
for i in range(1, h + 1):
    for j in range(1, n):
        if arr[i][j] == 0 and arr[i][j + 1] == 0:
            candidates.append((i, j))


def endpoint(arr, j):
    for i in range(1, h + 1):
        if arr[i][j] == 1:
            j += 1
        elif arr[i][j] == -1:
            j -= 1
    return j


def simulate(arr):
    for j in range(1, n + 1):
        if endpoint(arr, j) != j:
            return False
    return True


def go(arr, select, idx):
    if select > 3:
        return -1

    if simulate(arr):  # 성공하면 바로 종료
        return select
    ans = -1
    for i in range(idx, len(candidates)):
        a, b = candidates[i]
        if arr[a][b] == 0 and arr[a][b + 1] == 0:
            arr[a][b] = 1
            arr[a][b + 1] = -1
            ret = go(arr, select + 1, i + 2)  # dfs라 현재 1일 때 3이 return 될 수있다..
            arr[a][b] = arr[a][b + 1] = 0
            if ret != -1:
                if ans == -1 or ans > ret:
                    ans = ret
    return ans


print(go(arr, 0, 0))
