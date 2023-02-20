# https://www.acmicpc.net/problem/9017

import sys
from collections import defaultdict

t = int(sys.stdin.readline())
for test_case in range(1, t + 1):
    n = int(sys.stdin.readline())
    members = list(map(lambda x: int(x), sys.stdin.readline().split()))

    team_members = defaultdict(int)
    for member in members:
        team_members[member] += 1

    score = 1
    # total_score, count, last_member_score, team_index
    teams = [[0, 0, 0, i] for i in range(len(team_members) + 1)]
    for member in members:
        if team_members[member] < 6:
            teams[member] = [1001, 1001, 1001, 0]
            continue
        if teams[member][1] < 4:
            teams[member][0] += score
            teams[member][1] += 1
        elif teams[member][1] == 4:
            teams[member][2] = score
            teams[member][1] += 1
        score += 1

    teams.sort(key=lambda x: (x[0], x[2]))
    print(teams[1][3])