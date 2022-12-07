# 19564 : 반복
# https://www.acmicpc.net/problem/19564

# a b c d e f g h i j k l m n o p q r s t u v w x y z
string = input()

now_index = 0
next_index = 0
K = 0

while now_index < len(string):
    K += 1
    next_index = now_index + 1
    while (next_index < len(string)) and (ord(string[now_index]) < ord(string[next_index])):
        now_index += 1
        next_index += 1
    now_index = next_index

print(K)