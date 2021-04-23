# https://programmers.co.kr/learn/courses/30/lessons/43238
# 파라메트릭 서치: 최적해를 찾아가는 문제
# 1. 답: 최적 시간
# 2. 답의 범위를 줄여간다.
# 3. 그 시간에 n명 처리가 가능한가?

def possible(n, times, time_limit):
    cnt = 0
    for take_time in times:
        cnt += time_limit // take_time
    return cnt >= n


def solution(n, times):
    start, end = 0, max(times) * n
    optimal = 0

    while start <= end:
        mid = (start + end) // 2
        if possible(n, times, mid):
            optimal = mid # 점점 최적해로 다가간다.
            end = mid - 1  # 지금보다 더 줄여본다.
        else:
            start = mid + 1  # 지금보다 늘려야 한다.

    return optimal
