# 3135 : 라디오
# https://www.acmicpc.net/problem/3135

# 현재 주파수 A
# 목표 주파수 B

moves = 0
now_f, target_f = map(lambda ele: int(ele), input().split(" "))
N = int(input())
freq_list = []

for i in range(0, N):
    freq_list.append(int(input()))

