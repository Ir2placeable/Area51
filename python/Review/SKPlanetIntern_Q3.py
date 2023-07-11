from copy import deepcopy

result = 0
n = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def checkFlowers(visited):
    for y in range(n):
        for x in range(n):
            if visited[y][x] == '1':
                return False
    return True


def MoveCharacter(cur_y, cur_x, visited):
    global result
    # 움직일 수 있는 방향 찾기
    nex_d_list = []
    for i in range(4):
        nex_y = cur_y + dy[i]
        nex_x = cur_x + dx[i]

        if 0 <= nex_y < n and 0 <= nex_x < n and visited[nex_y][nex_x] == '1':
            nex_d_list.append(i)

    # 움직일 수 있는 방향이 없다
    if not nex_d_list:
        visited[cur_y][cur_x] = '0'
        if checkFlowers(visited):
            result = 1
        return

    # 움직일 수 있는 방향이 있다
    for nex_d in nex_d_list:
        visited_temp = deepcopy(visited)

        # 특정 방향으로 최대한 움직인다.
        cur_x_temp = cur_x
        cur_y_temp = cur_y

        nex_y = cur_y_temp + dy[nex_d]
        nex_x = cur_x_temp + dx[nex_d]

        while 0 <= nex_y < n and 0 <= nex_x < n and visited_temp[nex_y][nex_x] == '1':
            visited_temp[cur_y_temp][cur_x_temp] = '0'

            cur_y_temp, cur_x_temp = nex_y, nex_x

            nex_y = cur_y_temp + dy[nex_d]
            nex_x = cur_x_temp + dx[nex_d]

        MoveCharacter(cur_y_temp, cur_x_temp, visited_temp)


def solution(boards):
    global result, n
    answer = []

    for test_case in boards:
        result = 0
        n = len(test_case)

        maps = [list(single_line) for single_line in test_case]

        character_x = character_y = 0
        for y in range(n):
            for x in range(n):
                if maps[y][x] == '2':
                    character_x = x
                    character_y = y

        MoveCharacter(character_y, character_x, maps)
        answer.append(result)

    return answer


print(solution([["00011", "01111", "21001", "11001", "01111"], ["00011", "00011", "11111", "12101", "11111"]]))
print(solution([["1111", "1121", "1001", "1111"], ["0000", "0000", "0000", "0002"], ["0000", "0100", "0000", "0002"], ["0000", "0010", "0121", "0010"]]))