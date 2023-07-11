# 16208 : 귀찮음
# https://www.acmicpc.net/problem/16208

cost = 0
num_of_stick = int(input())
list_of_stick = list(map(lambda x: int(x), input().split(" ")))
total = sum(list_of_stick)

for stick in list_of_stick:
    cost += stick * (total - stick)
    total -= stick

print(cost)

