# 1439 : 뒤집기
# https://www.acmicpc.net/problem/1439

string = input()
seq0, seq1 = 0, 0
start_index = 0
while start_index < len(string):
    stop_index = start_index + 1
    while (stop_index < len(string)) and (string[start_index] == string[stop_index]):
        stop_index += 1

    if string[start_index] == '0':
        seq0 += 1
    else :
        seq1 += 1
    start_index = stop_index
print(min(seq0, seq1))