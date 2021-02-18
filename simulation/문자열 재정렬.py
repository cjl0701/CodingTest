# 수: 정수
# 숫자: 0 ~ 9 글자
data = input()
result = []
sum = 0
for x in data:
    if x.isalpha():
        result.append(x)
    else:
        sum += int(x)
result.sort()
if sum != 0:  # 0을 붙이면 안되니까
    result.append(str(sum))
print("".join(result))  # 리스트->문자열
