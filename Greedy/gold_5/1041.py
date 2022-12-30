# 1041 : 주사위
# https://www.acmicpc.net/problem/1041

# 3면 : 4개 * 최소 3개 합
# 2면 : {(N-2) * 4 + (N-1) * 4 } * 최소 2개 합
# 1면 : (N-2)**2 * 5 + (N-2) * 4 * 최소 1개 합
# 주사위의 A와 F는 동시에 존재할 수 없음 -> A와 F 중에 큰 수를 제외시킨다.
import sys

n = int(sys.stdin.readline())
dice_numbers = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))

numbers = []
for i in range(3):
    a, b = dice_numbers[i], dice_numbers[6-i-1]
    if a > b:
        numbers.append(b)
    else:
        numbers.append(a)

numbers.sort()
sum3 = sum(numbers)
sum2 = sum(numbers[:2])
sum1 = numbers[0]

face3 = 4 * sum3
face2 = ((n-2)*4 + (n-1)*4) * sum2
face1 = ((n-2)**2 + (n-1)*(n-2)*4) * sum1
print(face1 + face2 + face3)