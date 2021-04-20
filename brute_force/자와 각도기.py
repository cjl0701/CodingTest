# https://www.acmicpc.net/problem/2916
"""기준을 잡으면 중복을 줄일 수 있다."""
input()
base = list(map(int, input().split()))
know = [False] * 360
know[0] = True  # 자연스럽게 base 기록 가능
""" {모든 아는 각과 모든 아는 각 조합}은 너무 많다. 중복을 줄이자(순서를 부여한다던지)"""
# 아는 값(base)를 기준으로 모든 조합을 만들어보면 충분하다.
for b in base:
    # b로 가능한 모든 것 다 만들기
    for _ in range(360):  # 새로운 값이 1씩 증가하며 반영된다고 쳐도 한 바퀴 돌 수 있다.
        for x in range(360):
            if know[x]:
                know[(b + x) % 360] = know[(b - x + 360) % 360] = True

for num in map(int, input().split()):
    print("YES" if know[num] else "NO")
