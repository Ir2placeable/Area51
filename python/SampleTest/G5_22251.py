# https://www.acmicpc.net/problem/22251

# 1을 1로 변경하는 경우 -> 0개 토글
# 1을 2로 변경하는 경우 -> 5개 토글
# a를 b로 변경하는 경우 -> x개 토글이 고정되어 있다.
import sys

segments = [[1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 1, 1, 0, 0, 1, 1],
            [1, 0, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1]]
toggleCounts = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(10):
        count = 0
        for k in range(7):
            if segments[i][k] != segments[j][k]:
                count += 1
        toggleCounts[i][j] = count

max_number, num_segments, max_toggle, cur_number = map(lambda x: int(x), sys.stdin.readline().split())
cur_segment = list(str(cur_number).zfill(num_segments))

result = -1
for target_number in range(1, max_number + 1):
    target_segment = list(str(target_number).zfill(num_segments))

    required_toggles = 0
    for i in range(num_segments):
        required_toggles += toggleCounts[int(target_segment[i])][int(cur_segment[i])]

    if required_toggles <= max_toggle:
        result += 1
print(result)