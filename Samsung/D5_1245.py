# 이진탐색

t = int(input())
for test_case in range(1, t + 1):
    n = int(input())
    temp = list(map(lambda x: int(x), input().split()))

    # location, scale
    points = []
    for i in range(n):
        points.append([temp[i], temp[i+n]])

    result_list = []
    for i in range(n-1):
        left = points[i][0]
        right = points[i+1][0]
        while right - left > 1 / 10 ** 12:
            mid = (right + left) / 2

            force = 0
            for location, mass in points:
                if mid == location:
                    continue
                temp_force = mass / (mid - location) ** 2
                if location < mid:
                    force -= temp_force
                else:
                    force += temp_force

            if force < 0:
                left = mid
            else:
                right = mid
        result_list.append(format((left + right) / 2, ".10f"))

    result = ' '.join(result_list)
    print("#%d" % test_case, result)