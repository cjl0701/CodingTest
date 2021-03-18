# BJ 12970
# 명백하게 증명할 수 없으면 분명히 반례가 있다. 손대지 마라.
# 손으로 끄적여 보며 규칙 파악: 0<=갯수<=a*b
# skill: case 분류. case 마다 변화를 살핀다.
# skill: 하나를 고정해 놓고 생각한다.
# A 마다 앞의 B 갯수 => B를 고정시키고 A의 위치를 바꿔본다.
n, k = map(int, input().split())
# B 사이에 A를 놓아보는 방법
for a in range(1, n):
    b = n - a
    if k > a * b:  # 최대 갯수 넘으면
        continue
    cnt = [0] * (b + 1)
    for _ in range(a):
        x = min(k, b)
        cnt[x] += 1
        k -= x
    ans = ""
    for x in range(b, -1, -1):
        ans += "A" * cnt[x]
        if x > 0:
            ans += "B"
    print(ans)
    exit(0)
print(-1)
