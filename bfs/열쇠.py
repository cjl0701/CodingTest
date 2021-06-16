# https://www.acmicpc.net/problem/9328
from collections import deque

dx = (0, 0, -1, 1)
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
    wait_qs = [deque() for _ in range(ord('Z') - ord('A') + 1)]
    check[0][0] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < h and 0 <= ny < w and not check[nx][ny] and a[nx][ny] != '*':
                check[nx][ny] = True
                ch = a[nx][ny]
                if 'a' <= ch <= 'z' and ch not in keys:
                    keys.add(ch)
                    q.extend(wait_qs[ord(ch) - ord('a')])  # 비우지 않아도 ㄱㅊ
                elif 'A' <= ch <= 'Z':
                    if ch.lower() not in keys:
                        wait_qs[ord(ch) - ord('A')].append((nx, ny))
                        continue
                elif ch == '$':
                    ans += 1
                q.append((nx, ny))
    print(ans)
