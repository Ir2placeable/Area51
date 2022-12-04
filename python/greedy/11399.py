# 11399 : ATM
# https://www.acmicpc.net/problem/11399


# times의 순서를 변경해서 최소 합이 되어야 함 -> 그리디

people = int(input())
times = list(map(lambda x: int(x), input().split(" ")))
times2 = []

for i in range(0, len(times)):
    times2.append([i+1, times[i]])

times2.sort(key=lambda x:x[1])

sum_time = 0
now_time = 0
for time in times2:
    now_time += time[1]
    sum_time += now_time

print(sum_time)

# 2번 사람은 1분만에,
# 5번 사람은 1+2 = 3분,
# 1번 사람은 1+2+3 = 6분,
# 4번 사람은 1+2+3+3 = 9분,
# 3번 사람은 1+2+3+3+4 = 13분이 걸리게 된다.
# 각 사람이 돈을 인출하는데 필요한 시간의 합은 1+3+6+9+13 = 32분이다.
