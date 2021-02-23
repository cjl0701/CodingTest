# 가르침 https://www.acmicpc.net/problem/1062
# counter보다는 구성 원소 비교 등 방식이 범용적인 비트마스크 쓰자. 단순히 셀 때만 counter.
# 몇 개의 단어를 읽을 수 있는지 count
def count(mask):
    cnt = 0
    for word in words:
        if word & mask == word:
            cnt += 1
    return cnt

# 매개변수 전달 많이 하면 느려짐
def go(selected, idx, mask):
    if selected == k:
        return count(mask)
    if idx == ord('z') - ord('a') + 1:
        return 0

    # 학습
    ans = go(selected + 1, idx + 1, mask | (1 << idx))
    if idx not in essential:  # 필수가 아닐 경우 안 배우는 버전도 진행
        ret = go(selected, idx + 1, mask)
        if ret > ans:
            ans = ret
    return ans


n, k = map(int, input().split())
# word의 구성 원소만 알면된다. counter? bitmask?
words = [0] * n
for i in range(n):
    for c in input():
        words[i] |= (1 << (ord(c) - ord('a')))
essential = [ord(x) - ord('a') for x in ['a', 'c', 't', 'i', 'n']]
print(go(0, 0, 0))
