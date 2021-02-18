data = input()
row = ord(data[0]) - ord("a") + 1  # 문자열->아스키코드
col = int(data[1])

# 방향 벡터 정의 - 2가지 방법
steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
# dx = [-2, -2, -1, -1, 1, 1, 2, 2]
# dy = [-1, 1, -2, 2, -2, 2, -1, 1]

count = 0
for step in steps:
    nx, ny = row + step[0], col + step[1]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1
print(count)
