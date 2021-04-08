def solution(table, languages, preference):
    table = [t.split() for t in table]
    # 총 점수 리스트 초기화
    score = [['SI', 0], ['CONTENTS', 0], ['HARDWARE', 0], ['PORTAL', 0], ['GAME', 0]]
    # 선호도 딕셔너리 초기화
    prefer_dict = {'JAVA': 0, 'JAVASCRIPT': 0, 'C': 0, 'C++': 0, 'C#': 0, 'SQL': 0, "PYTHON": 0, "KOTLIN": 0, "PHP": 0}
    for i in range(len(languages)):
        prefer_dict[languages[i]] = preference[i]
    # 테이블 순회하며 총 점수 매기기
    idx = 0
    for t in table:
        sum = 0
        for i in range(1, 6):
            lang, point = t[i], 6 - i
            sum += prefer_dict[lang] * point
        score[idx][1] = sum
        idx += 1
    print(score)
    score.sort(key=lambda tp: (-tp[1], tp[0]))
    print(score)
    return score[0][0]


table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
         "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
         "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]
print(solution(table, languages, preference))
