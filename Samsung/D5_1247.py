# 가능한 모든 경로를 살펴도 된다고 했다. -> 브루트 포스
# 회사 -> 고객 -> 집 경로에서 고객의 경로가 항상 변한다.
# 고객의 경로는 순열로 나타낼 수 있다.

# 14분 컷

from itertools import permutations

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    temp = list(map(lambda x: int(x), input().split()))

    start = [temp[0], temp[1]]
    end = [temp[2], temp[3]]

    customers = []
    for i in range(4, len(temp), 2):
        customers.append([temp[i], temp[i+1]])

    customers_index = [i for i in range(len(customers))]

    result = 1000000000
    for temp2 in permutations(customers_index, len(customers)):
        temp_result = 0
        prev = start
        for i in temp2:
            temp_result += abs(customers[i][0] - prev[0])
            temp_result += abs(customers[i][1] - prev[1])
            prev = customers[i]
        temp_result += abs(prev[0] - end[0]) + abs(prev[1] - end[1])

        result = min(result, temp_result)

    print("#%d %d" % (test_case, result))