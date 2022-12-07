# 25707 : 팔찌 만들기
# https://www.acmicpc.net/problem/25707

balls = int(input())
ball_list = list(map(lambda x: int(x), input().split(" ")))
# ball_list.sort()

acc = 0
for i in range(0, balls-1):
    acc += max(ball_list[i+1] - ball_list[i], (ball_list[i+1] - ball_list[i]) * -1)

acc += max(ball_list[-1] - ball_list[0], (ball_list[-1] - ball_list[0]) * -1)
print(acc)