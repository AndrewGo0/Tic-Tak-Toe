# write your code here
#print('Enter cells:')
userInput = '         '


def get_result(cells):
    matrix = [[cells[i], cells[i+1], cells[i+2]] for i in [0, 3, 6]]
    x_wins = False
    o_wins = False
    impossible = False
    game_not_finished = False
    num_of_X = 0
    num_of_O = 0
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 'X':
                num_of_X += 1
            elif matrix[i][j] == 'O':
                num_of_O += 1
            elif matrix[i][j] == ' ' or matrix[i][j] == '_':
                game_not_finished = True

        if matrix[i][0] == matrix[i][1] == matrix[i][2]:

            if matrix[i][0] == "X":
                x_wins = True
            if matrix[i][0] == 'O':
                o_wins = True
        if matrix[0][i] == matrix[1][i] == matrix[2][i]:

            if matrix[0][i] == "X":
                x_wins = True
            if matrix[0][i] == 'O':
                o_wins = True

    if matrix[0][0] == matrix[1][1] == matrix[2][2] or matrix[0][2] == matrix[1][1] == matrix[2][0]:
        if matrix[1][1] == "X":
            x_wins = True
        if matrix[1][1] == 'O':
            o_wins = True
    if abs(num_of_X - num_of_O) > 1:
        impossible = True

    if x_wins and o_wins:
        impossible = True

    if impossible:
        return 'Impossible'
    elif x_wins:
        return 'X wins'
    elif o_wins:
        return 'O wins'
    elif game_not_finished:
        return 'Game not finished'
    else:
        return 'Draw'


def fill_the_field(cells):
    mas = cells
    return f'---------\n| {mas[0]} {mas[1]} {mas[2]} |\n' \
           f'| {mas[3]} {mas[4]} {mas[5]} |\n| {mas[6]} {mas[7]} {mas[8]} |\n---------'


def select_cell(cells, coordinates):
    x_coordinate = coordinates.split(' ')[0]
    o_coordinate = coordinates.split(' ')[1]
    if x_coordinate.isdigit() == False or o_coordinate.isdigit() == False:
        print('You should enter numbers!')
        return cells
    elif int(x_coordinate) > 3 or int(x_coordinate) < 1 or int(o_coordinate) > 3 or int(o_coordinate) < 1:
        print('Coordinates should be from 1 to 3!')
        return cells
    else:
        x_coordinate = int(x_coordinate) - 1
        o_coordinate = 3 - int(o_coordinate)
        matrix = [[cells[i], cells[i+1], cells[i+2]] for i in [0, 3, 6]]
        if matrix[o_coordinate][x_coordinate] == 'X' or matrix[o_coordinate][x_coordinate] == 'O':
            print('This cell is occupied! Choose another one!')
            return cells
        else:
            x_counter = 0
            o_counter = 0
            for i in range(3):
                for j in range(3):
                    if matrix[i][j] == 'X':
                        x_counter += 1
                    if matrix[i][j] == 'O':
                        o_counter += 1
            if x_counter > o_counter:
                matrix[o_coordinate][x_coordinate] = 'O'
            elif o_counter > x_counter:
                matrix[o_coordinate][x_coordinate] = 'X'
            else:
                matrix[o_coordinate][x_coordinate] = 'X'
            mas = ''.join(matrix[0]) + ''.join(matrix[1]) + ''.join(matrix[2])
            return ''.join(mas)


print(fill_the_field(userInput))
while True:
    print('Enter the coordinates:')
    userCoordinate = input()
    print(fill_the_field(select_cell(userInput, userCoordinate)))
    userInput = select_cell(userInput, userCoordinate)
    if get_result(userInput) != 'Game not finished':
        print(get_result(userInput))
        break




