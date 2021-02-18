# 정당성: 곱하기가 더하기보다 더 커진다

# 0, 1 앞 뒤에만 +
data = input()

result = int(data[0])
for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
