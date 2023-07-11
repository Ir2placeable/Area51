# 17070 : 파이프 옮기기 1
# https://www.acmicpc.net/problem/17070
import sys

# 가로 : 0 / 새로 : 1 / 대각선 : 2
n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(map(lambda x: int(x), sys.stdin.readline().split())))

# 가로, 세로, 대각선 총 3개의 경우가 있으므로, 각 위치 x, y 마다 3개의 공간을 준비해둔다.
dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]
# 첫 시작 위치는 항상 0, 0로 고정이다. 또한 해당 위치의 방향은 가로로 고정된다.
# dp 가로, 0, 1 은 1로 초기화한다.
dp[0][0][1] = 1

# DP 문제는 초기값이 필요하다.
for i in range(2, n):
    # 그래프에 벽이 없으면 -> 이동 경로를 dp에 추가
    if graph[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]

# 파이프의 종료 위치는 1,1 ~ n-1, n-1 이다.
for x in range(1, n):
    for y in range(1, n):
        # 대각선으로 이어지는 경우의 dp를 계산한다.
        if graph[x][y] == 0 and graph[x-1][y] == 0 and graph[x][y-1] == 0:
            dp[2][x][y] = dp[0][x-1][y-1] + dp[1][x-1][y-1] + dp[2][x-1][y-1]

        if graph[x][y] == 0:
            # 현재 위치가 가로에서 오는 경우
            dp[0][x][y] = dp[0][x][y - 1] + dp[2][x][y - 1]
            # 현재 위치가 세로에서 오는 경우
            dp[1][x][y] = dp[1][x - 1][y] + dp[2][x - 1][y]

print(sum(dp[i][n-1][n-1] for i in range(3)))