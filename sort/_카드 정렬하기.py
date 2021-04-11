# BJ1715
import heapq

n = int(input())
h = []
for _ in range(n):
    heapq.heappush(h, int(input()))

total = 0
while len(h) > 1:
    s = heapq.heappop(h) + heapq.heappop(h)
    total += s
    heapq.heappush(h, s)
print(total)
