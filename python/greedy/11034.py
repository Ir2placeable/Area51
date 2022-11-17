# 11034 : 캥거루 세마리2
# https://www.acmicpc.net/problem/11034

# 캥거루 3마리가 1차원 좌표 위에 있음
# 한번 이동 시, 바깥쪽의 캥거루가 두 캥거루 사이로 이동함
# 결론적으로, 캥거루는 연속된 숫자로 위치하게 됨
# 그리디로 어떻게 해결하지 이걸?

# 3 5 9 / 5 8 9 / 5 6 8 / 6 7 8

while True:
    try:
        num_of_moves = 0
        kangarooA, kangarooB, kangarooC = map(lambda ele: int(ele), input().split(" "))

        gapAB = kangarooB - kangarooA
        gapBC = kangarooC - kangarooB

        print(max(gapAB, gapBC)-1)
    except:
        exit(0)