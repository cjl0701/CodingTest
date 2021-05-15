# https://www.acmicpc.net/problem/17298
import sys

n = int(input())
stack = list()
answer = ['-1'] * n
for i, new in enumerate(list(map(int, sys.stdin.readline().split()))):
    while stack and stack[-1][0] < new:
        answer[stack.pop()[1]] = str(new)
    stack.append((new, i))
print(' '.join(answer))
