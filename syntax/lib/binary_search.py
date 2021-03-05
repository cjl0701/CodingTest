# bisect_left(lower_bound): 정렬 순서를 유지하면서 배열에 x를 삽입할 가장 왼쪽 인덱스
# bisect_right(upper_bound): 정렬 순서를 유지하면서 배열에 x를 삽입할 가장 오른쪽 인덱스
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
print(bisect_left(a, 4))  # 4보다 크거나 같으면서 가장 작은 수
print(bisect_right(a, 4))  # 4보다 크면서 가장 작은 수
# [1, 2, (*)4, 4,(*) 8]

# 탐색 대상이 없을 때 반환값: 있어야할 위치의 왼쪽, 오른쪽 1,2,(*)4,4,8 -> 2/2
print(bisect_left(a, 3))  # 3보다 크거나 같으면서 가장 작은 수
print(bisect_right(a, 3))  # 3보다 크면서 가장 작은 수


# 활용: 값이 특정 범위에 속하는 데이터 갯수 구하기
def count_by_range(arr, left_value, right_value):
    upper_bound = bisect_right(arr, right_value)
    lower_bound = bisect_left(arr, left_value)
    return upper_bound - lower_bound


arr = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
arr.sort()
print(count_by_range(arr, 4, 4))
print(count_by_range(arr, -1, 3))
