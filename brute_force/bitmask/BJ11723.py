# 집합

import sys

n = 21
m = int(sys.stdin.readline())
s = 0
for _ in range(m):
    op, *num = sys.stdin.readline().split()
    if len(num) > 0:
        x = int(num[0])
    if op == 'add':
        s |= 1 << x
    elif op == 'remove':
        s &= ~(1 << x)
    elif op == 'check':
        if (s & 1 << x) > 0:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
    elif op == 'toggle':
        s ^= 1 << x
    elif op == 'all':
        s = (1 << n) - 1
    elif op == 'empty':
        s = 0
