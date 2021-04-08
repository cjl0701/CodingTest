# 추천인에게 상납
def pay(man, money, referral, answer, idx_table):
    # 수익 기록
    man_idx = idx_table[man]
    paid = int(money * 0.1)
    answer[man_idx] += (money - paid)

    # 상납
    referer = referral[man_idx]
    if referer != '-':
        pay(referer, paid, referral, answer, idx_table)


def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    # name-index mapping
    idx_table = {name: i for i, name in enumerate(enroll)}

    # 수익 발생 -> 상납
    for man, sell in zip(seller, amount):
        pay(man, sell * 100, referral, answer, idx_table)

    return answer


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]  # 부모
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))
