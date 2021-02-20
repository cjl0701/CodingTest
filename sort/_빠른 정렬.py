# O(NlogN)
# 퀵 정렬 - 기준보다 큰 데이터와 작은 데이터의 위치를 바꿈 (최악의 경우 O(N^2)
def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:  # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[right], array[left] = array[left], array[right]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(array, 0, len(array) - 1)
print(array)


# 파이썬의 장점을 살린 방식
def quick_sort_py(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    # 분할 이우 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort_py(left_side) + [pivot] + quick_sort_py(right_side)


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print(quick_sort_py(array))

# 계수 정렬(Counting Sort) : 각각의 데이터가 총 몇 번 등장하는지 갯수를 센다. O(N+K)
# 데이터의 크기 범위가 제한(K)되어 정수 형태로 표현할 수 있을 때만 사용 가능
# 동일한 데이터가 여러 번 등장하며 데이터 범위가 크지 않을 때 효과적!

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)
for i in range(len(array)):
    count[array[i]] += 1

for idx in range(len(count)):
    for _ in range(count[idx]):
        print(idx, end=" ")
