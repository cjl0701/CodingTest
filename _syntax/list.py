# 리스트 초기화
a = [1, 2, 3, 4]
a = []
a = list()  # []
a = [-1] * 10  # [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

# 인덱싱
a = [0, 1, 2, 3, 4, 5]
print(a[-2])  # 4

# 슬라이싱
print(a[0:4:2])  # [0, 2]

# 리스트 컴프리헨션: 대괄호 안에 조건문과 반복문을 적용하여 리스트 초기화
array = [i for i in range(10)]  # range(n) = [0:n]
print(array)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
array = [i * i for i in range(1, 10, 2)]
print(array)  # [1, 9, 25, 49, 81]

# n*m 크기의 이차원 배열을 초기화 할 때 유리
n = 4
m = 2
arr = [[-1] * m for _ in range(n)]
print(arr)  # [[-1, -1], [-1, -1], [-1, -1], [-1, -1]]

a = [1, 4, 3]
a.append(2)
a.sort(reverse=True)
print(a)  # [4, 3, 2, 1]
a.reverse()
print(a)  # [1, 2, 3, 4]
a.insert(1, 2)
print(a)  # [1, 2, 2, 3, 4]
print(a.count(2))  # 2

a.remove(2)  # 값이 2인 원소 하나만 제거됨
print(a)
# 특정 값을 가지는 원소를 모두 제거하기
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
# remove_set에 포됨되지 않는 값만을 저장
result = [i for i in a if i not in remove_set]
print(result) # [1, 2, 4]
