# 14247 : 나무 자르기
# https://www.acmicpc.net/problem/14247
import sys

n = int(sys.stdin.readline())
list1 = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))
list2 = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))

list3 = list(map(lambda a, b : [a, b], list1, list2))
list3 = sorted(list3, key=lambda x: x[1])
# print(list3)

total = 0
for i in range(0, n):
    total += list3[i][0] + list3[i][1]*i

print(total)