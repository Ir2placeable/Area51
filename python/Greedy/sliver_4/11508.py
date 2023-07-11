# 11508 : 2+1 세일
# https://www.acmicpc.net/problem/11508

N = int(input())

item_list = []
for i in range(0, N):
    item_list.append(int(input()))
item_list.sort(reverse=True)

cost = 0
flag = 0
for item in item_list:
    if flag == 2:
        flag = 0
        continue
    cost += item
    flag += 1

print(cost)