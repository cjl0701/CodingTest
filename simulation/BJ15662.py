# 톱니바퀴 2
n = int(input())
a = [list(input()) for _ in range(n)]
k = int(input())

for _ in range(k):
    no, dir = map(int, input().split())
    # '동시에' 회전하므로, 회전 가능한 것들을 구해놓고 한번에 회전
    no -= 1
    dirs = [0] * n  # 0:회전x, 1:시계, -1:반시계
    dirs[no] = dir
    # 왼쪽
    for i in range(no - 1, -1, -1):
        if a[i][2] != a[i + 1][6]:
            dirs[i] = dirs[i + 1] * -1
        else:
            break
    # 오른쪽
    for i in range(no + 1, n):
        if a[i - 1][2] != a[i][6]:
            dirs[i] = dirs[i - 1] * -1
        else:
            break
    # 동시에 회전
    for i in range(n):
        if dirs[i] == 1:  # 시계 방향
            temp = a[i][7]
            for j in range(7,0,-1):
                a[i][j] = a[i][j-1]
            a[i][0] = temp
        elif dirs[i] == -1:
            temp = a[i][0]
            for j in range(7):
                a[i][j] = a[i][j + 1]
            a[i][7] = temp

ans=0
for i in range(n):
    if a[i][0]=='1':
        ans+=1
print(ans)