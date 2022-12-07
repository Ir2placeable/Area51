# 14469 : 소가 길을 건너간 이유 3
# https://www.acmicpc.net/problem/14469

n = int(input())

item_list = []
# item_list[0] = 시작점
# item_list[1] = 종단점

for i in range(0, n):
    a, b = map(lambda x: int(x), input().split(" "))
    item_list.append([a, a+b])
item_list.sort()
# print(item_list)

over_time = 0
for i in range(0, n-1):
    if item_list[i][1] > item_list[i+1][0]:
        over_time = item_list[i][1] - item_list[i+1][0]
        item_list[i+1] = list(map(lambda x: x + over_time, item_list[i+1]))
print(item_list[-1][1])
# print(item_list)