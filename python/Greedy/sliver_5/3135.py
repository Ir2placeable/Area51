# 3135 : 라디오
# https://www.acmicpc.net/problem/3135

# 현재 주파수 A
# 목표 주파수 B

moves = 0
now_f, target_f = map(lambda ele: int(ele), input().split(" "))
N = int(input())
freq_list = [now_f]

for i in range(0, N):
    freq_list.append(int(input()))

min_freq = 10000
min_index = 0
for i in range(0, len(freq_list)):
    diff = max(target_f - freq_list[i], (target_f - freq_list[i]) * -1)
    if min_freq > diff:
        min_freq = diff
        min_index = i

if not min_index == 0:
    moves += 1
moves += min_freq
print(moves)