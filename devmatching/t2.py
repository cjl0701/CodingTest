def rotate(arr, query):
    r1, c1, r2, c2 = query
    min_val = before = arr[r1][c1]
    # c1->c2
    for c in range(c1 + 1, c2 + 1):
        arr[r1][c], before = before, arr[r1][c]
        min_val = min(min_val, before)
    # r1->r2
    for r in range(r1 + 1, r2 + 1):
        arr[r][c2], before = before, arr[r][c2]
        min_val = min(min_val, before)
    # c1<-c2
    for c in range(c2 - 1, c1 - 1, -1):
        arr[r2][c], before = before, arr[r2][c]
        min_val = min(min_val, before)
    # r1<-r2
    for r in range(r2 - 1, r1 - 1, -1):
        arr[r][c1], before = before, arr[r][c1]
        min_val = min(min_val, before)
    return min_val


def solution(rows, columns, queries):
    # 배열을 만든다
    arr = [[0] * (rows + 1)]
    base = 0
    for _ in range(rows):
        arr.append([0] + [x + base for x in range(1, columns + 1)])
        base += columns

    # rotate 후 결과를 answe에 담는다
    answer = []
    for query in queries:
        answer.append(rotate(arr, query))
    return answer


rows = 3
columns = 3
queries = [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]
print(solution(rows, columns, queries))
