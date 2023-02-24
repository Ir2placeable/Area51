dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
result = 0
n = 0


def CheckFull(maps):
    for y in range(n):
        for x in range(n):
            if maps[y][x] == '1':
                return False
    return True


def MoveCharacter(cur_y, cur_x, cur_d, maps):
    global result
    nex_y = cur_y + dy[cur_d]
    nex_x = cur_x + dx[cur_d]

    # 전진할 수 없으면, 방향을 변경한다.
    if nex_y < 0 or nex_x < 0 or nex_y > n-1 or nex_x > n-1 or maps[nex_y][nex_x] != '1':
        for _ in range(3):
            cur_d = (cur_d + 1) % 4
            MoveCharacter(cur_y, cur_x, cur_d)
    direction_count = 0
    isBlocked = False
    while nex_y < 0 or nex_x < 0 or nex_y > n-1 or nex_x > n-1 or maps[nex_y][nex_x] != '1':
        if direction_count == 3:
            isBlocked = True
            break
        cur_d = (cur_d + 1) % 4
        nex_y = cur_y + dy[cur_d]
        nex_x = cur_x + dx[cur_d]

        direction_count += 1

    # 방향이 모두 막혀 있으면
    if isBlocked:
        maps[cur_y][cur_x] = '0'
        if CheckFull(maps):
            result = 1

        maps[cur_y][cur_x] = '1'
        return

    # 전진할 수 있으면, 그대로 이동한다. + 백트래킹
    maps[cur_y][cur_x] = '0'
    MoveCharacter(nex_y, nex_x, cur_d, maps)
    maps[cur_y][cur_x] = '1'


def solution(boards):
    global n, result
    answer = []

    for board in boards:
        result = 0
        n = len(board)

        maps = [[0 for _ in range(n)] for _ in range(n)]
        x = y = 0
        for i in range(n):
            for j in range(n):
                if board[i][j] == '2':
                    x, y = j, i
                maps[i][j] = board[i][j]

        MoveCharacter(y, x, 0, maps)
        answer.append(result)
    return answer


# print(solution([["1111", "1121", "1001", "1111"], ["0000", "0000", "0000", "0002"], ["0000", "0100", "0000", "0002"],
#                 ["0000", "0010", "0120", "0010"]]))
print(solution([["00011", "01111", "21001", "11001", "01111"], ["00011", "00011", "11111", "12101", "11111"]]))