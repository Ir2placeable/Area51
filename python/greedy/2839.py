# 2839 : 설탕 배달
# https://www.acmicpc.net/problem/2839

# 경우의 수를 전부 구해보는 것이다..!

sugar = int(input())
bag3 = 0
bag5 = 0

temp = 0
i3 = 0
i5 = 0
flag = False
oppo = []
while i5 <= sugar//5:
    # print(i5)
    i3 = 0
    temp = 5 * i5 + 3 * i3
    while temp <= sugar:
        # print('i3 : ', i3)
        temp = 5 * i5 + 3 * i3
        if temp == sugar:
            flag = True
            break
        i3 += 1
    if flag:
        oppo.append(i5 + i3)
        flag = False
    i5 += 1

if len(oppo) == 0:
    print(-1)
else:
    print(oppo[-1])