# 16분

from collections import deque

test_case = int(input())
for case_number in range(1, test_case + 1):
    n = int(input())
    temp = list(map(lambda x: int(x), input().split()))

    screws = deque([])
    for i in range(0, 2*n - 1, 2):
        screws.append([temp[i], temp[i+1]])

    while len(screws) > 1:
        screw = screws.popleft()
        target = screw[-1]

        for i in range(len(screws)):
            if screws[i][0] == target:
                screw += screws[i]
                screws.remove(screws[i])
                break
        screws.append(screw)

    result = screws.pop()
    result = ' '.join(list(map(lambda x: str(x), result)))
    print("#%d" %(case_number), result)