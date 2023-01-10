# 2141: 우체국
# https://www.acmicpc.net/problem/2141

# 다시 풀어볼 문제
# 특이 유형
import sys

n = int(sys.stdin.readline())
towns = []
total_people = 0
for _ in range(n):
    a, b = map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))
    towns.append([a, b])
    total_people += b
towns.sort()

acc = 0
for town in towns:
    acc += town[1]
    if acc >= total_people/2:
        print(town[0])
        break
