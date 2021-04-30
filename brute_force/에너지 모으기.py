# https://www.acmicpc.net/problem/16198
# 함수 개선. 굳이 매번 energy를 전달하고 유지할 필요x. 처음으로 모으면 됨
def getEnergy(marble):
    if len(marble) == 2:
        return 0
    ans = 0
    for i in range(1, len(marble) - 1):
        energy = marble[i - 1] * marble[i + 1] + getEnergy(marble[:i] + marble[i + 1:])
        ans = max(ans, energy)
    return ans


n = int(input())
marble = list(map(int, input().split()))
print(getEnergy(marble))
