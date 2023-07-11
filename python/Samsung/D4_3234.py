def dfs(left, right, index):
    global result
    if left < right:
        return

    if index == n:
        result += 1
        return

    if left >= criteria:
        result += value[n-index]
        return

    for i in range(n):
        if visited[i] == 1:
            continue

        visited[i] = 1
        dfs(left + numbers[i], right, index + 1)
        dfs(left, right + numbers[i], index + 1)
        visited[i] = 0


import math
value = [math.factorial(i) * 2**i for i in range(11)]
t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    numbers = list(map(lambda x: int(x), input().split()))
    criteria = math.ceil(sum(numbers)/2)
    visited = [0 for _ in range(n+1)]

    result = 0
    dfs(0, 0, 0)

    print("#%d %d" % (test_case, result))