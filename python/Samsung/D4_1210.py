# 구현 문제

# 24분 컷

for _ in range(10):
    test_case = int(input())
    maps = []
    for i in range(100):
        maps.append(list(map(lambda x: int(x), input().split())))

    # 시작점
    cur = 0
    for i in range(100):
        if maps[-1][i] == 2:
            cur = i
            break

    # 사다리로 이동하기
    # 하나씩 위로 움직인다.
    for y in range(99, -1, -1):
        # 왼쪽 체크
        if 0 < cur and maps[y][cur-1] == 1:
            while 0 < cur and maps[y][cur-1] == 1:
                cur -= 1
        elif cur < 99 and maps[y][cur + 1] == 1:
            while cur < 99 and maps[y][cur+1] == 1:
                cur += 1

    result = cur
    print("#%d %d" % (test_case, result))