# BJ 14238
"""
1. DP를 쓰면 횟수가 줄여지는 이유
    d[a][b][c][p2][p1]: 각각 a,b,c 개 남았고, 전전날 p2, 전날 p1가 출근하는게 가능한가?
    앞의 구성이 뭐가 됐든, a,b,c,p2,p1인 상태에서 할 수 있는 선택은 같고 결과도 같다
    => 같은 상태로 보고 여러번 반복하지 않는다.
2. idx를 기준으로 하지 않는 이유
    정답이 날짜 기준인 것이 아니므로. a,b,c 선택을 전부 마친 상태가 정답 상태.
    첫 선택을 정할 수가 없으므로, 아무 제약이 없는 A,A로 시작한다.
    그럼 처음 b를 선택할 경우 d[a][b-1][c][0][1]가 되고, 정답은 d[0][0][0][any][any]인 상태이다.
    'i번째 일 일때'로 진행하면 bb,b를 모든 케이스에 대해서 새로운 d로 시작 해봐야한다.
"""
s = input()
n = len(s)
# 0:A, 1:B, 2:C
limit = [0, 0, 0]
for ch in s:
    limit[ord(ch) - ord('A')] += 1
d = [[[[[-1] * 3 for _ in range(3)] for _ in range(n + 1)] for _ in range(n + 1)]
     for _ in range(n + 1)]


def f(a, b, c, p2, p1):
    if a + b + c == 0:
        d[a][b][c][p2][p1] = 1  # a,b,c 다 썼으면 성공
        return d[a][b][c][p2][p1]
    if d[a][b][c][p2][p1] != -1:  # 이미 진행해본 경로는 더 진행x
        return d[a][b][c][p2][p1]
    if a > 0 and f(a - 1, b, c, p1, 0) == 1:  # 진행해서 성공에 도달
        d[a][b][c][p2][p1] = 1  # 성공 표시 및 반환
        return 1
    if b > 0 and p1 != 1 and f(a, b - 1, c, p1, 1) == 1:
        d[a][b][c][p2][p1] = 1  # 추후 정답 추적을 위한 표시
        return 1
    if c > 0 and p1 != 2 and p2 != 2 and f(a, b, c - 1, p1, 2) == 1:
        d[a][b][c][p2][p1] = 1
        return 1
    # a,b,c 전부 실패
    d[a][b][c][p2][p1] = 0
    return 0


# 현 상태에서 무얼 선택할 수 있는가 기록
def back(a, b, c, p1):
    if a + b + c == 0:  # 끝에 도달
        return ""
    # 새로운 경로 찾지 않도록 f 말고 d 쓰자
    if a > 0 and d[a - 1][b][c][p1][0] == 1:
        return "A" + back(a - 1, b, c, 0)
    if b > 0 and d[a][b - 1][c][p1][1] == 1:
        return "B" + back(a, b - 1, c, 1)
    if c > 0 and d[a][b][c - 1][p1][2] == 1:
        return "C" + back(a, b, c - 1, 2)
    return ""


if f(*limit, 0, 0) == 1:
    print(back(*limit, 0))
else:
    print(-1)

"""
def f(idx, x, y):
    if idx == len(s):
        return True
    # 이미 방문한 적 있으면 진행 x
    if d[idx][x][y]:
        return False
    d[idx][x][y] = True
    # A, B, C를 차례대로 넣어본다.
    global ans, a, b, c
    temp = ans
    if a > 0:
        ans = temp + 'A'
        a -= 1
        if f(idx + 1, y, 0):
            return True
        a += 1
    if b > 0 and y != 1:
        ans = temp + 'B'
        b -= 1
        if f(idx + 1, y, 1):
            return True
        b += 1
    if c > 0 and x != 2 and y != 2:
        ans = temp + 'C'
        c -= 1
        if f(idx + 1, y, 2):
            return True
        c += 1
    return False


# if f(0, 0, 0) or f(0, 0, 1) or f(0, 0, 2) or f(0, 1, 0) or f(0, 1, 2) or f(0, 2, 0) or f(0, 2, 1):
if len(s) <= 1:
    print(s)
elif f(0, 0, 0) or f(0, 0, 1) or f(0, 0, 2) or f(0, 1, 0) or f(0, 1, 2) or f(0, 2, 0) or f(0, 2, 1):
    print(ans)
else:
    print(-1)
"""
