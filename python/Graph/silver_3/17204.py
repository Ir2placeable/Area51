# 17204 : 죽음의 게임
# https://www.acmicpc.net/problem/17204
import sys

people, target = map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))
numbers = []
for _ in range(people):
    numbers.append(int(sys.stdin.readline()))

visited = [0] * people
visited[0] = 1
count = 0
index = 0
while True:
    if index == target:
        break

    index = numbers[index]
    count += 1

    if visited[index] == 0:
        visited[index] = 1
    else:
        count = -1
        break

print(count)