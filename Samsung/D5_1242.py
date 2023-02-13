# 구현
# 55분 컷

HexToBin = {'0':'0000', '1':'0001', '2':'0010', '3':'0011',
         '4':'0100', '5':'0101', '6':'0110', '7':'0111',
         '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
         'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

Decoding = {'211':0, '221':1, '122':2, '411':3, '132':4, '231':5, '114':6, '312':7, '213':8, '112':9}


def getIndexOfCode(a, b, c):
    k = min(a, b, c)
    a //= k
    b //= k
    c //= k
    return str(100 * a + 10 * b + c)

def verifyCheckSum(numbers):
    temp = sum(numbers)
    for i in range(0, 8, 2):
        temp += numbers[i] * 2

    if temp % 10 == 0:
        return True
    else:
        return False

t = int(input())

for test_case in range(1, t+1):
    height, width = map(lambda x: int(x), input().split())
    hex_code = [input() for _ in range(height)]

    bin_code = ['' for _ in range(height)]
    for i in range(height):
        for j in range(width):
            bin_code[i] += HexToBin[hex_code[i][j]]

    result = 0
    codes = []
    histories = []
    for y in range(height):
        a, b, c = 0, 0, 0
        for x in range(4 * width -1, -1, -1):
            if a == 0 and b == 0 and bin_code[y][x] == '1':
                c += 1
            elif c > 0 and a == 0 and bin_code[y][x] == '0':
                b += 1
            elif c > 0 and b > 0 and bin_code[y][x] == '1':
                a += 1

            if a > 0 and b > 0 and c > 0 and bin_code[y][x] == '0':
                # 암호코드 발견
                codes.append(Decoding[getIndexOfCode(a, b, c)])
                a, b, c = 0, 0, 0

            # 암호코드 8자리가 완성되면
            if len(codes) == 8:
                codes.reverse()

                # 히스토리에 추가한다.
                if codes not in histories:
                    histories.append(codes)

                    # 정상 암호코드인 경우 결과값을 더한다.
                    if verifyCheckSum(codes):
                        result += sum(codes)
                codes = []

    print("#%d %d" % (test_case, result))