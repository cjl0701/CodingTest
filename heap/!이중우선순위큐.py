# https://programmers.co.kr/learn/courses/30/lessons/42628
import heapq


# O(N^2).. 다시 풀자 O(NlogN)으로
def solution(operations):
    element = 0  # 동기화를 위한 원소 갯수 표시
    maxh = []  # 음수로 넣는다
    minh = []
    for op in operations:
        if op[0] == "D":
            if element > 0:  # 최대 삭제
                element -= 1
                if op[2] == '-':
                    heapq.heappop(minh)
                else:
                    heapq.heappop(maxh)
            if element == 0:
                maxh.clear()
                minh.clear()
        else:  # 추가
            num = int(op[2:])
            heapq.heappush(maxh, -num)
            heapq.heappush(minh, num)
            element += 1
    return [0, 0] if element == 0 else [-heapq.heappop(maxh), heapq.heappop(minh)]


"""
def solution(operations):
    min_h = []
    max_h = []
    for op in operations:
        if op[0] == "I":
            heapq.heappush(min_h, int(op[2:]))
            heapq.heappush(max_h, -1 * int(op[2:]))  # 최대힙을 만드려면 최소힙에 음수로 넣어야 됨
        elif min_h:
            if op[2] == '-':
                max_h.remove(-heapq.heappop(min_h))
            else:
                min_h.remove(-heapq.heappop(max_h))

    return [0, 0] if not min_h else [heapq.heappop(max_h) * -1, heapq.heappop(min_h)]
"""

""" remove하면 힙이 망가진다? 
    마지막 레벨에 위치하기도 하고, 삭제하면 빈칸이 아니라 당겨진다.
    삽입 시 맨 아래서 올라가며 위치를 잡고, 삭제 시 맨 위에서 내려가며 위치 잡는다. 그래서 괜찮다. """
