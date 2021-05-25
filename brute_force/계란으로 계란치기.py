# 경우의수 제대로 계산해라. 그 과정이 코드로 그대로 구현되는 경우가 많다.  (n-1)^n
# https://www.acmicpc.net/problem/16987
"""
각 계란의 내구도는 상대 계란의 무게만큼 깎이게 된다
왼쪽부터 차례로 들어서 한 번씩만 다른 계란을 쳐 최대한 많은 계란을 깨

1. 가장 왼쪽의 계란을 든다.
2. 손에 들고 있는 계란으로 깨지지 않은 다른 계란 중에서 하나를 친다.
단, 손에 든 계란이 깨졌거나 깨지지 않은 다른 계란이 없으면 치지 않고 넘어간다.
3. 이후 손에 든 계란을 원래 자리에 내려놓는다.
4. 가장 최근에 든 계란의 한 칸 오른쪽 계란을 손에 들고 2번 과정을 다시 진행한다.
단, 가장 최근에 든 계란이 가장 오른쪽에 위치한 계란일 경우 계란을 치는 과정을 종료한다.
"""
n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]

"""
전역변수 쓰지 않고 그냥 끝에서 구한 값을 리턴해줘도 된다
n이 작으니까 그냥 cnt를 맨 끝에서 직접 구해도 된다
탈출 조건을 2가지 경우로 처리해도 되지만, 다음으로 진행하지 않을 경우를 위한 flag를 둬도 된다.
"""
def go(eggs, idx, left, cnt):
    if idx == n or left <= 1:
        global ans
        ans = max(ans, cnt)
        return
    if eggs[idx][0] <= 0:
        go(eggs, idx + 1, left, cnt)
    else:
        for i in range(n):
            if i == idx:
                continue
            if eggs[i][0] > 0:
                eggs[idx][0] -= eggs[i][1]
                eggs[i][0] -= eggs[idx][1]
                broken = 0
                if eggs[idx][0] <= 0:
                    broken += 1
                if eggs[i][0] <= 0:
                    broken += 1
                go(eggs, idx + 1, left - broken, cnt + broken)
                eggs[idx][0] += eggs[i][1]
                eggs[i][0] += eggs[idx][1]


ans = 0
go(eggs, 0, n, 0)
print(ans)
