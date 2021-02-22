# 맞춰봐 https://www.acmicpc.net/problem/1248
# 백트래킹, 건너뛰기 안하면 시간초과..! 옵션이 아닌 필수

# 재귀 설계
# 탈출 조건: idx==n
# 성공 조건: idx==n 까지 도달
# 연산: idx 마다 숫자 선택-> 타당성 검사(back tracking)
# 반환: 조기 종료를 위한 bool

n = int(input())
data = input()
sign = [[0] * n for _ in range(n)]
idx = 0
for i in range(n):
    for j in range(i, n):
        if data[idx] == '0':
            sign[i][j] = 0
        elif data[idx] == '+':
            sign[i][j] = 1
        else:
            sign[i][j] = -1
        idx += 1
arr = [0] * n  # arr[n] ->  list index out of range


def valid(idx):
    sum = 0
    for i in range(idx, -1, -1):
        sum += arr[i]
        if sign[i][idx] == 0 and sum != 0:
            return False
        elif sign[i][idx] > 0 and sum <= 0:
            return False
        elif sign[i][idx] < 0 and sum >= 0:
            return False
    return True


def go(idx):
    if idx == n:
        return True
    # idx 순서대로 하나씩 선택
    # 부호에 따라 건너 뛰기
    # 합 조건에 어긋하면 back tracking
    if sign[idx][idx] == 0:
        arr[idx] = 0
        return valid(idx) and go(idx + 1)
    for i in range(1, 11):
        arr[idx] = i * sign[idx][idx]
        if valid(idx) and go(idx + 1):
            return True

    return False


go(0)
print(' '.join(map(str, arr)))
