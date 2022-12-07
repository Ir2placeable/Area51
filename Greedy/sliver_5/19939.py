# 19939 : 박 터뜨리기
# https://www.acmicpc.net/problem/19939

# 팀 개수 : teams
# 공 개수 : balls
# 바구니의 공 개수 모두 다름, 단 최소 1개 이상
# 가장 많이 담긴 바구니와, 가장 적게 담긴 바구니의 차이가 최소가 되어야 한다.
# return 공 개수 차이 / if cant return -1

balls, teams = map(lambda x: int(x), input().split(" "))

if (teams * (teams+1) // 2) > balls:
    print(-1)
else:
    balls -= teams * (teams+1) // 2
    basic_ball = balls // teams
    balls = balls % teams

    basket = []
    for i in range(0, teams):
        basket.append(basic_ball + i + 1)

    if not balls == 0:
        basket[-1] += 1

    print(basket[-1] - basket[0])
