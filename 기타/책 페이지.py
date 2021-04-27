# https://www.acmicpc.net/problem/1019
# 넘 복잡, 0 예외 처리도.. -> 그럼 다른 규칙을 찾아야지. 왜 어려운 길로 dfs하냐고.. 접근이 어렵다 싶으면 멈춰
"""
규칙을 찾자 -> 세기 쉽게 덩어리로 묶자. 0~9로 끝나는 덩어리
1~N => A~B까지 세는 문제로.
끝이 0,9로 끝나도록 맞추고 그 전까지는 직접 갯수를 센다.
1의 자리부터 갯수를 구한다. 이후에는 고려x
"""



def count(n, ten):
    # for i in range(10): 끝 자리 수는 구하고 넘어왔으니 안구해도 됨..
    #     cnt[i] += ten // 10
    while n > 0:
        cnt[n % 10] += ten
        n //= 10


start, end, ten = 1, int(input()), 1
cnt = [0] * 10
# start~end 까지 숫자 갯수 세기. 0~9로 끝나면 쉽게 셀 수 있음!
while start <= end:
    while start % 10 != 0 and start <= end:
        count(start, ten)
        start += 1
    while end % 10 != 9 and start <= end:
        count(end, ten)
        end -= 1
    if start <= end:
        start //= 10
        end //= 10
        add = (end - start + 1) * ten
        for i in range(10):
            cnt[i] += add
        ten *= 10
print(' '.join(map(str, cnt)))

""" 검수 용
temp = [0] * 10
for i in range(1, end+1):
    while i > 0:
        temp[i % 10] += 1
        i //= 10

print(temp)
"""
