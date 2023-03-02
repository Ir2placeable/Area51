# https://www.acmicpc.net/problem/1138
import sys

n = int(sys.stdin.readline())
people_in_left = list(map(lambda x: int(x), sys.stdin.readline().split()))
line = [0 for _ in range(n)]

for person in range(n):
    target_pass = people_in_left[person]
    current_pass = 0
    for i in range(n):
        # 이미 사람이 위치한 경우
        if line[i] != 0:
            continue

        # 빈 공간을 모두 패스한 경우
        if target_pass == current_pass:
            line[i] = person + 1
            break

        current_pass += 1

print(*line)