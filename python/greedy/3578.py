# 3578 : Holes
# https://www.acmicpc.net/problem/3578

# input 개수에 맞는 구멍을 가지고 만들 수 있는 최소 수를 구하여라
# test1 : input 15 / output : 48888888
# test2 : input 0 / output : 1

# 1 : 0
# 2 : 0
# 3 : 0
# 4 : 1
# 5 : 0
# 6 : 1
# 7 : 0
# 8 : 2
# 9 : 1
# 0 : 1

# 8은 두 개, 4는 한 개

holes = int(input())

if holes == 0:
    print(1)
elif holes == 1:
    print(0)
elif holes == 2:
    print(8)

# 홀수
elif holes % 2 == 1:
    print(int('4' + '8' * (holes//2)))
# 짝수
else :
    print(int('8' * (holes//2)))
