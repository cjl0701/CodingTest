# https://programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque


def solution(priorities, location):
    q = deque()
    for i, p in enumerate(priorities):
        q.append((i, p))
    priorities.sort(key=lambda x: -x)
    idx = 0
    while q:
        while priorities[idx] != q[0][1]:
            q.append(q.popleft())
        idx += 1
        if q.popleft()[0] == location:
            break
    return idx
