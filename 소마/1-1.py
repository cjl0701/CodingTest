# 연계 스킬, 순서 대로
# 연계 스킬들만 -> dfs
skills = list(input().split())
dict = {v: i for i, v in enumerate(skills)}  # 인접 리스트 생성을 위해 문자-숫자 맵핑
l = len(skills)
graph = [[] for _ in range(l)]
n = int(input())
solo = [True] * l  # 단독 스킬 여부
for _ in range(n):
    pre, post = input().split()
    graph[dict[pre]].append(post)
    solo[dict[post]] = False  # 후속 스킬은 단독 스킬이 아님


def dfs(graph, i, s):
    if graph[i]:
        for i in graph[i]:
            dfs(graph, dict[i], s + " " + i)
    else:  # 끝에 도달
        print(s)


for i, v in enumerate(skills):
    if graph[i] and solo[i]:  # 후속 스킬이 존재하고, 단독 스킬인 경우
        dfs(graph, i, v)
