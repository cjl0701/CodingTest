# N-Queen https://www.acmicpc.net/problem/9663

# 재귀 설계
# 종료: row==n
# 성공: row==n 까지 도달하면 count
# 연산: 놓을 수 있는 곳이면 놓고 다음 step
# 반환: 성공시 1

def valid(row, col):
    if check_col[col]:
        return False
    if check_ws[row + col]:
        return False
    if check_es[row - col + (n - 1)]:
        return False
    return True


def go(row):
    if row == n:
        return 1
    cnt = 0
    # 모든 지점에 놓아본다.
    for col in range(n):
        if valid(row, col):  # 놓을 수 없는 지점이면 back
            check_col[col] = check_ws[row + col] = check_es[row - col + (n - 1)] = True
            cnt += go(row + 1)
            check_col[col] = check_ws[row + col] = check_es[row - col + (n - 1)] = False
    return cnt


n = int(input())
check_col = [False] * n
check_ws = [False] * (2 * n - 1)  # row+col
check_es = [False] * (2 * n - 1)  # row-col+n-1
print(go(0))
