# 15904 : UCPC는 무엇의 약자일까?
# https://www.acmicpc.net/problem/15904

string = input()
target = 'UCPC'
target_index = 0
UCPC_flag = False

for char in string:
    if target[target_index] == char:
        target_index += 1
        if target_index == 4:
            UCPC_flag = True
            break

if target_index >= 4:
    print('I love UCPC')
else:
    print('I hate UCPC')