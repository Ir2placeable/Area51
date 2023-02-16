# 그래프로 탐색하는 문제

def dfs(cur, index):
    global result
    if sum(cur) >= k:
        result = min(result, sum(cur) - k)
        return

    for i in range(index, n):
        dfs(cur + [numbers[i]], i+1)


t = int(input())
for test_case in range(1, t+1):
    n, k = map(lambda x: int(x), input().split())
    numbers = list(map(lambda x: int(x), input().split()))

    result = 10000 * 20 + 1
    dfs([], 0)

    print("#%d %d" % (test_case, result))