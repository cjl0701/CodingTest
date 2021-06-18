# https://www.acmicpc.net/problem/16939
from copy import deepcopy


def check(cube):
    for section in range(6):
        s = 4 * section + 1
        for i in range(1, 4):
            if cube[s] != cube[s + i]:
                return False
    return True


def spin(type, time, cube):
    a = deepcopy(cube)
    for _ in range(time):
        if type == 0:
            temp = a[1]
            a[1] = a[5]
            a[5] = a[9]
            a[9] = a[24]
            a[24] = temp
            temp = a[3]
            a[3] = a[7]
            a[7] = a[11]
            a[11] = a[22]
            a[22] = temp
        elif type == 1:
            temp = a[2]
            a[2] = a[6]
            a[6] = a[10]
            a[10] = a[23]
            a[23] = temp
            temp = a[4]
            a[4] = a[8]
            a[8] = a[12]
            a[12] = a[21]
            a[21] = temp
        elif type == 2:
            temp = a[13]
            a[13] = a[5]
            a[5] = a[17]
            a[17] = a[21]
            a[21] = temp
            temp = a[14]
            a[14] = a[6]
            a[6] = a[18]
            a[18] = a[22]
            a[22] = temp
        elif type == 3:
            temp = a[15]
            a[15] = a[7]
            a[7] = a[19]
            a[19] = a[23]
            a[23] = temp
            temp = a[16]
            a[16] = a[8]
            a[8] = a[20]
            a[20] = a[24]
            a[24] = temp
        elif type == 4:
            temp = a[3]
            a[3] = a[17]
            a[17] = a[10]
            a[10] = a[16]
            a[16] = temp
            temp = a[4]
            a[4] = a[19]
            a[19] = a[9]
            a[9] = a[14]
            a[14] = temp
        elif type == 5:
            temp = a[1]
            a[1] = a[18]
            a[18] = a[12]
            a[12] = a[15]
            a[15] = temp
            temp = a[2]
            a[2] = a[20]
            a[20] = a[11]
            a[11] = a[13]
            a[13] = temp
    return a


cube = [0] + list(map(int, input().split()))
for i in range(6):
    for time in (1, 3):
        if check(spin(i, time, cube)):
            print(1)
            exit(0)
print(0)
