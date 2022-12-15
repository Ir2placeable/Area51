# 5545 : 최고의 피자
# https://www.acmicpc.net/problem/5545

# pizza_cal = dough_cal + sum(topping_cal)
# pizza_cost = dough_cost + topping_cost * topping_kinds

# best_pizza = max value of (pizza_cal / pizza_cost)
# so, best_pizza has max pizza_cal and min pizza_cost

import sys

toppings = int(sys.stdin.readline())
dough_cost, topping_cost = map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))
dough_cal = int(sys.stdin.readline())

topping_cal_list = []
for i in range(0, toppings):
    topping_cal_list.append(int(sys.stdin.readline()))
topping_cal_list.sort(reverse=True)
# print(topping_cal_list)

best = dough_cal / dough_cost
A, B = dough_cal, dough_cost
a, b = 0, 0

for i in range(0, toppings):
    a += topping_cal_list[i]
    b += topping_cost
    best = max(best, (A+a)/(B+b))
print(int(best))