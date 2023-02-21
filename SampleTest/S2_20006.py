# https://www.acmicpc.net/problem/20006
import sys

total_players, max_players = map(lambda x: int(x), sys.stdin.readline().split())
# [ {tier : int, count: int, players: []} .... ]
waiting_queue = []

for _ in range(total_players):
    tier, nickname = sys.stdin.readline().split()
    tier = int(tier)

    isJoined = False
    for i in range(len(waiting_queue)):
        if waiting_queue[i]['count'] == max_players:
            continue

        if waiting_queue[i]['tier'] + 10 >= tier >= waiting_queue[i]['tier'] - 10:
            waiting_queue[i]['players'].append([tier, nickname])
            waiting_queue[i]['count'] += 1
            isJoined = True
            break

    if isJoined:
        continue
    waiting_queue.append({'tier' : tier, 'count': 1, 'players': [[tier, nickname]]})

for room in waiting_queue:
    if room['count'] == max_players:
        print('Started!')
    else:
        print('Waiting!')

    for player in sorted(room['players'], key=lambda x: x[1]):
        print(*player)