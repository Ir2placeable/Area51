# https://www.acmicpc.net/problem/15661
import sys


def getScoreDiff():
    global answer

    teamA, teamB = 0, 0
    for i in range(n):
        for j in range(n):
            if picked_players[i] and picked_players[j]:
                teamA += getStats[i][j]
            elif not picked_players[i] and not picked_players[j]:
                teamB += getStats[i][j]

    answer = min(answer, abs(teamA - teamB))
    return


def backTracking(index):
    if index == n:
        getScoreDiff()
        return

    # index 번 선수를 뽑는다.
    picked_players[index] = True
    backTracking(index + 1)
    # index 번 선수를 뽑기 취소한다.
    picked_players[index] = False
    backTracking(index + 1)


n = int(sys.stdin.readline())
getStats = [list(map(lambda x: int(x), sys.stdin.readline().split())) for _ in range(n)]
picked_players = [False for i in range(n)]

answer = sys.maxsize
backTracking(0)
print(answer)