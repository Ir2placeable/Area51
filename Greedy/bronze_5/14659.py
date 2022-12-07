# 14659 : 한조서열정리하고옴ㅋㅋ
# https://www.acmicpc.net/problem/14659

archers = int(input())
height_list = list(map(lambda ele: int(ele), input().split(" ")))

max_kills = 0
for i in range(0, archers):
    kills = 0

    for j in range(i+1, archers):
        if height_list[i] > height_list[j]:
            kills += 1
        else:
            break

    max_kills = max(max_kills, kills)

    if max_kills > archers//2:
        break

print(max_kills)