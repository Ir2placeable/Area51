# 20186 : 수 고르기
# https://www.acmicpc.net/problem/20186
import sys

N, K = map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))
number_list = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))

new_list = []
for i in range(0, N):
    new_list.append([i, number_list[i]])

new_list = sorted(new_list, key=lambda x: x[1], reverse=True)

score = 0
for i in range(0, K):
    score += new_list[i][1]
    score -= i

print(score)