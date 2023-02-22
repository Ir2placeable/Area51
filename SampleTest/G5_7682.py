# https://www.acmicpc.net/problem/7682
import sys

players = ['X', 'O']


def EndCondition(state):
    isEnd1 = True
    for temp in state:
        if temp == '.':
            isEnd1 = False
            break

    isEnd2 = False
    for i in range(0, 9, 3):
        if state[i] == '.':
            continue
        if state[i] == state[i+1] == state[i+2]:
            isEnd2 = True
            break

    isEnd3 = False
    for i in range(3):
        if state[i] == '.':
            continue
        if state[i] == state[i+3] == state[i+6]:
            isEnd3 = True
            break

    isEnd4 = False
    if (state[0] == state[4] == state[8] != '.') or (state[2] == state[4] == state[6] != '.'):
        isEnd4 = True

    if isEnd1 or isEnd2 or isEnd3 or isEnd4:
        return True
    else:
        return False


def TicTacToe(cur_state, cur_player):
    # print(cur_state)
    global result
    if cur_state == target_state:
        result = 'valid'
        return

    if EndCondition(cur_state):
        return

    for i in range(9):
        if visited[i] == 1:
            continue

        visited[i] = 1
        next_state = cur_state[:]
        next_state[i] = players[cur_player]
        next_player = (cur_player + 1) % 2

        TicTacToe(next_state, next_player)
        visited[i] = 0


while True:
    string = sys.stdin.readline().rstrip()
    if string == 'end':
        break

    target_state = list(string)
    init_state = ['.' for _ in range(9)]
    visited = [0 for _ in range(9)]

    result = 'Invalid'
    TicTacToe(init_state, 0)
    print(result)