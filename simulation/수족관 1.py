# https://www.acmicpc.net/problem/8982
"""개선: 같은 선분에 대해 여러번 처리 => 선분 단위로 그룹 지어 처리"""
import sys

n = int(input())
n -= 2
n //= 2
index = dict()
top = [0] * n
bottom = [0] * n
width = [1] * n
point = [tuple() for _ in range(n)]

sys.stdin.readline()
for i in range(n):
    c1, r = map(int, sys.stdin.readline().split())
    c2, r = map(int, sys.stdin.readline().split())
    index[(c1, c2)] = i
    bottom[i] = r
    width[i] = c2 - c1
sys.stdin.readline()

for _ in range(int(input())):
    c1, r1, c2, r2 = map(int, sys.stdin.readline().split())
    hole = index[(c1, c2)]
    # 구멍 내기 -> 수면 높이 달라짐
    top[hole] = r1
    surface = r1
    for i in range(hole - 1, -1, -1):
        surface = min(surface, bottom[i])
        top[i] = max(surface, top[i])
    surface = r1
    for i in range(hole + 1, n):
        surface = min(surface, bottom[i])
        top[i] = max(surface, top[i])

ans = 0
for i in range(n):
    if bottom[i] - top[i] > 0:
        ans += (bottom[i] - top[i]) * width[i]
print(ans)
""" 예외
14
0 0
0 5
1 5
1 3
2 3
2 4
3 4
3 2
5 2
5 4
6 4
6 3
8 3
8 0
1
1 3 2 3
"""
