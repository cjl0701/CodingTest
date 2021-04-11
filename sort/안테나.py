# BJ18310
n = int(input())
house = list(map(int, input().split()))
house.sort()
# 중간 값을 출력
print(house[(n - 1) // 2])  # 중간 인덱스이므로 n-1!
# 그림을 그려서 일반화하면 증명할 수 있다