# BJ 2916
""" 주어진 예제로 깊이있게 고민 + 주어지지 않은 극단적인 값으로 고민
    틀린 이유
    문제에 대한 '고찰' 부족. 그대로 받아들일 것이 아니라 생각 필요
    |30-70|만 고려. -40 => 320으로 바꿀 생각을 못 함..
 """

# 어려운 지점: 새로운 값이 추가되면 base가 달라지는데? => 추가해서 반영하면 된다!
n, k = map(int, input().split())
base = list(map(int, input().split()))
# 가능한 각을 모두 구한다.
d = [False] * 360
# 모든 새로운 각은 base를 기반으로 한다
d[0] = True
for b in base:  # 새로 추가된 원소가 반영된다
    for x in range(360):
        if d[x]:
            for new in [(b + x) % 360, (b - x + 360) % 360]:
                if not d[new]:
                    d[new] = True
                    base.append(new)
# 정답 출력
for x in map(int, input().split()):
    print("YES" if d[x] else "NO")

# n, k = map(int, input().split())
# prev = list(map(int, input().split()))
# degree = list(map(int, input().split()))
# table = [False] * 361
# for p in prev:
#     table[p] = True
#
# next = []
# while True:
#     for i in range(len(prev)):
#         for j in range(len(prev)):
#             for num in ((prev[i] + prev[j]) % 360, (prev[i] - prev[j] + 360) % 360):
#                 if not table[num]:
#                     table[num] = True
#                     next.append(num)
#     if next:
#         prev += next
#         next = []
#     else:
#         break
# for d in degree:
#     print("YES" if table[d] else "NO")
