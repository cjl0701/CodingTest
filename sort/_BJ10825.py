# 국영수
n = int(input())
students = [list(input().split()) for _ in range(n)]
students.sort(key=lambda l: (-int(l[1]), int(l[2]), -int(l[3]), l[0]))
for student in students:
    print(student[0])

# a = [[[PriorityQueue() for _ in range(101)] for _ in range(101)] for _ in range(101)]
# for _ in range(n):
#     name, k, e, m = input().split()
#     a[int(k)][int(e)][int(m)].put((name.lower(), name))
#
# for k in range(100, 0, -1):
#     for m in range(1, 101):
#         for e in range(100, 0, -1):
#             while a[k][m][e]:
#                 print(a[k][m][e].get()[1])
#                 # sys.stdout.write(a[k][m][e].get()[1] + "\n")
