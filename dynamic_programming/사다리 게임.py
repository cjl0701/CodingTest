# BJ 2008
""" 접근법
하나씩 놓고 지우기엔 경우의 수가 너무 많다. => 문제를 분리하자
모든 경우를 알 필요없다. 최소 경우만 알면된다.
최소비용 = 이전 단계까지의 최소 비용 + 최소비용
단계의 기준을 정하자
"""
w, h = map(int, input().split())
start, goal, delete, add = map(int, input().split())
rows = [0] + [int(input()) for _ in range(h)]
start -= 1
goal -= 1
# d[i][j] = i번째 가로선까지 고려했을 때, start에서 j까지 최소 비용
d = [[100 * 500 * 1000 + 1] * w for _ in range(h + 1)]

# 초기값. 가로선을 아직 만나지 않았을 때
for j in range(w):
    d[0][j] = abs(start - j) * add

for i in range(1, h + 1):
    for j in range(w):
        for k in range(w):
            left, right = (k, j) if k <= j else (j, k)
            cost = d[i - 1][k]
            # 삭제가 필요한 경우
            if rows[i] in (left, right + 1):
                cost += delete
            # 추가
            if left + 1 <= rows[i] <= right:  # 중간에 가로선이 있는 경우
                cost += (right - left - 1) * add
            else:  # 중간에 가로선이 없는 경우
                cost += (right - left) * add
            d[i][j] = min(d[i][j], cost)
print(d[h][goal])
