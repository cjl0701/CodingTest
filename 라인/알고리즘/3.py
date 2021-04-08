# 최악의 경우를 상정: 최대한 만나지 않도록 들어오자마자 나간다.
def solution(enter, leave):
    sequence = []
    n = len(enter)
    idx = -1
    # 나갈 수 있으면 바로 나간다.
    for l in leave:
        # 나가려면 이미 들어와 있어야 한다.
        if not l in sequence:
            for i in range(idx + 1, n):
                sequence.append(enter[i])
                idx = i
                if enter[i] == l:
                    break
        sequence.append(l)

    # 들어와서 나갈 때 까지 만난 놈을 적는다
    answer = [0] * n
    for i in range(1, n + 1):
        start = False
        for x in sequence:
            if x == i:
                if not start:
                    start = True
                else:
                    break
            else:
                if start:
                    answer[i - 1] += 1
                    answer[x - 1] += 1
    for i in range(n):
        answer[i] = answer[i] // 2
    return answer


enter = [1, 3, 2]
leave = [1, 2, 3]
enter = [1, 4, 2, 3]
leave = [2, 1, 3, 4]
print(solution(enter, leave))
