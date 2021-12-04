import numpy as np

xdim = 5
ydim = 5
zdim = 100

drawn_numbers = np.loadtxt('input.txt', max_rows=1, dtype=int, delimiter=',')
bingo_boards = np.loadtxt('input.txt', skiprows=2, dtype=int)
bingo_boards = np.reshape(bingo_boards, (zdim, xdim, ydim), order='C')


def check_vertical(array, y):
    for i in range(ydim):
        if not array[i, y] == -1:
            return False
    return True


def check_horizontal(array, x):
    for i in range(xdim):
        if not array[x, i] == -1:
            return False
    return True


def is_not_in_winning_board_indices(indices, current_index):
    if len(indices) == 0:
        return True

    for index in indices:
        if index == current_index:
            return False

    return True


winning_board = None
winning_number = 0
number_of_winning_boards = 0
winning_boards_z_indices = []

for i in range(len(drawn_numbers)):
    for z in range(zdim):
        for x in range(xdim):
            for y in range(ydim):
                if bingo_boards[z, x, y] == drawn_numbers[i]:
                    bingo_boards[z, x, y] = -1

                if check_horizontal(bingo_boards[z, :, :], x) or check_vertical(bingo_boards[z, :, :], y):

                    if is_not_in_winning_board_indices(winning_boards_z_indices, z):
                        winning_boards_z_indices.append(z)
                        number_of_winning_boards += 1

                    if number_of_winning_boards == zdim:
                        winning_board = bingo_boards[z, :, :]
                        winning_number = drawn_numbers[i]
                        break

            if (winning_board is not None) and number_of_winning_boards == zdim:
                break

        if (winning_board is not None) and number_of_winning_boards == zdim:
            break

    if (winning_board is not None) and number_of_winning_boards == zdim:
        break

print(winning_board)
print(winning_number)

sum_winning_board = 0
for i in range(xdim):
    for j in range(ydim):
        if not winning_board[i, j] == -1:
            sum_winning_board += winning_board[i, j]

print(sum_winning_board * winning_number)