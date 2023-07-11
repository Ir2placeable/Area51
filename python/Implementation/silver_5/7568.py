# https://www.acmicpc.net/problem/7568

import sys

n = int(sys.stdin.readline())
people = []
for _ in range(n):
    people.append(list(map(lambda x: int(x), sys.stdin.readline().split())))


def isPig(spec):
    pig_param = 1
    for weight, height in people:
        if spec[0] < weight and spec[1] < height:
            pig_param += 1
    return pig_param


result = []
for person in people:
    result.append(isPig(person))
print(*result)