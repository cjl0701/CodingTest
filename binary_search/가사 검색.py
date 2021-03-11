# https://programmers.co.kr/learn/courses/30/lessons/60060
from bisect import bisect_left, bisect_right

# 틀린 이유: 갯수에 따라 그 많은 배열을 만들 배짱이 없었다..
# 공통 코드 => 함수화
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

# 모든 단어를 길이마다 나눠 저장
arr = [[] for _ in range(100001)]
reversed_arr = [[] for _ in range(100001)]


def count_by_range(arr, start, end):
    return bisect_right(arr, end) - bisect_left(arr, start)


def solution(words, queries):
    for word in words:
        arr[len(word)].append(word)
        reversed_arr[len(word)].append(word[::-1])

    # 이진 탐색을 수행하기 위해 각 단어 리스트 정렬
    for i in range(2, 100001):
        arr[i].sort()
        reversed_arr[i].sort()

    answer = []
    for query in queries:
        if query[-1] == '?':
            res = count_by_range(arr[len(query)], query.replace('?', 'a'), query.replace('?', 'z'))
        else:
            res = count_by_range(reversed_arr[len(query)], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z'))
        answer.append(res)
    return answer


print(solution(words, queries))

""" 길이 별로 배열을 나누지 않아서 처리하기 복잡했다. 결국 에러.. 머리 아프면 결국 틀린다.
def solution(words, queries):
    n = len(words)
    words.sort()
    words_reverse = [w[::-1] for w in words]
    words_reverse.sort()

    answer = []
    for query in queries:
        length = len(query)
        cnt = 0
        if query[-1] == '?':
            l = bisect_left(words, query.replace('?', ''))
            r = bisect_right(words, query.replace('?', 'z'))
            for i in range(l, r):
                if len(words[i]) == length:
                    cnt += 1
        else:
            query = query[::-1]
            l = bisect_left(words_reverse, query.replace('?', ''))
            r = bisect_right(words_reverse, query.replace('?', 'z'))
            for i in range(l, r):
                if len(words_reverse[i]) == length:
                    cnt += 1
        answer.append(cnt)
    return answer
"""
