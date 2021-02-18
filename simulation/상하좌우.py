n = int(input())
x, y = 1, 1  # 한 줄에 초기화 가능
plans = input().split()

# R,L,U,D에 따른 이동 방향
move_types = ['R', 'L', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:  # 문자열 비교: ==
            nx = x + dx[i]  # 초기화 없이 바로 생성 가능
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n: continue
    x, y = nx, ny  # scope 기준은 함수!

print(x, y)
