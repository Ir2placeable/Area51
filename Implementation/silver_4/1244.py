# https://www.acmicpc.net/problem/1244

import sys
n = int(sys.stdin.readline())
switches = [-1] + list(map(lambda x: int(x), sys.stdin.readline().split()))

m = int(sys.stdin.readline())
students = [] # 남 1, 여 2
for _ in range(m):
    students.append(list(map(lambda x: int(x), sys.stdin.readline().split())))


def boy(num):
    for k in range(num, n+1, num):
        switches[k] = (switches[k] + 1) % 2


def girl(num):
    switches[num] = (switches[num] + 1) % 2

    index = 1
    while 0 < num - index and num + index <= n and switches[num - index] == switches[num + index]:
        switches[num - index] = (switches[num - index] + 1) % 2
        switches[num + index] = (switches[num + index] + 1) % 2
        index += 1


for gender, number in students:
    if gender == 1: # 남자
        boy(number)
    else: # 여자
        girl(number)

switches.pop(0)
result = []
for i in range(0, n, 20):
    result.append(switches[i:i+20])

for temp in result:
    print(*temp)