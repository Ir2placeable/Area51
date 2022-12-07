# 14487 : 욱제는 효도쟁이야!!
# https://www.acmicpc.net/problem/14487

# 가장 중요한 것은, 비싼 비용을 빼면 된다는 것이다.
num_of_towns = int(input())

cost_of_towns = list(map(lambda x: int(x), input().split(" ")))
cost_of_towns.sort()

min_cost = 0
for i in range(0, len(cost_of_towns)-1):
    min_cost += cost_of_towns[i]

print(min_cost)