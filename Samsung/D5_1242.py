# 구현 문제

# 1. 직사각형 배열을 2진수로 변환한다.
# 2. 각 줄의 비율을 조사하여 -> 8자리 코드로 만든다.
# 3. 체크섬을 판별한다.
# 4. 정상코드의 수를 합한다.

# 30분 초과 실패


codeDictionary = {3211: 0, 2221: 1, 2122: 2, 1411: 3, 1132: 4, 1231: 5, 1114: 6, 1312: 7, 1213: 8, 3112: 9}


def HexTobin(hexNum):
    return bin(int(hexNum, 16))[2:].zfill(4)


def Decoding(encodedNum):
    temp_code = []
    cur_code = encodedNum[0]
    cur_count = 0

    for i in range(0, len(encodedNum)):
        if cur_code == encodedNum[i]:
            cur_count += 1
        else:
            temp_code.append(cur_count)
            cur_count = 1
            cur_code = encodedNum[i]
    temp_code.append(cur_count)

    temp_code = list(map(lambda x: str(x // min(temp_code)), temp_code))
    temp_code = int(sum(temp_code))
    return codeDictionary[temp_code]


t = int(input())
for test_case in range(1, t+1):
    height, width = map(lambda x: int(x), input().split())
    codes = []
    for _ in range(height):
        temp_code = ''
        for char in input():
            temp_code += HexTobin(char)
        codes.append(temp_code)

    for single_code in codes:
        for i in range(0, len(single_code), 8):
            print(single_code[i:i+8])



