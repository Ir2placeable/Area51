# 13305 : 주유소
# https://www.acmicpc.net/problem/13305

cities = int(input())
roads = list(map(lambda x: int(x), input().split(" ")))
prices = list(map(lambda x: int(x), input().split(" ")))
cost = 0

now = 0
while now < cities-1:
    nex = now
    while nex < cities-1 and prices[now] <= prices[nex]:
        nex += 1

    temp_cost = 0
    for i in range(now, nex):
        temp_cost += roads[i]
    # print(temp_cost * prices[now])
    cost += temp_cost * prices[now]
    
    now = nex

print(cost)