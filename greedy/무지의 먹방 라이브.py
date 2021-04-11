# https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3
# 인덱스 등이 복잡해서 생각할게 많음 => 시간이 오래 걸리고 틀리게 된다.
# => 적절한 자료구조를 생각했어야 했다!!!!!!!!!!!!
import heapq

food_times = [3, 1, 2]
k = 5


# 처음 생각: 아이디어는 같으나 매번 빼줬다. => O(N^2)
# 두번째 생각: 리스트를 이용해 직접 빼주지 않고 차이로 갯수를 셋다. O(N)이나 인덱스가 복잡해 실수
# 세번째 답: 인덱스가 복잡하지 않도록 heapq 자료구조 도입
def solution(food_times, k):
    # k초 후에 섭취해야 할 음식이 없다면 -1
    if sum(food_times) <= k:
        return -1
    # 가장 작은 음식부터 빼고 시간을 센다
    # 이를 위해 최소힙을 만든다.
    h = []
    for i, v in enumerate(food_times):
        heapq.heappush(h, (v, i + 1))  # v가 우선순위 기준
    t = 0  # 먹기 위해 사용한 시간
    previous = 0  # 직전에 다 먹은 음식 시간
    while t + (h[0][0] - previous) * len(h) <= k:
        t += (h[0][0] - previous) * len(h)
        previous = heapq.heappop(h)[0]
    # 남은 음식을 0으로 만들지 못하니 다 세면 된다.
    h.sort(key=lambda x: x[1])  # 음식 번호 기준으로 정렬
    rest = (k - t) % len(h)  # 남은 음식 중에서 몇 번째 음식인지 확인
    return h[rest][1]


print(solution(food_times, k))