# https://www.acmicpc.net/problem/10431
import sys
from collections import deque

n = int(sys.stdin.readline())
for _ in range(n):
    temp = list(map(lambda x: int(x), sys.stdin.readline().split()))

    case_num = temp[0]
    nums = deque(temp[1:])
    del temp

    result = 0
    line = deque([])
    while nums:
        num = nums.popleft()

        if not line:
            line.append(num)
            continue

        if line[0] > num:
            result += len(line)
            line.appendleft(num)
        else:
            line.append(num)

    print("%d %d" % (case_num, result))