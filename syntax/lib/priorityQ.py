# 우선순위큐: 우선순위 높은 놈이 먼저 나온다. (default: 작은 값이 우선순위가 높다)
# push,pop: O(log n)
import heapq  # 일반 값을 넣으면 값을 기준으로 heap을 만들어 준다.
import queue  # Priority Queue 객체

h = []  # heap 자체인 list
heapq.heappush(h, 7)
heapq.heappush(h, 5)
heapq.heappush(h, 6)
print(h)  # [5, 7, 6]
print(heapq.heappop(h))  # 5
print(heapq.heappop(h))  # 6

# 튜플을 넣으면, 첫번째 요소는 우선순위 값, 두번째 요소는 데이터
h = []
heapq.heappush(h, (3, "ll"))
heapq.heappush(h, (4, "o"))
heapq.heappush(h, (1, "h"))
heapq.heappush(h, (2, "e"))
print(h)  # [(1, 'h'), (2, 'e'), (3, 'll'), (4, 'o')]
print(heapq.heappop(h))  # (1, 'h')
print(heapq.heappop(h))  # (2, 'e')
print(h)  # [(3, 'll'), (4, 'o')]

# 배열 자체를 힙으로 바꾸기 O(n)
h = [(3, "Go to home"), (10, "Do not study"), (1, "Enjoy!"), (4, "Eat!"), (7, "Pray!")]
heapq.heapify(h)
print(h)  # [(1, 'Enjoy!'), (4, 'Eat!'), (3, 'Go to home'), (10, 'Do not study'), (7, 'Pray!')]
arr = [4, 5, 2, 4, 1]
heapq.heapify(arr)
print(arr)  # [1, 4, 2, 4, 5]
print(heapq.heappop(arr))  # 1
print(heapq.heappop(arr))  # 2
print(arr)  # [4, 4, 5]

# 최대 힙: 키 값을 음수로 만든다.
h = [(3, "Go to home"), (10, "Do not study"), (1, "Enjoy!"), (4, "Eat!"), (7, "Pray!")]
max_h = [(-k, v) for k, v in h]
heapq.heapify(max_h)
print(max_h)  # [(-10, 'Do not study'), (-7, 'Pray!'), (-1, 'Enjoy!'), (-4, 'Eat!'), (-3, 'Go to home')]

"""queue.PriorityQueue : 리스트를 최소힙으로써 작동하게 하는 것이 아닌, 우선순위 큐 자체 생성"""
pq = queue.PriorityQueue()
pq2 = queue.PriorityQueue(maxsize=8)  # 최대 크기 8로 잡음

pq.put(2)
pq.put(1)
print(pq)  # <queue.PriorityQueue object at 0x0000024F841658E0>
print(pq.get())  # 1

pq2.put((2, "apple"))
pq2.put((0, "banana"))
print(pq2.get())  # (0, 'banana')
print(pq2.get()[1])  # apple
# iterable하지 않다. 그냥 get으로 하나하나 뺀다.
