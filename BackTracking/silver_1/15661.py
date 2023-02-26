# # https://www.acmicpc.net/problem/15661
# import sys
#
#
# def backTracking(teamA, teamB, index):
#
#
# n = int(sys.stdin.readline())
# getStats = [list(map(lambda x: int(x), sys.stdin.readline().split())) for _ in range(n)]
# players = [i for i in range(n)]
#
# result = sys.maxsize
# temp = 0
# for i in range(n):
#     for j in range(i, n):
#         temp += getStats[i][j] + getStats[j][i]
# backTracking(0, 0, 0)
# print(result)