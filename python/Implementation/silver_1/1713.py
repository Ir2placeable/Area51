# https://www.acmicpc.net/problem/1713

# LFU 구현
# 빈도 수 낮은 것 제거
# 2개 이상인 경우 -> 오래된 것 제거

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
nums = list(map(lambda x: int(x), sys.stdin.readline().split()))

time = 0
frames = []
for num in nums:
    time += 1

    isFrame = -1
    for i in range(len(frames)):
        if frames[i][2] == num:
            isFrame = i
            break

    # HIT
    if isFrame != -1:
        frames[isFrame][0] += 1
    # MISS
    else:
        if len(frames) >= n:
            frames.pop(0)
        frames.append([1, time, num])
    frames.sort(key=lambda x: (x[0], x[1]))

result = sorted(list(map(lambda x: x[2], frames)))
print(*result)