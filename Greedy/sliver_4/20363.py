# 20363 : 당근 키우기
# https://www.acmicpc.net/problem/20363

# X : 온기 / Y : 수분
# 모든 자리의 합으로 계산되는 것이 아님!
# 필요한 X보다 더 많은 X를 계산해 두고, Y를 더하는 방법이 최소값이다.

X, Y = map(lambda x: int(x), input().split(" "))
if X < Y:
    X, Y = Y, X

print(X + Y + Y//10)