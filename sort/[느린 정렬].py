# O(N^2)
# 선택 정렬 - 인덱스 단위로 작은 값을 넣음
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_idx = i
    for j in range(i + 1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j
    array[min_idx], array[i] = array[i], array[min_idx]  # swap

print(array)

# 삽입 정렬 - 정렬된 영역으로의 삽입 (선택 정렬보단 빠름, 거의 정렬된 상태라면 매우 빠름)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):  # i부터 1까지 -1씩 감소
        if array[j] < array[j - 1]:  # 앞놈보다 작으면 swap
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)
