# https://www.acmicpc.net/problem/2292

# BFS 최단경로 문제같지만, 단순 수학으로 풀 수 있는 문제이다.
# 1 ~ 1 : 0
# 2 ~ 7 : 6
# 8 ~ 19 : 12
# 20 ~ 37 : 18
# 6의 배수로 증가하는 추세를 보인다.
import sys

n = int(sys.stdin.readline())

temp = 1
add = 1
while temp < n:
    temp += 6 * add
    add += 1
print(add)