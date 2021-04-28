# https://www.acmicpc.net/problem/10942
# 시간 초과 ->IO, recursive error -> setrecursionlimit
import sys

sys.setrecursionlimit(100000)  # 최대 재귀 깊이 늘리기
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

d = [[-1] * n for _ in range(n)]


# 재귀를 더 줄이려면 백트래킹을 적용하자.
def f(s, e):
    if s >= e:
        return 1
    if d[s][e] == -1:
        d[s][e] = 0
        if data[s] == data[e]:  # 백트래킹. 최소 조건이 맞지 않으면 재귀 들어갈 필요x
            d[s][e] = f(s + 1, e - 1)
    return d[s][e]


for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(f(s - 1, e - 1)) + "\n")

# bottom-up: 길이가 1인 것, 2인 것 k인 것 순으로 구함
