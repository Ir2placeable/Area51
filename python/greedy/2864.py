# 2864 : 5와 6의 차이
# https://www.acmicpc.net/problem/2864

# 5가 들어오면 6이 될 수 있음.
# 6이 들어오면 5가 될 수 있음.
# 5 또는 6의 위치를 파악해서, 아예 두 수를 만드는 것임.
a, b = input().split(" ")

min_a, min_b, max_a, max_b = '', '', '', ''
for i in a:
    if i == '5' or i == '6':
        max_a += '6'
        min_a += '5'
    else:
        min_a += i
        max_a += i

for i in b:
    if i == '5' or i == '6':
        max_b += '6'
        min_b += '5'
    else:
        min_b += i
        max_b += i

print(int(min_a) + int(min_b), int(max_a) + int(max_b))