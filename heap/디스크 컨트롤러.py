"""
그리디: 소요 시간이 짧은 것부터 처리하면 전체 대기 시간이 최소다. (처리 시간은 같다)
=> 최소 힙
"""

import heapq


def solution(jobs):
    answer = 0  # ""(현재 시간 - 요청 시간) + 작업 시간" 의 평균
    waiting_q = []
    cur_t = 0
    idx = 0
    n = len(jobs)

    # 먼저 요청이 들어온 작업부터 시작한다 => 요청 시간 별 정렬
    jobs.sort(key=lambda job: job[0])  # jobs.sort() 기본 값이 튜플 앞 놈.

    while idx < n or waiting_q:
        # 작업 요청이 현재 시간보다 작으면 대기
        while idx < n and jobs[idx][0] <= cur_t:
            heapq.heappush(waiting_q, (jobs[idx][1], jobs[idx][0]))  # 튜플의 정렬 기준은 기본값이 앞놈
            idx += 1
        # 대기 큐에 있는 것 처리
        if waiting_q:
            time, req_t = heapq.heappop(waiting_q)
            answer += (cur_t - req_t) + time
            cur_t += time
        # 큐에 아무것도 없는데 시간이 안돼서 진행 못하는 경우
        else:
            cur_t = jobs[idx][0]

    return answer // n


""" 진짜 큐 쓴 버전
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
"""
