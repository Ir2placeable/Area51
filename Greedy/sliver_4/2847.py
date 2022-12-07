# 2847 : 게임을 만든 동준이
# https://www.acmicpc.net/problem/2847

levels = int(input())

score_list = []
for i in range(0, levels):
    score_list.append(int(input()))

dec = 0
for i in range(levels-2, -1, -1):
    if score_list[i] >= score_list[i+1]:
        dec += score_list[i] - score_list[i+1] + 1
        score_list[i] = score_list[i+1] - 1
print(dec)