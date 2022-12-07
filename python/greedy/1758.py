# 1758 : 알바생 강호
# https://www.acmicpc.net/problem/1758

waiting_people = int(input())

tip_list = []
for i in range(1, waiting_people+1):
    tip_list.append(int(input()))

tip_list.sort(reverse=True)

total_tip = 0
for i in range(0, waiting_people):
    tip = tip_list[i] - i
    if tip > 0 :
        total_tip += tip

print(total_tip)