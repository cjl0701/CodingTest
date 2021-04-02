# 프로그래머스
from collections import deque


def solution(bridge_length, weight, truck_weights):
    t = 1
    cur_weight = 0
    q = deque()
    for truck_weight in truck_weights:
        # 추가 불가능 => 첫 트럭이 빠질때까지
        while cur_weight + truck_weight > weight:
            truck = q.popleft()
            for i in range(len(q)):
                q[i][1] -= truck[1]  # [truck_weight, bridge_length]
            t += truck[1]
            cur_weight -= truck[0]

        # 추가 가능 상태가 됨
        q.append([truck_weight, bridge_length])
        cur_weight += truck_weight
        # 1초 흐름
        if q[0][1] == 1:
            cur_weight -= q.popleft()[0]
        for i in range(len(q)):
            q[i][1] -= 1
        t += 1
    t += q[-1][1]  # 마지막 트럭이 빠져나오는데 걸리는 시간
    return t


bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
# bridge_length = 100
# weight = 100
# truck_weights = [10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length, weight, truck_weights))
