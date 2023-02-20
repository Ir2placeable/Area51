# https://www.acmicpc.net/problem/3758
import sys

for _ in range(int(input())):
    teams, problems, target, logs = map(lambda x: int(x), sys.stdin.readline().split())
    log_list = [list(map(lambda x: int(x), sys.stdin.readline().split())) for i in range(logs)]

    # team_id / count / score_list / last_time
    teams = [[i+1, 0, [0 for i in range(problems)], 0] for i in range(teams)]

    time = 0
    for team_id, problem_id, score in log_list:
        teams[team_id - 1][1] += 1
        teams[team_id - 1][2][problem_id - 1] = max(teams[team_id - 1][2][problem_id - 1], score)
        teams[team_id - 1][3] = time
        time += 1

    for i in range(len(teams)):
        teams[i][2] = sum(teams[i][2])
    teams.sort(key=lambda x: (-x[2], x[1], x[3]))

    for i in range(len(teams)):
        if teams[i][0] == target:
            print(i+1)
            break
