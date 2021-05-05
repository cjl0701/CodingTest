# https://www.acmicpc.net/problem/17070
"""충격 - 시간초과 난 이유
일반화해서 풀면 if문을 매번 3*2회씩 추가적으로 해야 한다.. 그래서 시간 초과
일반화를 하기 때문에 x만 검사해도 될때 y도 검사해야 한다..
문제에서 백만가지 경우라고 했지만, 그 훨씬 이상의 가짓수를 계산하는 것..

때에 따라서는 더럽게 푸는 게 맞다..
특이 케이스 하나가 아니라 3개 중 2개가 2번 연산하는 거잖아
그럼 3번 연산으로 일반화하는게 에바지..
"""
""" 충격 2 - 시간 초과 난 진짜 이유
jump를 못해서..
x == y == n - 1  <- 방식으로 하면 x!=n-1일 경우에도 jump 불가..3가지 다 비교해봐야 함..
x == n - 1 and y == n - 1 <- 방식으로 하니 통과..
작은 차이가 크구나.. 짧다고 좋은 게 아니구나.. 
"""
"""
0. 방법의 수가 백만 이하라고 주어졌다 
    => 완전 탐색 가능.
1. 2칸 차지 -> 2칸의 정보를 유지?
    => no. 방향과 뒷칸을 알면 앞칸을 알 수 있고, 앞칸은 뒷칸으로만 이동하게 되어있다.
2. 방향에 따른 이동 
    => 3가지로 일반화하면 불필요한 연산이 너무 많아진다.
"""


# dir 방향으로 부터 (x,y)에 도달
def go(x, y, dir):
    if x == n - 1 and y == n - 1:
        return 1
    ans = 0
    if dir == 0:  # 가로
        if y + 1 < n and a[x][y + 1] == 0:
            ans += go(x, y + 1, 0)
            if x + 1 < n and a[x + 1][y] == 0 and a[x + 1][y + 1] == 0:
                ans += go(x + 1, y + 1, 2)
    elif dir == 1:  # 세로
        if x + 1 < n and a[x + 1][y] == 0:
            ans += go(x + 1, y, 1)
            if y + 1 < n and a[x][y + 1] == 0 and a[x + 1][y + 1] == 0:
                ans += go(x + 1, y + 1, 2)
    elif dir == 2:  # 대각선
        garo = sero = False
        if y + 1 < n and a[x][y + 1] == 0:
            garo = True
            ans += go(x, y + 1, 0)
        if x + 1 < n and a[x + 1][y] == 0:
            sero = True
            ans += go(x + 1, y, 1)
        if garo and sero and a[x + 1][y + 1] == 0:
            ans += go(x + 1, y + 1, 2)
    return ans


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
print(go(0, 1, 0))
