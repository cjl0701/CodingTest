# https://www.acmicpc.net/problem/12872
# 완전 탐색 너무 많아 => 규칙/특징/의미/배운것
# p개 =  p-1일 때 의 경우의 수 x 조건 만족 수 : DP
# 경우의 수 -> case 분류
""" 시간 초과
재귀에서 check로 중복 재귀하지 않아야 한다.
check를 사용하기 위해선,
start->end로 가지만 base가 end이도록 구성해야 한다.
p->p+1이지만, 구현 편의를 위해 p<-p+1이라고 해석하자.
"""
# 중복은 건너뛰어야 -> top-down
MOD = 1000000007
n, m, p = map(int, input().split())
"""
d = [[[-1] * (n + 1) for _ in range(n + 1)] for _ in range(p + 1)]
new, picked 해서 눈에 안띄었는데, new, picked type을 의미하고 합이 항상 n이다..
항정식이므로 변수 하나 유지해도 나머지 구할 수 있다.
"""
d = [[-1] * (n + 1) for _ in range(p + 1)]


def f(cnt, picked):
    new = n - picked
    # 끝에 도달해서 성공한 경우만 센다.
    if cnt == p:
        return 1 if new == 0 else 0

    if d[cnt][picked] == -1:
        d[cnt][picked] = 0  # 방문 체크
        # 신곡을 플레이리스트에 추가
        if new > 0:
            d[cnt][picked] += f(cnt + 1, picked + 1) * new
            """ (p,x)에서 (p+1,x-1)이 된다. (x개 선택지 가능)
            반대로 (p,x)는 (p+1,x-1)에서 하나 뺀 것. (x개 선택지 가능) """
        # 기존 곡에서 추가
        if picked > m:  # 기존 곡 중 적어도 m개는 추가 못한다.
            d[cnt][picked] += f(cnt + 1, picked) * (picked - m)
        d[cnt][picked] %= MOD
    return d[cnt][picked]


print(f(0, 0))
