# 오름차순 힙 정렬
import heapq


def heapsort_inc(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    while h:
        result.append(heapq.heappop(h))
    return result


# 최대힙을 이용하고 싶다면 부호를 바꿔 넣고 꺼낸 뒤 다시 바꾼다
def heapsort_dec(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    while h:
        result.append(-heapq.heappop(h))
    return result


print(heapsort_inc([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
print(heapsort_dec([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
