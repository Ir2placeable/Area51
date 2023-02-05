# https://www.acmicpc.net/problem/1138

# N 최대 10, 순열 최대값 약 300만, 최대 10번 돌림 -> 3000천만 -> 완전탐색 불가능

import sys
n = int(sys.stdin.readline())
nums = list(map(lambda x: int(x), sys.stdin.readline().split()))

result = [0 for i in range(n)]
for i in range(n):
    base = result.index(0)
    add = nums[i]

    for j in range(base, n):
        if result[j] == 0:
            if add == 0:
                result[j] = i + 1
                break

            add -= 1



print(result)