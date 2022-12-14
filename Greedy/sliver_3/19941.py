# 19941 : 햄버거 분배
# https://www.acmicpc.net/problem/19941

n, fork = map(lambda x: int(x), input().split(" "))
temp = input()
table = []
for char in temp:
    table.append(char)

count = 0
for i in range(0, n):
    # 사람 기준 카운트
    if table[i] == 'P':
        j = i - fork
        while (0 <= j < n) and (j <= i + fork):
            if table[j] == 'H':
                table[j] = 'X'
                count += 1
                break
            j += 1
print(count)