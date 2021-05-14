# https://www.acmicpc.net/problem/16986
"""
'모든 경우'가 순열로 표현될 경우, 재귀보다 간단한 반복문으로 가능!
"""
def next_permutaion(a):
    i = len(a) - 1
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
    if i <= 0:  # 전부 내림차순: 최후 순열
        return False
    j = len(a) - 1
    while a[j] <= a[i - 1]:  # 앞 놈(a[i-1])보다 다음으로 큰 수를 찾아 swap
        j -= 1
    a[i - 1], a[j] = a[j], a[i - 1]
    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True


n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
play = [[x for x in range(n)]]
for _ in range(2):
    play.append(list(map(lambda x: int(x) - 1, input().split())))

while True:
    index = [0, 0, 0]
    win = [0, 0, 0]
    p1, p2 = 0, 1
    while index[0] < n and win[1] < k and win[2] < k:
        if p1 > p2:
            p1, p2 = p2, p1
        result = a[play[p1][index[p1]]][play[p2][index[p2]]]
        index[p1] += 1
        index[p2] += 1
        if result == 2:
            win[p1] += 1
            p2 = 3 - p1 - p2
        else:
            win[p2] += 1
            p1 = 3 - p1 - p2
        if win[0] == k:
            print(1)
            exit(0)
    if not next_permutaion(play[0]):
        break
print(0)
