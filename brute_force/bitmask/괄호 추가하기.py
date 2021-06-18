"""
[틀린 이유]
엣지케이스 -> input 값이 아니라 result가 엣지일 수 있음.(초기값, 없는 값에 주의)
복잡할수록 예외 걸릴 확률이 높다. 특히 인덱스 복잡.. => 쉽게 계산하도록 꾀를 부리자!
[접근법]
괄호 => 먼저 계산한다.
먼저 계산할 것들을 정하고(비트마스크) 먼저 계산한다.
순차적으로 계산한다.
꾀: 계산상 편의를 위해 '먼저 계산한 결과', '+', '0'으로 치환한다.
"""


def operate(operand1, operand2, operator):
    if operator == '*':
        return operand1 * operand2
    elif operator == '+':
        return operand1 + operand2
    else:
        return operand1 - operand2


n = int(input())
m = (n - 1) // 2
expression = list(input())
for i in range(0, n, 2):
    expression[i] = int(expression[i])
ans = None
for bitmask in range(1 << m):
    # 먼저 계산할 것(괄호)를 정한다
    valid = True
    for i in range(m - 1):
        if bitmask & (1 << i) > 0 and bitmask & (1 << (i + 1)) > 0:
            valid = False
    # 먼저 계산한다
    if valid:
        ex = expression[:]
        for k in range(m):
            if bitmask & (1 << k) > 0:
                i = 2 * k + 1
                ex[i - 1] = operate(ex[i - 1], ex[i + 1], ex[i])
                ex[i] = '+'
                ex[i + 1] = 0
        # 최종 계산
        result = ex[0]
        for i in range(1, n, 2):
            result = operate(result, ex[i + 1], ex[i])
        if ans is None or ans < result:
            ans = result
print(ans)
