# 공유기 설치
# 파라메트릭 서치: 최적화 문제를 여러번의 결정 문제로 바꿔 범위를 줄여나간다.
# 틀린 이유: 처음부터 접근을 잘못했는데, 안 떠올랐으면서도 그걸 못 버려. 의식적으로 버려보자.
n, c = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()
# 구하고자 하는 것 = 최적 길이: 큰 범위부터 좁혀나가보자.
start = 1  # 최소 길이
end = a[-1] - a[0]  # 최대 길이
optimal = 0

while start <= end:
    # 최적값: 최소~최대 길이 범위 사이인데. 중간보다 큰지 작은지 부터 보자
    mid = (start + end) // 2
    # 모든 지점을 돌아보며, 놓을 수 있으면 놓는다.
    previous = a[0]  # 첫 지점에는 무조건 놓는다.
    count = 1
    for i in range(n):
        if a[i] - previous >= mid:
            count += 1
            previous = a[i]
    # 더 많이 설치했다 => 길이를 늘려야 한다. 최소 현재 값보다는 크다
    if count >= c:
        start = mid + 1
        optimal = mid
    # 더 적게 설치했다 => 길이를 줄여야 한다. 현재 값보다는 작다
    else:
        end = mid - 1

print(optimal)
