tc = int(input())
dx = (-1, 0, 1)
for _ in range(tc):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    # d[i][j]: i번째 열 j행을 선택했을 때 최대값 <- 나중에 복잡
    # d[i][j] i행 j열 일 때 최대값.. 계산하기 편한 쪽으로 맞추는게 낮다..
    # 한 줄 입력값으로 2차원 배열을 초기화 하는 방법!!
    d = []
    index = 0
    for i in range(n):  # d 미리 싹 다 초기화.. 나중에 깔끔해짐.
        d.append(data[index:index + m])
        index += m

    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 올 때
            if i == 0:  # 예외 처리 깔끔
                left_up = 0
            else:
                left_up = d[i - 1][j - 1]
            # 왼쪽에서 올 때
            left = d[i][j - 1]
            # 왼쪽 아래에서 올 때
            if i == n - 1:  # 예외 처리 깔끔
                left_down = 0
            else:
                left_down = d[i + 1][j - 1]
            d[i][j] += max(left_up, left, left_down)  # 한꺼번에 계산 때리기 깔끔
    ans = 0
    for i in range(n):
        ans = max(ans, d[i][m - 1])
    print(ans)
