# 경사로
# 시뮬레이션: 문제에 나와 있는 조건을 적는다.
# 복잡하니까 실수하고 틀리는 거다. 복잡하게 설계하지 마라. 코드를 간결하게 해라. 함수화해라.
# 가로, 세로 방향의 코드가 비슷하므로, 함수를 만들어 재활용한다.
# i,j 헷갈리게 만들지 않는다. 쉬운 방법을 찾자.
# 모든 케이스를 포함하도록 설계한다.
def valid(a):
    check = [False] * len(a)
    for i in range(1, n):
        if a[i - 1] != a[i]:
            diff = a[i - 1] - a[i]
            if diff == -1:  # 오르막
                # 경사로를 놓을 칸의 높이는 모두 같아야 한다. l개 연속
                for k in range(1, l + 1):
                    if i - k < 0:  # 경사로를 놓다가 범위를 벗어나면 안된다.
                        return False
                    if check[i - k]:  # 경사로를 놓은 곳에 또 경사로를 놓을 순 없다.
                        return False
                    if a[i - k] != a[i - 1]:
                        return False
                    check[i - k] = True
            elif diff == 1:  # 내리막
                for k in range(l):
                    if i + k >= n:
                        return False
                    if check[i + k]:
                        return False
                    if a[i] != a[i + k]:
                        return False
                    check[i + k] = True
            else:  # 높이 차이가 1이어야만 경사로를 둘 수 있다.
                return False
    return True

n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for row in arr:
    if valid(row):
        ans += 1
for c in range(n):
    col = [arr[i][c] for i in range(n)]
    if valid(col):
        ans += 1
print(ans)
""" 개같이 짠 코드. 초반 설계의 중요성..
for i in range(n):
    for j in range(n - 1):
        if a[i][j] == a[i][j + 1]:
            continue
        if abs(a[i][j] - a[i][j+1]) > 1:
            break
        if a[i][j] - a[i][j + 1] == 1:  # 내리막길
            if l == 1:
                if check[i][j + 1]:
                    break
                else:
                    check[i][j + 1] = True
                    continue
            for k in range(j + 1, j + l):  # l-1번 연속되면 가능
                if not k + 1 < n or check[i][k] or check[i][k + 1] or a[i][k] != a[i][k + 1]:
                    break
            else:  # 경사로를 놓는다.
                for k in range(j + 1, j + l + 1):
                    check[i][k] = True
                continue
            break  # 불연속. 실패
        elif a[i][j] - a[i][j + 1] == -1:  # 오르막길
            if l == 1:
                if check[i][j]:
                    break
                else:
                    check[i][j] = True
                    continue

            for k in range(j, j - l + 1, -1):
                if not k - 1 >= 0 or check[i][k] or check[i][k - 1] or a[i][k] != a[i][k - 1]:
                    break
            else:
                for k in range(j, j - l, -1):
                    check[i][k] = True
                continue
            break
    else:  # 완료
        ans += 1
# 세로
check = [[False] * n for _ in range(n)]
for j in range(n):
    for i in range(n - 1):
        if a[i][j] == a[i + 1][j]:
            continue
        if abs(a[i][j] - a[i + 1][j]) > 1:
            break
        if a[i][j] - a[i + 1][j] == 1:  # 내리막길
            if l == 1:
                if check[i + 1][j]:
                    break
                else:
                    check[i + 1][j] = True
                    continue
            for k in range(i + 1, i + l):  # l번 연속되면 가능
                if not k + 1 < n or check[k][j] or check[k + 1][j] or a[k][j] != a[k + 1][j]:
                    break
            else:  # 경사로를 놓는다.
                for k in range(i + 1, i + l + 1):
                    check[k][j] = True
                continue
            break  # 불연속. 실패
        elif a[i][j] - a[i + 1][j] == -1:  # 오르막길
            if l == 1:
                if check[i][j]:
                    break
                else:
                    check[i][j] = True
                    continue
            for k in range(i, i - l + 1, -1):
                if not k - 1 >= 0 or check[k][j] or check[k - 1][j] or a[k][j] != a[k - 1][j]:
                    break
            else:
                for k in range(i, i - l, -1):
                    check[k][j] = True
                continue
            break
    else:  # 완료
        ans += 1
print(ans)
"""
