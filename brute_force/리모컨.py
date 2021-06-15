# 빠른 원 큐 풀이법: 극단적 예시를 먼저 들어놓고 구현해야 한다. 소잃고 외양간 고치기 x

def is_possible(channel, broken):
    if channel == 0:
        return -1 if broken[channel] else 1
    press = 0
    while channel > 0:
        press += 1
        if broken[channel % 10]:
            return -1
        channel //= 10
    return press


goal = int(input())
broken = [False] * 10
if input() != '0':  # 0일 경우 다음 읽을 것이 없다 -> EOF Exception
    for x in map(int, input().split()):
        broken[x] = True
# +,- 누르는 경우
ans = abs(goal - 100)
# 번호 누르는 경우
for channel in range(max(goal * 2 - 100, 100)):
    press = is_possible(channel, broken)
    if press != -1:
        ans = min(ans, press + abs(goal - channel))
print(ans)