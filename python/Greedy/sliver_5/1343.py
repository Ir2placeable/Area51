# 1343 : 폴리오미노
# https://www.acmicpc.net/problem/1343

string = input()

index = 0
stack = 0
result = ''
while 1:
    if index == len(string):
        if stack % 2 == 1 :
            result = -1
            break
        result += 'AAAA' * (stack // 4)
        stack = stack % 4
        result += 'BB' * (stack // 2)
        stack = 0
        break
    elif string[index] == 'X':
        stack += 1
    elif string[index] == '.':
        if stack % 2 == 1 :
            result = -1
            break
        result += 'AAAA' * (stack // 4)
        stack = stack % 4
        result += 'BB' * (stack // 2)
        stack = 0
        result += '.'

    index += 1

print(result)