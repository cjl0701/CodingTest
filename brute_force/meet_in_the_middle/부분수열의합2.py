"""
완탐으로 모든 경우를 세면 너무 많다. O(2^40)
중복 계산이 많다. 미리 더해 둔 것을 써도 된다.
중간에서 만나기 => 탐색의 크기가 줄어든다
2^40은 너무 커 => 2^20, 2^20은 구할 수 있다.
반쪽짜리로 two pointers를 쓰든 이진 탐색을 쓰든 방법 수를 줄인다.
"""
n, s = map(int, input().split())
arr = list(map(int, input().split()))
m = n // 2
n -= m
sum1 = list()
sum2 = list()
for bitmask in range(1 << n):
    sum = 0
    for i in range(n):
        if (bitmask & (1 << i)) > 0:
            sum += arr[i]
    sum1.append(sum)
for bitmask in range(1 << m):
    sum = 0
    for i in range(m):
        if (bitmask & (1 << i)) > 0:
            sum += arr[n + i]
    sum2.append(sum)

sum1.sort()
sum2.sort(reverse=True)
idx1 = idx2 = cnt = 0
while idx1 < len(sum1) and idx2 < len(sum2):
    sum = sum1[idx1] + sum2[idx2]
    if sum < s:
        idx1 += 1
    elif sum > s:
        idx2 += 1
    else:
        i1, i2 = idx1, idx2
        while idx1 < len(sum1) and sum1[idx1] == sum1[i1]:
            idx1 += 1
        while idx2 < len(sum2) and sum2[idx2] == sum2[i2]:
            idx2 += 1
        cnt += (idx1 - i1) * (idx2 - i2)
if s == 0: # 예외 케이스: 문제에서 부분집합은 크기가 양수라고 했다 => 0개+0개=0인 경우는 제외
    cnt -= 1
print(cnt)

"""# 이진 탐색으로 구간 찾기
second.sort()
for f in first:
    ans += bisect_right(second, s - f) - bisect_left(second, s - f)
"""
