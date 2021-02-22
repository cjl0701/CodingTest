# 카잉 달력 https://www.acmicpc.net/problem/6064
# 년도가 MN일 때 끝. 전체를 완전 탐색하면 O(MN)이 걸려 너무 큼
# 규칙 찾기 -> M칸씩 건너뛸 수 있다! O(N)
t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    # 나눠 떨어지는 경우 0이되므로, -1한 것을 나누고 1을 더한다
    x -= 1
    y -= 1
    year = x  # x->mx->m2x->m3x->.. 일때 y가 일치하는가
    while year < m * n:
        if year % n == y:  # -1 했으므로 year일 때 일치한다면
            print(year + 1)  # year+1이 정답
            break
        year += m
    else:  # break로 탈출 시엔 안 먹힘
        print(-1)
