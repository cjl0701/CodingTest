# https://programmers.co.kr/learn/courses/30/lessons/42883
"""틀린 이유
1. 시간 초과가 나면 시간 복잡도를 줄이려고 해라. O(N)으로 될까?
2. 그리디라고 스택, 힙 등 자료구조 안 쓰는건 아니다. 시간 복잡도를 줄이기 위해 필요.
"""
# 정당성: 앞 자리의 수가 큰 수가 큰 수이다.
# 앞에 큰 수를 유지하며 k개를 빼야한다.
def solution(number, k):
    stack=[number[0]]
    for num in number[1:]:
        # 앞에서부터 큰 수만 담아야 한다. 작은 수 k개를 뺀다.
        while k>0 and stack and stack[-1]<num:
            stack.pop()
            k-=1
        stack.append(num)

    return ''.join(stack[:len(stack)-k])