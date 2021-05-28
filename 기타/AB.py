# https://www.acmicpc.net/problem/12970
"""
대원칙: 규칙을 활용한다.
skill: 답의 범위를 구한다.
- 범위: 0 ~ a*b
- 1씩 차이나므로 모든 수를 만들 수 있다
=> a*b==k인 것이 무조건 존재한다!
"""
import sys

n, k = map(int, input().split())
ans = ''
for b in range(n + 1):
    a = n - b
    if a * b < k:
        continue
    position = [0] * (b + 1)
    # a번 선택한다
    for _ in range(a):
        x = min(k, b)
        position[x] += 1
        k -= x
    # 출력 - 문자열 합치기보다 버퍼 출력이 빠르다?
    sys.stdout.write("A" * position[b])
    for i in range(b - 1, -1, -1):
        sys.stdout.write("B"+"A"*position[i])
    exit(0)
print(-1)