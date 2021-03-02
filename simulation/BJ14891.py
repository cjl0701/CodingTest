# 톱니바퀴
# ㅅㅂ.. no-1 안해서 / n>3이 아니라 n>=3이라 해서.. 틀림..

a = [list(input()) for _ in range(4)]
k = int(input())

for _ in range(k):
    no, dir = map(int, input().split())
    # '동시에' 회전하므로, 회전 가능한 것들을 구해놓고 한번에 회전
    no -= 1
    dirs = [0] * 4  # 0:회전x, 1:시계, -1:반시계
    dirs[no] = dir
    # 왼쪽
    for i in range(no - 1, -1, -1):
        if a[i][2] != a[i + 1][6]:
            dirs[i] = dirs[i + 1] * -1
        else:
            break
    # 오른쪽
    for i in range(no + 1, 4):
        if a[i - 1][2] != a[i][6]:
            dirs[i] = dirs[i - 1] * -1
        else:
            break
    # 동시에 회전
    for i in range(4):
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

ans = 0
for i in range(4):
    if a[i][0] == '1':
        ans |= (1 << i)  # 1,2,4,8 추가
print(ans)

"""
def rotate(n, rotation, left, right):
    # 회전 시키기 전에 기록
    l, r = a[n][6], a[n][2]

    # n 번째 톱니바퀴를 rotation 방향으로 회전시킨다.
    if rotation == 1:  # 시계 방향
        a[n] = list(a[n][7]) + a[n][:7]
    elif rotation == -1:
        a[n] = a[n][1:] + list(a[n][0])

    # 좌우를 회전시킨다.
    if left:
        if n - 1 >= 0 and l != a[n - 1][2]:
            rotate(n - 1, rotation * -1, True, False)
    if right:
        if n + 1 <= 3 and r != a[n + 1][6]:
            rotate(n + 1, rotation * -1, False, True)


for _ in range(k):
    no, dir = map(int, input().split())
    rotate(no - 1, dir, True, True)

ans = 0
point = 1
for i in range(4):
    if a[i][0] == '1':
        ans += point
    point *= 2
print(ans)
"""
