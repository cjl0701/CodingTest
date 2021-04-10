# https://www.acmicpc.net/problem/12969
# O(3^30). 완전 탐색하기엔 너무 큰데.. => check로 백트래킹
n, k = map(int, input().split())
ans = ""
# dict로 하려면 튜플 매번 생성해야 함..
check = [[[[False] * (n * (n + 1) // 2) for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]

def go(i, a, b, cnt):
    if i == n:
        return True if cnt == k else False

    if check[i][a][b][cnt]:
        return False
    check[i][a][b][cnt] = True  # 할 수 있는 선택이 같으므로

    global ans
    temp = ans
    # A 선택
    ans = temp + 'A'
    if go(i + 1, a + 1, b, cnt):
        return True
    # B 선택
    ans = temp + 'B'
    if go(i + 1, a, b + 1, cnt + a):
        return True
    ans = temp
    # C 선택
    ans = temp + 'C'
    if go(i + 1, a, b, cnt + a + b):
        return True
    return False


if go(0, 0, 0, 0):
    print(ans)
else:
    print(-1)
