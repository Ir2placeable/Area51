# 2891 : 카약과 강풍
# https://www.acmicpc.net/problem/2891

# 출발할 수 없는 팀의 수 출력
# 앞, 뒤 팀에만 빌려줄 수 있음

teams, broken_teams, spare_teams = map(lambda x: int(x), input().split(" "))
broken_list = list(map(lambda x: int(x), input().split(" ")))
spare_list = list(map(lambda x: int(x), input().split(" ")))
broken_list.sort()
spare_list.sort()

boats = []
for i in range(0, teams+2):
    boats.append(1)
for i in broken_list:
    boats[i] -= 1
for i in spare_list:
    boats[i] += 1

no = 0
for i in range(1, teams+1):
    if boats[i] == 0:
        if boats[i-1] == 2:
            boats[i-1] -= 1
            boats[i] += 1
        elif boats[i+1] == 2:
            boats[i+1] -= 1
            boats[i] += 1
        else:
            no += 1

print(no)