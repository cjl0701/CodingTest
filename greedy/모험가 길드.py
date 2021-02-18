# 정당성: 그룹 인원이 적어야 많은 그룹이 생성된다.
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

group = 0
member = 0

for i in arr:
    member += 1
    if i <= member:  # 공포도가 인원 수보다 작거나 같다면 그룹 결성 가능
        group += 1
        member = 0
print(group)
