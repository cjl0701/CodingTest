# 열쇠 https://www.acmicpc.net/problem/9328
from collections import deque

dx = (0, 0, -1, 1)  # 매번 쓰이므로
dy = (1, -1, 0, 0)

t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    # 패딩
    a = ['.' + input() + '.' for _ in range(h)]  # str 일차원 배열
    h += 2
    w += 2
    a = ['.' * w] + a + ['.' * w]  # 리스트 원소 합치기
    keys = set(input())  # {'0'} or {'a','b',,}
    """ 파이썬다운 코드로 대체 
    파이썬은 인덱스로 접근하는 것만큼 집합의 'in' 키워드로 접근하는게 편리
    temp = input()
    keys = [False] * (ord('z') - ord('a') + 1)
    if temp != '0':
        for key in temp:
            keys[ord(key) - ord('a')] = True
    """
    ans = 0
    check = [[False] * w for _ in range(h)]
    q = deque()
    q.append((0, 0))
    waitingQ = [deque() for _ in range(ord('Z') - ord('A') + 1)]
    check[0][0] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if not (0 <= nx < h and 0 <= ny < w):
                continue
            c = a[nx][ny]
            if c == '*' or check[nx][ny]:
                continue
            check[nx][ny] = True

            if c == '$':
                ans += 1
            elif 'A' <= c <= 'Z':  # 문
                if not c.lower() in keys:  # 열쇠 없으면 대기
                    waitingQ[ord(c) - ord('A')].append((nx, ny))
                    continue
            elif 'a' <= c <= 'z':  # 열쇠에 해당하는 문에 대기중인 것을 진행 큐로
                if c not in keys:
                    keys.add(c)
                    q.extend(waitingQ[ord(c) - ord('a')]) # 비우지 않아도 ㄱㅊ
                """ set을 활용한 코드로 대체
                keys[ord(c) - ord('a')] = True
                while waitingQ[ord(c) - ord('a')]:
                    q.append(waitingQ[ord(c) - ord('a')].popleft())
                """
            q.append((nx, ny))
    print(ans)
