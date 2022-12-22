# 14247 : 나무 자르기
# https://www.acmicpc.net/problem/14247
import sys

n = int(sys.stdin.readline())
list1 = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))
list2 = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))

# total = 0
# for i in range(0, n):
#     print(list1, total)
#     val, idx = 0, 0
#     for j in range(0, n):
#         if val < list1[j]:
#             val = list1[j]
#             idx = j
#
#     list1[idx] = 0
#     total += val
#
#     for j in range(n):
#         list1[j] += list2[j]
#
# print(total)