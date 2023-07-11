# 2138 : 전구와 스위치
# https://www.acmicpc.net/problem/2138

import sys

n = int(sys.stdin.readline())
a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

original = []
target = []
for i in a:
    original.append(int(i))
for i in b:
    target.append(int(i))
# print(original)
# print(target)


def switch(bulbs, index):
    for i in range(max(0, index-1), min(n, index+2)):
        bulbs[i] = (bulbs[i] + 1) % 2


# not turn on the first switch
def case1():
    count = 0

    temp1 = original[:]
    temp2 = target[:]

    for i in range(1, n):
        if temp1[i-1] != temp2[i-1]:
            count += 1
            switch(temp1, i)

    if temp1[-1] != temp2[-1]:
        count = 100001
    return count

# turn on the first switch
def case2():
    count = 1

    temp1 = original[:]
    temp2 = target[:]
    switch(temp1, 0)

    for i in range(1, n):
        if temp1[i-1] != temp2[i-1]:
            count += 1
            switch(temp1, i)

    if temp1[-1] != temp2[-1]:
        count = 100001

    return count


result = min(case1(), case2())
if result == 100001:
    print(-1)
else:
    print(result)