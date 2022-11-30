# 2891 : 카약과 강풍
# https://www.acmicpc.net/problem/2891

# 출발할 수 없는 팀의 수 출력

stop_teams = 0
teams, broken_teams, spare_teams = map(lambda x: int(x), input().split(" "))
broken_teams_list = list(map(lambda x: int(x), input().split(" ")))
spare_teams_list = list(map(lambda x: int(x), input().split(" ")))

