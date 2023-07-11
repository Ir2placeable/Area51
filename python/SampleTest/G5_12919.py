# https://www.acmicpc.net/problem/12919

# 일단 하나씩 다 해보면서 구할 수 있을 것 같음..
# BFS 방식으로 해보자 -> 시간초과 발생
# 시간초과 원인..? 모르겠으나, DFS 방식으로 해보자
# DFS 방식 -> 시간초과 발생
# S -> T 가 아니라, T -> S 순서로 해보자

import sys

target = sys.stdin.readline().rstrip()
string = sys.stdin.readline().rstrip()


def invertString(origin):
    modified = ''
    for i in range(len(origin)-1, -1, -1):
        modified += origin[i]
    return modified


def dfs(_string):
    global result
    if _string == target:
        result = 1
        return
    if len(_string) < len(target):
        return

    if _string[0] == 'B':
        dfs(invertString(_string)[:-1])
    if _string[-1] == 'A':
        dfs(_string[:-1])


result = 0
dfs(string)
print(result)