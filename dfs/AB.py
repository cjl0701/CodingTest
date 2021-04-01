# BJ 12970
# dfs를 이용한 풀이 ver. 기타 ver도 있음.
n, k = map(int, input().split())
check = [[[False] * (n * (n - 1) // 2 + 1) for _ in range(n + 1)] for _ in range(n + 1)]


def go(i, a, cnt):
    if i == n:
        return True if cnt == k else False

    if not check[i][a][cnt]: # 같은 상황인 경우 중복 연산 막기
        check[i][a][cnt] = True

        global ans
        # A 추가
        if go(i + 1, a + 1, cnt):
            ans = 'A' + ans
            return True
        # B 추가
        if go(i + 1, a, cnt + a):
            ans = 'B' + ans
            return True
    return False


ans = ""
print(ans if go(0, 0, 0) else -1)
