# 뒤집기 https://www.acmicpc.net/problem/1439
# 정당성: 전체 뒤집기는 의미 없다. {000111}00 뒤집기도 의미 없다. 연속적 {000} or {111} 단위만 의미 있다.
data = input()
count0, count1 = 0, 0
# 첫 글자 처리
if data[0] == '1':
    count1 += 1
else:
    count0 += 1

# 두번째 부터 끝까지
for i in range(len(data) - 1):
    # 연속성 깨질 경우 count
    if data[i + 1] != data[i]:
        if data[i + 1] == '1':
            count1 += 1
        else:
            count0 += 1

print(min(count0, count1))
