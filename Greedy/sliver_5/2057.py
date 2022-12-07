# 2057 : 팩토리얼 분해
# https://www.acmicpc.net/problem/2057

# 예를 들어 2 = 0!+1!로 나타낼 수 있지만, 5는 이와 같은 방식으로 나타낼 수 없다.

N = int(input())
fac_list = []


def factorial(x):
    if x == 0:
        return 1
    acc = 1
    for i in range(1, x + 1):
        acc *= i
    return acc


index = 0
while 1:
    fac = factorial(index)
    if fac > N:
        break
    fac_list.append(fac)
    index += 1

fac_list.sort(reverse=True)
# print(fac_list)

flag = False
for num in fac_list:
    if N - num < 0:
        continue
    N -= num
    # print(num)
    if N == 0:
        flag = True
        break

if flag:
    print('YES')
else:
    print('NO')