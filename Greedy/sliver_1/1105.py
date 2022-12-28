# 1105 : 팔
# https://www.acmicpc.net/problem/1105

# L에 포함된 8의 개수 중 몇 개나 줄일 수 있냐? 가 문제의 의도이다.
import sys

L, R = sys.stdin.readline().rstrip().split(" ")

list1 = []
for l in L:
    list1.append(l)

list2 = []
for r in R:
    list2.append(r)

# print(list1, list2)
if len(list1) != len(list2):
    print(0)
else:
    count = 0
    for i in range(0, len(list1)):
        if list1[i] != list2[i]:
            break

        if list1[i] == '8':
            count += 1

    print(count)