import heapq
from collections import deque


def solution(jobs):
    n = len(jobs)
    answer = 0
    cur_time = 0
    jobs.sort()
    request = deque(jobs)
    waiting_q = []

    while request or waiting_q:
        # 작업 도중 요청 다 받기
        while request and request[0][0] <= cur_time:
            req = request.popleft()
            heapq.heappush(waiting_q, (req[1], req[0]))  # 소요 시간 순

        # 작업 도중 아닐 때 요청 -> 현재 시간 갱신해서 코드 일관성 유지
        if not waiting_q: # 선행 조건들 이용하자. 굳이 request 확인할 필요x
            cur_time = request[0][0]
        else:
            process = heapq.heappop(waiting_q) # process = waiting_q.pop() #끝에 있는거 꺼냄
            cur_time += process[0]
            answer += (cur_time - process[1])
    return answer // n

""" 큐 안 쓴 버전
def solution(jobs):
    answer = 0
    jobs.sort(key=lambda job: job[0])  # ==jobs.sort(). 요청 시간을 기준으로 정렬
    cur_t = 0
    h = []
    idx = 0
    while h or idx < len(jobs):
        while idx < len(jobs) and cur_t >= jobs[idx][0]:
            heapq.heappush(h, (jobs[idx][1], jobs[idx][0]))  # 튜플의 정렬기준은 앞에서부터
            idx += 1
        if not h:
            cur_t = jobs[idx][0]  # 시간 갱신
        else:
            work_t, req_t = heapq.heappop(h)
            cur_t += work_t
            answer += cur_t - req_t
    return answer // len(jobs)
"""