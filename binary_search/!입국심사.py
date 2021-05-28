# https://programmers.co.kr/learn/courses/30/lessons/43238
# n이 너무 크다. 완탐 x.. 너무 크다.. 이진 탐색? 파라메트릭 서치!
"""
파라메트릭 서치: 최적해를 찾아가는 문제
1. 답: 최적 시간
2. 답의 범위를 줄여간다.
3. 그 시간에 n명 처리가 가능한가?
"""


def possible(n, times, time_limit):
    cnt = 0
    for take_time in times:
        cnt += time_limit // take_time
    return cnt >= n


# 가능하다면 줄이고, 너무 많이 줄였으면 그것보다는 늘리고!
def solution(n, times):
    start, end = 1, max(times) * n
    optimal = 0

    while start <= end:
        mid = (start + end) // 2
        if possible(n, times, mid):  # 성공하면 시간을 줄이는 방향으로 간다
            optimal = mid  # 점점 최적해로 다가간다.
            end = mid - 1  # 최소 값을 찾는 것이 목적이므로, 값의 범위를 줄여간다.
        else:
            start = mid + 1  # 지금보다는 늘려야만 한다.

    return optimal
