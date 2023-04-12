import sys

n = int(sys.stdin.readline())
nums = [0] + [int(sys.stdin.readline()) for _ in range(n)]
# print(nums)

result = []
for start in range(1, n+1):
    visited = [False for _ in range(n+1)]
    visited[start] = True

    cur, nex = start, nums[start]
    temp = [cur, nex]

    while True:
        if visited[nex]:
            if nex == start:
                result += temp
            break

        visited[nex] = True
        cur, nex = nex, nums[nex]
        temp += [nex]

result = sorted(set(result))
print(len(result))
for num in result:
    print(num)
