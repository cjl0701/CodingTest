# 플레이 리스트
# 틀린 이유: 애초에 bottom-up은 원소 단위로 모든 점을 순회하니까 발상도 그렇게 함..
# 구현 시: 거꾸로 구할 수 있다는 점을 몰랐다.
""" but bottom-up도 재귀로 할 수 있다.
=> 큰 단위로, 좀 더 일반화해서 생각해도 된다.
경우의 수 : case 분류 => 현 상태까지 갯수 * 현재 선택할 수 있는 경우의 수
"""

n, m, p = map(int, input().split())
# d[p][x] : p번째 곡 선택, 이미 추가된 곡 x 개, 추가되지 않은 곡 n-x개. (y는 x,n으로 표현)
""" skill: 거꾸로 구하기
    d[p][x]*y = d[p+1][x+1] 이기도 하지만, 반대로 미래로부터 구할 수도 있다.
    d[p][x] = d[p+1][x+1]*y """
d = [[-1] * (n + 1) for _ in range(p + 1)]


def f(i, x):
    y = n - x
    if i == p:
        if y == 0:
            return 1  # 모든 곡을 다 써야 한다고 했으므로
        else:
            return 0
    if d[i][x] == -1:
        d[i][x] = 0
        # 새로운 곡 추가
        if y > 0:
            d[i][x] = f(i + 1, x + 1) * y
        # 추가된 곡에서 재 추가
        if x > m:
            d[i][x] += f(i + 1, x) * (x - m)
        d[i][x] %= 1000000007
    return d[i][x]


print(f(0, 0))
