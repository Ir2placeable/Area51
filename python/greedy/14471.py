# 14471 : 포인트 카드
# https://www.acmicpc.net/problem/14471

# 첫 줄 : 칸 개수 2N / 복권 개수 M
# 다음 줄 : 당첨 도장 개수 / 꽝 도장 개수

# 복권 개수 M개 중 1개를 제외하고 전부 당첨이 되려고 함
# 당첨 조건 : 절반 이상 당첨

holes, tickets = map(lambda x: int(x), input().split(" "))

wins = 0
pay_to_win = []
for i in range(0, tickets):
    true, false = map(lambda x: int(x), input().split(" "))

    if true >= false :
        wins += 1
    else:
        pay_to_win.append(holes - true)

pay_to_win.sort()
money = 0
for i in range(0, tickets - wins-1):
    money += pay_to_win[i]

print(money)

