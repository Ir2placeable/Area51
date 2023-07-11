# 브루트포스
# 5분 컷

t = int(input())
for test_case in range(1, t+1):
    n, k = map(lambda x: int(x), input().split())
    items = [0 for _ in range(k)]

    index = 0
    while n > 0:
        items[index] += 1
        index = (index + 1) % k
        n -= 1

    result = 1
    for item in items:
        result *= item

    print("#%d %d" % (test_case, result))