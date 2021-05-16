# https://www.acmicpc.net/problem/12872
"""
N개 중 P개의 노래를 듣는 경우의 수
- 모든 노래가 들어가야 한다 (N<=P)
- 같은 노래를 추가하려면 그 사이에 M개의 곡이 있어야 한다 (M<=N)

=> 경우를 나누자면,
1. 같은 노래를 추가할 경우
2. 새로운 노래를 추가할 경우

완탐으로하면 O(N^P), 최악의 경우 100^100으로 너무 커. => 갯수만 궁금하므로 DP
for문 애매 => 재귀
중복 재귀를 막기 위해서 수렴식으로 d[i][j]=d[i-1][t-1]+d[i-1][t]
"""

whole, m, p = map(int, input().split())
# 변하는 것: p, already, new이나, already+new==p이므로 new 생략
d = [[-1] * (whole + 1) for _ in range(p + 1)]


def f(i, already):
    if i == 0:
        return 1 if already == 0 else 0
    if d[i][already] == -1:
        d[i][already] = 0  # 방문 표시
        if already - 1 >= 0:  # 신곡 추가 / (whole - (already - 1))는 항상 양수..
            d[i][already] = f(i - 1, already - 1) * (whole - (already - 1))
        if already - m > 0:  # 기존 곡 추가
            d[i][already] += f(i - 1, already) * (already - m)
        d[i][already] %= 1000000007
    return d[i][already]


print(f(p, whole))