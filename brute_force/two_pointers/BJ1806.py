# 부분합
n, s = map(int, input().split())
a = list(map(int, input().split()))
ans = n + 1  # 최소 길이만 갱신하면 됐다..
left = right = 0
total = a[right]
while left <= right < n:
    if total <= s:
        if total == s:
            ans = min(ans, right - left + 1)
        right += 1
        if right < n:
            total += a[right]
    else:
        ans = min(ans, right - left + 1)
        total -= a[left]
        left += 1
        if n > left > right:
            right = left
            total += a[right]

print(ans if ans != n + 1 else 0)
