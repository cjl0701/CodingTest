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