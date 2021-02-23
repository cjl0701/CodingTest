from collections import deque

# 덱 사용법
deq = deque()
deq.append(4)  # 오른쪽 삽입
deq.appendleft(-1)
deq.pop()  # 오른쪽 삭제
deq.popleft()
# 기존 list 형태의 함수를 모두 지원
deq.extend([5, 6])
deq.extendleft([-2, -3])  # 왼쪽으로 차례대로 붙음
print(deq)  # deque([-3, -2, 5, 6])

# rotate, reverse 등 Linked List의 특성을 지원.
deq.rotate(2)  # 2칸 움직임
print(deq)  # deque([5, 6, -3, -2])
print(deque(reversed(deq)))  # deque([-2, -3, 6, 5])

# stack : list를 이용해 구현
a = [1, 2]
a.append(3)
a.append(4)
# 스택
print(a.pop())  # 4
print(a)  # [1, 2, 3]

# queue: deque을 이용해 구현. <-
# pop()은 O(1)이지만 pop(0)는 O(N)이므로. (list는 arraylist)
queue = deque([1, 2, 3])  # deque(iterable, [, maxlen])를 사용해 초기화
queue.append(4)  # 오른쪽 삽입
print(queue.popleft())  # 1
print(queue)  # deque([2, 3, 4])