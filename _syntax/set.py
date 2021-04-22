# 집합 자료형 초기화 1 : 문자열 or 리스트를 set()으로 초기화
l = [1, 1, 2, 2, 3]  # 중복 제거됨
data = set(l)  # {1, 2, 3}
# 집합 자료형 초기화 2
data = {1, 1, 2, 2, 3}  # set literal (리터럴:<->변수. 고정된 값. 고정된 값으로 표현한다는 것.)

# 집합 연산
a = set([1, 2, 3, 4, 5])
b = {3, 4, 5, 6, 7}
a | b  # {1, 2, 3, 4, 5, 6, 7}
a & b  # {3, 4, 5}
a - b  # {1, 2}
# a가 변경되진 않는다
print(a.union(b))  # {1, 2, 3, 4, 5, 6, 7}
print(a)  # {1, 2, 3, 4, 5}
a.intersection(b)
a.difference(b)

# 원소 조회, 추가 및 삭제 - O(1)
print(4 in data)  # False
data.add(4)
data.update([5, 6])  # 여러 개 추가
data.remove(3)  # 원소 3 삭제
data.clear()  # 비우기

# TypeError: unhashable type: 'list'
s = set()
arr = [1, 2]
s.add(arr.copy())  # set에 들어있는 값들은 해쉬 가능해야 한다. 문자열,숫자,튜플만 가능.
s.add(tuple(arr))  # 리스트가 아닌 hashable한 튜플을 넣어야 한다.
