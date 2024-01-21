from random import randint as rnd


def check_h_v(chess_desk: list):
    """Checking for "1" value vertically and horizontally"""
    temp_H_V = []
    for column in range(len(chess_desk)):
        for raw in range(len(chess_desk[0])):
            if chess_desk[column].count(1) > 1:
                return False
            temp_H_V.append(chess_desk[raw][column])
        if temp_H_V.count(1) > 1:
            return False
        temp_H_V.clear()
    return True


def check_diag_l(desk_chess: list):
    """Checking diagonals from lower left to upper right"""
    i = 6
    size = len(desk_chess)
    temp_d = []
    while i >= 0:
        for raw2 in range(size - i):
            temp_d.append(desk_chess[raw2 + i][raw2])
        if temp_d.count(1) > 1:
            return False
        temp_d.clear()
        i -= 1
    j = 1
    while j < size:
        for rawm in range(size - j):
            temp_d.append(desk_chess[rawm][rawm + j])
        if temp_d.count(1) > 1:
            return False
        temp_d.clear()
        j += 1
    return True


def check_diag_r(desk_chess: list):
    """Checking diagonals from bottom right to top left"""
    i = 5
    size = len(desk_chess)
    temp_d = []
    while i >= -1:
        for raw1 in range(size - 1, i, -1):
            temp_d.append(desk_chess[raw1][i - raw1])
        if temp_d.count(1) > 1:
            return False
        temp_d.clear()
        i -= 1
    j = 2
    while j < size:
        for raw3 in range(size - j + 1):
            temp_d.append(desk_chess[raw3][- j - raw3])
        if temp_d.count(1) > 1:
            return False
        temp_d.clear()
        j += 1
    return True


def is_attacking(q_1, q_2):
    """Checking whether the queens beat each other"""
    desk = [[0] * 8 for _ in range(8)]
    desk[q_1[0] - 1][q_1[1] - 1] = 1
    desk[q_2[0] - 1][q_2[1] - 1] = 1
    if check_h_v(desk) == check_diag_l(desk) == check_diag_r(desk):
        return True
    else:
        return False


def check_queens(queens: list):
    result = []
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            result.append(is_attacking(queens[i], queens[j]))
    if False in result:
        return False
    else:
        return True


def generate_boards():
    result = []
    count = 0
    attempts = 4
    while count < attempts:
        board = ((rnd(1, 8), rnd(1, 8)) for _ in range(1, 9))
        temp = [*board]
        if check_queens(temp) is True:
            result.append(temp)
            count += 1
    return result


board_list = generate_boards()
print(board_list)
