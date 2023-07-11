# https://www.acmicpc.net/problem/10431
import sys
from collections import deque

n = int(sys.stdin.readline())
for _ in range(n):
    temp = list(map(lambda x: int(x), sys.stdin.readline().split()))

    case_num = temp[0]
    nums = deque(temp[1:])

    result = 0
    line = []
    while nums:
        num = nums.popleft()

        if not line:
            line.append(num)
            continue

        inserted = False
        for i in range(len(line)):
            if line[i] > num:
                result += len(line) - i
                line.insert(i, num)
                inserted = True
                break

        if not inserted:
            line.append(num)

    print("%d %d" % (case_num, result))