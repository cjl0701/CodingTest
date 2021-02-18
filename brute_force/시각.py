# 파이썬: 1초에 약 2천만번
n = int(input())

count = 0
for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            # if '3' in (str(h), str(m), str(s)): 33, 30은 안 친다..!
            if '3' in str(h) + str(m) + str(s):  # 문자열 안에 3이 들어있나 확인하기 편함
                count += 1
print(count)
