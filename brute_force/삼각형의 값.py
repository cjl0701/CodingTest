def calc(row, left, right, s):
    # 범위 연산은 공통이므로
    if not (1 <= row <= h) or left < 1 or right >= 2 * row:
        return
    s += sum[row][right] - sum[row][left - 1]
    global ans
    if ans < s:
        ans = s
    if left % 2 == 1:  # 홀수
        calc(row + 1, left, right + 2, s)
    else:  # 짝수
        calc(row - 1, left - 2, right, s)


tc = 0
while True:
    tc += 1
    inputs = list(map(int, input().split()))
    h = inputs[0]
    if h == 0:
        break
    # 리스트, 누적합
    a = [[]]  # 빈 리스트 a[0] 뒤에 이어 붙인다
    sum = [[]]
    k = 1
    for i in range(1, h + 1):
        a.append([0] * (2 * i)) # 그때그때 초기화
        sum.append([0] * (2 * i))  # 누적합 계산하기 편하도록 0을 비운다
        for j in range(1, 2 * i):
            a[i][j] = inputs[k]
            k += 1
            sum[i][j] = sum[i][j - 1] + a[i][j]

    ans = -1000
    for i in range(1, h + 1):
        for j in range(1, 2 * i):
            calc(i, j, j, 0)
    print(str(tc) + ". " + str(ans))