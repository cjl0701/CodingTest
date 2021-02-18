"""
# input => str
n = int(input())
# data = list(map(int, input().split()))
data = input().split()  # ['1', '2', '3'] <class 'list'>
data = map(int, data)  # <map object at 0x0000018FBB3399A0> <class 'map'>
l1 = list(data)  # [1, 2, 3]
l2 = list(data)  # []  generator니까!
print(l1)
print(l2)

a, b, c = map(int, input().split())
print(a, b, c)

# 빠르게 입력 받기
import sys

data = sys.stdin.readline().rstrip()  # 오른쪽 엔터 제거
print(data)
"""
# print 이후 줄바꿈 하지 않으려면
print(1, end="")
print(2, end="!")  # 12!

# f-string
answer = 4
print(f"정답은 {answer}입니다")

