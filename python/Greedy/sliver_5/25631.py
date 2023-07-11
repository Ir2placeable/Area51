# 25631 : 마트료시카
# https://www.acmicpc.net/problem/25631

N = int(input())
dolls = list(map(lambda x: int(x), input().split(" ")))

doll_list = {}
for doll in dolls:
    if doll in doll_list:
        doll_list[doll] += 1
    else:
        doll_list[doll] = 1

print(sorted(doll_list.items(), key=lambda x: x[1], reverse=True)[0][1])
