# https://www.acmicpc.net/problem/15661
import sys


def backTracking(count, index):
    global result

    if 0 < count < n:
        teamA, teamB = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] == 1 and visited[j] == 1:
                    teamA += getStats[i][j]
                elif visited[i] == 0 and visited[j] == 0:
                    teamB += getStats[i][j]
                    
        result = min(result, abs(teamA - teamB))

    for i in range(index, n):
        if visited[i] == 1:
            continue
            
        visited[i] = 1
        backTracking(count + 1, i + 1)
        visited[i] = 0


n = int(sys.stdin.readline())
getStats = [list(map(lambda x: int(x), sys.stdin.readline().split())) for _ in range(n)]
players = [i for i in range(n)]
visited = [i for i in range(n)]

result = sys.maxsize
backTracking(0, 0)
print(result)