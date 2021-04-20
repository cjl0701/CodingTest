# https://www.acmicpc.net/problem/2008
""" 접근법
하나씩 놓고 지우기엔 경우의 수가 너무 많다. => 문제를 크기를 좁히자
모든 경우를 알 필요없다. 최소 경우만 알면된다.
최소비용 = 이전 단계까지의 최소 비용 + 최소비용
단계의 기준을 정하자
"""

m, n = map(int, input().split())
start, end, delete, add = map(int, input().split())
line = [0] + [int(input()) for _ in range(n)]

"""문제 크기를 줄여보자. 간단하게 한 단계만 생각"""
# 변하는 것: 행, 도착지점
# d[r][x]: r번째 가로선까지 고려했을 때, 출발점에서 x로 가는 최소 비용
# d[r][x] = d[r-1][y] + cost (1<=y<=m)
d = [[int(1e10)] * (m + 1) for _ in range(n + 1)]

# 초기 값: 맨 위에 추가
for x in range(1, m + 1):
    d[0][x] = abs(start - x) * add

# 가로행 1~n번 고려
for r in range(1, n + 1):
    for to in range(1, m + 1):
        for frm in range(1, m + 1):
            left, right = frm, to
            if left > right:
                left, right = right, left
            # 추가 비용
            if left <= line[r] < right:  # 사이에 가로선이 있는 경우
                cost = (right - left - 1) * add
            else:  # 사이에 가로선이 없는 경우
                cost = (right - left) * add
                if line[r] in (left - 1, right):  # 삭제가 필요한 경우
                    cost += delete
            d[r][to] = min(d[r][to], d[r - 1][frm] + cost)

print(d[n][end])
