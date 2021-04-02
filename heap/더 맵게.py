# 프로그래머스
import heapq


def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while scoville:
        scv = heapq.heappop(scoville)
        if scv >= K:
            return cnt
        if scoville:
            scv += heapq.heappop(scoville) * 2
            cnt += 1
            heapq.heappush(scoville, scv)
    return -1


scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))
