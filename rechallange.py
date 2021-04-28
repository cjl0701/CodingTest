n, k = map(int, input().split())
d = [False] * 360
d[0] = True
for base in map(int, input().split()):
    for _ in range(360):  # 1씩 증가해도 한바퀴 다 돈다.
        for x in range(360):
            if d[x]:
                d[(base + x) % 360] = d[(base - x + 360) % 360] = True
for q in map(int, input().split()):
    print("YES" if d[q] else "NO")
