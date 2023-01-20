# 14501 : 퇴사
# https://www.acmicpc.net/problem/14501

# 뒤에서 부터 날짜 별로 얻을 수 있는 가장 큰 금액을 계산해본다. in dp list

import sys

n = int(sys.stdin.readline())
schedules = []
for _ in range(n):
    schedules.append(list(map(lambda x: int(x), sys.stdin.readline().split())))


dp = [0 for _ in range(n)]
for start_day in range(n-1, -1, -1):
    total_revenue = 0
    for day in range(start_day, n):
        temp_revenue = 0
        next_day = day

        while next_day < n:
            if next_day + schedules[next_day][0] < n:
                temp_revenue += schedules[next_day][1]
                next_day += schedules[next_day][0]
            else:
                next_day += 1

        total_revenue = max(total_revenue, temp_revenue)

    dp[start_day] = total_revenue
print(dp)