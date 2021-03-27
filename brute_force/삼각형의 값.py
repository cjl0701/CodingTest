# BJ 4902 https://www.acmicpc.net/problem/4902
""" 치명적인 실수 : 문제 설명, 값의 범위 잘 읽자..
1. n=3까지만 고려해서 문제를 잘 못 이해..
2. 어디서 틀렸는지 모르겠다 => 알고보니 초기값이 0이 아니라 -10000이어야.. 리턴값도..
3. 전체 갯수 못 구하겠다.. 너무 수학이야 => 갯수 못구했으면 중복 피해야지
"""
""" skill
1. 쫄지말고 case 분류해서 하나씩 작은 문제를 해결하면 풀린다.
2. 중복을 연산을 피하기 위한 누적합 => s[0] 비워두기
3. 비슷한 연산인데 조건에 따라 다른 부분이 있으면 한 함수에서 if문 쓰면 된다..
"""
import sys


def down(row, left, right, upper):
    if row >= n or right >= len(a[row]):
        return 0  # 최하값이어야 한다..
    cur = upper + s[row][right]
    if left - 1 >= 0:
        cur -= s[row][left - 1]
    return max(cur, down(row + 1, left, right + 2, cur))


def up(row, left, right, lower):
    if row < 0 or left < 0 or right >= len(a[row]):
        return 0
    cur = lower + s[row][right] - s[row][left - 1]
    return max(cur, up(row - 1, left - 2, right, cur))


t = 1
while True:
    temp = list(map(int, sys.stdin.readline().split()))
    n = temp[0]
    if n == 0:
        break
    # 배열로 표현
    a = [[] for _ in range(n)]
    idx, length = 1, 1
    for i in range(n):
        a[i] = temp[idx:idx + length]
        idx += length
        length += 2

    ans = 0
    # 누적합 구해두기
    s = [[0] * (2 * n - 1) for _ in range(n)]
    for i in range(len(a)):
        for j in range(len(a[i])):
            if j - 1 >= 0:
                s[i][j] = s[i][j - 1]
            s[i][j] += a[i][j]

    # 각 시작점에 대하여, case 별로 구하기
    for i in range(n):
        for j in range(len(a[i])):
            if j % 2 == 0:
                ans = max(ans, down(i, j, j, 0))
            else:
                ans = max(ans, up(i, j, j, 0))
    print(str(t) + ". " + str(ans))
    t += 1
