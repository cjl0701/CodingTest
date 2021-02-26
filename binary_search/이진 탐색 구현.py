# 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 탐색 O(log2 N)
# 이진 탐색은 시작점, 끝점, 중간점을 이용해 탐색 범위를 설정

def binary_search_loop(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


n, target = 10, 6
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
array.sort()  # 리스트가 정렬되어 있어야 이진 탐색이 가능하다
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print("인덱스", result)
