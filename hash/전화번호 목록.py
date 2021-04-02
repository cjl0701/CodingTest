""" 하나만 찾으면 된다 => 옆만 비교 """


def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if len(phone_book[i]) <= len(phone_book[i + 1]):
            if hash(phone_book[i]) == hash(phone_book[i + 1][:len(phone_book[i])]):
                return False
    return True


# """ 파이썬 활용 """
# def solution(phone_book):
#     phone_book.sort()
#     for p1, p2 in zip(phone_book, phone_book[1:]): # zip: 병렬적으로 원소 꺼내옴(둘다 있어야)
#         if p2.startswith(p1):
#             return False
#     return True


phone_book = ["1230", "123", "1235", "567", "88"]
print(solution(phone_book))
