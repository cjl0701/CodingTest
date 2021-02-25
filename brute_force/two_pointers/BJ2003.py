# 모든 경우 다 해보기와 다르게 <절대 정답이 될 수 없는 경우>는 확인하지도 않을 수 있다.
# 수들의 합2 https://www.acmicpc.net/problem/2003
# 코드가 길어도 되니 최대한 아토믹하게 구현하자.. 그게 안전하고 덜 복잡하다.. 리팩토링은 나중에.
# 손으로 직접 풀어보면 구현 시 할 일을 빠뜨리지 않는다.
n, m = map(int, input().split())
arr = list(map(int, input().split()))
i = j = ans = 0
s = arr[j]
while i <= j < n:
    if s < m:
        j += 1
        if j < n:
            s += arr[j]
    elif s > m:
        s -= arr[i]
        i += 1
        if n > i > j:
            j = i
            s += arr[j]  # 손으로 구체적으로 풀어봤다면 알 수 있었을 것.
    elif s == m:
        ans += 1
        j += 1  # 아토믹하게. i 감소는 다음으로 미룬다!
        if j < n:  # 중복돼도 어쩔 수 없어 이런 거 신경쓰다 틀린다..
            s += arr[j]

print(ans)
