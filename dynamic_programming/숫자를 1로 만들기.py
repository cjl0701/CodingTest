# d[i]: i를 1로 만드는 비용
# d[i]=min(d[i/5].d[i/3],d[i/2],d[i-1])+1
x = int(input())
d = [-1] * 30001


def f(x):
    if x <= 1:
        return 0
    if d[x] == -1:
        d[x] = f(x - 1)
        if x % 5 == 0:
            d[x] = min(d[x], f(x // 5))
        if x % 3 == 0:
            d[x] = min(d[x], f(x // 3))
        if x % 2 == 0:
            d[x] = min(d[x], f(x // 2))
        d[x] += 1
    return d[x]


print(f(x))
