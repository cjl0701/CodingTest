# https://www.acmicpc.net/problem/4574
# 핵심 아이디어, 논리 비슷한데 왜 틀렸나.. range(2,10) 이라고 했다..
""" 완전 탐색 돌리기 복잡한 이유: 복잡한 인덱스
    => 순서 부여하기 """
di = (1, 0)
dj = (0, 1)


# (i,j) 위치에 num을 놓을 수 있는가?
def is_possible(i, j, num):
    if check_row[i][num] or check_col[j][num] or check_sq[(i // 3) * 3 + j // 3][num]:
        return False
    return True


def check(i, j, num, mark):
    check_row[i][num] = check_col[j][num] = check_sq[(i // 3) * 3 + j // 3][num] = mark


def go(no):  # (row, col)으로 받으면 뭔가 복잡
    if no >= 81:
        return True
    i, j = no // 9, no % 9
    if greed[i][j] != 0:
        return go(no + 1)  # False라고 return 안하면 계속 진행된다..

    # 어떤 타일(2칸)을 놓을 수 있는가
    for num1 in range(1, 10):
        if not is_possible(i, j, num1):
            continue
        check(i, j, num1, True)
        greed[i][j] = num1
        for k in range(2):
            ni, nj = i + di[k], j + dj[k]
            if not (0 <= ni < 9 and 0 <= nj < 9) or greed[ni][nj] != 0:
                continue
            for num2 in range(1, 10):
                if num1 == num2 or tile[num1][num2]:
                    continue
                if not is_possible(ni, nj, num2):
                    continue
                check(ni, nj, num2, True)
                greed[ni][nj] = num2
                tile[num1][num2] = tile[num2][num1] = True
                if go(no + 1):
                    return True
                tile[num1][num2] = tile[num2][num1] = False
                check(ni, nj, num2, False)
                greed[ni][nj] = 0
        check(i, j, num1, False)
        greed[i][j] = 0
    return False


tc = 1
while True:
    n = int(input())
    if n == 0:
        break
    greed = [[0] * 9 for _ in range(9)]
    # 백트래킹을 위한 check
    check_row = [[False] * 10 for _ in range(9)]  # i번째 row일때 해당 숫자 가능한가
    check_col = [[False] * 10 for _ in range(9)]  # j번째 col일때 해당 숫자 가능한가
    check_sq = [[False] * 10 for _ in range(9)]  # i*3+j번째 사각형에 해당 숫자 가능한가
    # 사용 타일 체크를 위한 리스트
    tile = [[False] * 10 for _ in range(10)]  # (x,y) 타일 가능한가?

    for _ in range(n):
        temp = input().split()
        i1, j1, num1 = ord(temp[1][0]) - ord('A'), int(temp[1][1]) - 1, int(temp[0])
        i2, j2, num2 = ord(temp[3][0]) - ord('A'), int(temp[3][1]) - 1, int(temp[2])
        greed[i1][j1] = num1
        greed[i2][j2] = num2
        check(i1, j1, num1, True)
        check(i2, j2, num2, True)
        tile[num1][num2] = tile[num2][num1] = True

    for num, temp in enumerate(input().split(), start=1):
        i, j = ord(temp[0]) - ord('A'), int(temp[1]) - 1
        greed[i][j] = num
        check(i, j, num, True)

    go(0)
    print(f"Puzzle {tc}")
    for line in greed:
        print(''.join(map(str, line)))
    tc += 1
