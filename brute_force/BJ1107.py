# 리모컨
# 배울 점 0: 재귀 설계부터 -> 애매하면 반복문
# 배울 점 1: 화끈하게 최대 범위 다 돌려버리면 쉽다.
# 배울 점 2: 예외 처리 일반화하기
# 고칠 점: 하나의 예외를 위해 예외 판단을 매번 하는걸 두려워 말자. 그걸 피하려다 틀린다.
""" 틀린 이유: 반례가 너무 많다
    => 새로운 로직(성급한 일반화인 경우) or 예외 처리
    *예외 처리 실패 이유
    1. 예외 처리가 복잡해서 방황
    2. 예외 처리 일반화 못함.. 로직에 녹여야 한다. """

# 재귀 설계
# 탈출 조건: x자리 ->x+1자리
# 성공: x자리 -> (x-1,x,x+1) 자리
# 연산: 고장나지 않았으면 누름
# 반환: x
# 예외 : 000=0..자릿수만 차지..
# 재귀가 애매하다 -> 반복문
# 어디까지 반복? 1,000,000-100

n = int(input())
m = int(input())
broken = [False] * 10  # 0~9번
if m != 0:
    for x in map(int, input().split()):
        broken[x] = True
# +,-만 눌러 이동할 경우
ans = abs(n - 100)


# 채널로 이동 -> +,-만 누르기
def possible(ch):
    if ch == 0:
        return 0 if broken[0] else 1
    press = 0
    while ch > 0:
        if broken[ch % 10]:
            return 0
        ch //= 10
        press += 1
    return press


for ch in range(1000000 - 100):
    press = possible(ch)
    if press > 0:
        ans = min(ans, abs(n - ch) + press)

print(ans)
