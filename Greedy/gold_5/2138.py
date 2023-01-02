# 2138 : 전구와 스위치
# https://www.acmicpc.net/problem/2138

# 스위치는 누르면 본인과 양쪽 전구의 전원이 켜지거나 꺼진다.
# 이런 문제는 규칙을 찾아야 한다.
# 모든 전구를 순회해야 한다. -> O(n) = n
#
# import sys
#
# n = int(sys.stdin.readline())
# original = sys.stdin.readline().rstrip()
# target = sys.stdin.readline().rstrip()
#
#
# # 첫 전구를 켤 때
# def case1():
#     count = 1
#     light0 = str((int(original[0]) + 1) % 2)
#     light1 = str((int(original[1]) + 1) % 2)
#
#     for i in range(1, n):
#         if original[i-1] != target[i-1]:
#             count += 1
#             light0 = str((int(original[i-1]) + 1) % 2)
#             light1 = str((int(original[i]) + 1) % 2)
#         else:
#             light0 = original[i]
#             light1 =
#     return count
#
#
# # 첫 전구를 켜지 않을 때
# def case2():
#     count = 0
#     light0 = original[0]
#     light1 = original[1]
#
#     for i in range(1, n):
#         if original[i-1] != target[i-1]:
#             count += 1
#             light0 = str((int(original[i-1]) + 1) % 2)
#             light1 = str((int(original[i]) + 1) % 2)
#     return count
#
# print(case1(), case2())