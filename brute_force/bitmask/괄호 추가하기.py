"""
괄호를 적절히 추가해 최댓값 만들기
괄호 안에는 연산자가 하나만.
중첩 괄호 불가.
"""

"""틀린 이유 
엣지케이스 -> input 값이 아니라 result가 엣지일 수 있음.(초기값, 없는 값에 주의)
복잡할수록 예외 걸릴 확률이 높다. 특히 인덱스 복잡..
"""
from collections import deque

n = int(input())
m = 0
operator = list()
operand = list()
for op in input():
    if op.isdigit():
        operand.append(int(op))
    else:
        operator.append(op)
        m += 1
ans = operand[0] if n == 1 else None


def valid(bitmask, length, order):
    before = False
    for i in range(length):
        if (1 << i & bitmask) > 0:
            if before:
                return False
            else:
                before = True
                order.add(i)
        else:
            before = False
    return True


def operate(operator, operand, prio):
    operator_q = deque()
    operand_q = deque()
    i = 0
    while i < len(operator):
        if i in prio:
            if operator[i] == '+':
                operand_q.append(operand[i] + operand[i + 1])
            elif operator[i] == '-':
                operand_q.append(operand[i] - operand[i + 1])
            elif operator[i] == '*':
                operand_q.append(operand[i] * operand[i + 1])
            if i + 1 < len(operator):
                operator_q.append(operator[i + 1])
            i += 2
        else:
            operand_q.append(operand[i])
            operator_q.append(operator[i])
            i += 1
    if i == len(operator):
        operand_q.append(operand[i])
    ret = operand_q.popleft()
    while operand_q:
        op = operator_q.popleft()
        if op == '+':
            ret += operand_q.popleft()
        elif op == '-':
            ret -= operand_q.popleft()
        elif op == '*':
            ret *= operand_q.popleft()
    return ret


for bm in range(1 << m):
    order = set()
    if valid(bm, m, order):
        result = operate(operator, operand, order)
        if ans is None or ans < result:
            ans = result
print(ans)
