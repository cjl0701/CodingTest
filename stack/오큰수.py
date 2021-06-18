# https://www.acmicpc.net/problem/17298
"""
오큰수 NGE(i)는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수, 없는 경우 -1.
오른쪽으로 이동하며 큰 수를 만나면 바로 기록 -> 스택에 쌓는다.
"""
import sys

n = int(input())
stack = list()
answer = ['-1'] * n
for i, new in enumerate(list(map(int, sys.stdin.readline().split()))):
    while stack and stack[-1][0] < new:
        answer[stack.pop()[1]] = str(new)
    stack.append((new, i))
print(' '.join(answer))
