# def solution(lottos, win_nums):
#     # 당첨 번호 표시
#     win_table = [False] * 46
#     for num in win_nums:
#         win_table[num] = True
#
#     # 맞은 갯수가 최소, 0을 모두 맞은 수로 바꾸면 최대
#     cnt = zero = 0
#     for num in lottos:
#         if num == 0:
#             zero += 1
#         elif win_table[num]:
#             cnt += 1
#     answer = []
#     for hit in (7 - cnt - zero, 7 - cnt):
#         answer.append(hit if hit < 7 else 6)
#     return answer

def solution(lottos, win_nums):
    # 당첨 번호 표시
    win_table = [False] * 46
    for num in win_nums:
        win_table[num] = True

    # 맞은 갯수가 최소, 0을 모두 맞은 수로 바꾸면 최대
    min = max = 0
    for num in lottos:
        if num == 0:
            max += 1
        elif win_table[num]:
            min += 1
    answer = []
    max += min

    # 순위 표시
    for hit in (max, min):
        ranking = 7 - hit
        answer.append(ranking if ranking < 7 else 6)
    return answer


# lottos = [44, 1, 0, 0, 31, 25]
# win_nums = [31, 10, 45, 1, 6, 19]
lottos = [0, 0, 0, 0, 0, 0]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))
