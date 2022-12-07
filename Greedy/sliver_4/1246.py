# 1246 : 온라인 판매
# https://www.acmicpc.net/problem/1246

eggs, customers = map(lambda x: int(x), input().split(" "))

cost_list = []
for i in range(0, customers):
    cost_list.append(int(input()))
cost_list.sort()

max_revenue = 0
cost = 0

for i in range(0, customers):
    potential_customers = 0
    for j in range(i, customers):
        if cost_list[j] >= cost_list[i] :
            potential_customers += 1
        else:
            break

    potential_customers = min(potential_customers, eggs)
    if max_revenue < cost_list[i] * potential_customers:
        max_revenue = cost_list[i] * potential_customers
        cost = cost_list[i]

print(cost, max_revenue)