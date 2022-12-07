# 10610 : 30
# https://www.acmicpc.net/problem/10610

N = input()

if int(N) < 30:
    print(-1)
else:
    temp = 0
    zero = False
    nums = []
    for char in N:
        temp += int(char)
        nums.append(char)
        if char == '0':
            zero = True

    result = ''
    if temp % 3 == 0 and zero:
        nums.sort(reverse=True)
        for i in nums:
            result += i
        print(int(result))
    else:
        print(-1)