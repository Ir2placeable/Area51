# https://www.acmicpc.net/problem/14889
import sys


def backTracking(count, index):
    global result

    if count == max_player:
        teamA, teamB = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    teamA += stats[i][j]
                elif not visited[i] and not visited[j]:
                    teamB += stats[i][j]

        result = min(result, abs(teamA - teamB))
        return

    for i in range(index, n):
        if visited[i] == 1:
            continue

        visited[i] = 1
        backTracking(count + 1, i + 1)
        visited[i] = 0


n = int(sys.stdin.readline())
stats = [list(map(lambda x: int(x), sys.stdin.readline().split())) for _ in range(n)]

max_player = n // 2
visited = [0 for _ in range(n)]

result = sys.maxsize
backTracking(0, 0)
print(result)