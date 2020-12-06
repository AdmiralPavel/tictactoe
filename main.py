# Вывод передаваемого игрового поля на экран
def print_board(board):
    print(f'{board[0]}|{board[1]}|{board[2]}')
    print('-+-+-')
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print('-+-+-')
    print(f'{board[6]}|{board[7]}|{board[8]}')


# Функция для ввода номера ячейки
def get_input(board, current_player):
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    inp = input(f'Введите номер ячейки, в которую вы хотите поставить {current_player}\n')
    if inp not in nums:
        print('Ошибка! Введите номер ячейки от 0 до 8')
        get_input(board, current_player)
    elif board[int(inp)] == int(inp):
        board[int(inp)] = current_player
    else:
        print('Ошибка! В данной ячейке уже стоит символ.')
        get_input(board, current_player)


# Функция, отображающая конец игры
def is_game_ended(board, current_player):
    horizontal_win = board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or \
                     board[6] == board[7] == board[8]

    vertical_win = board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or \
                   board[2] == board[5] == board[8]

    diagonal_win = board[0] == board[4] == board[8] or board[2] == board[4] == board[6]

    if horizontal_win or vertical_win or diagonal_win:
        return current_player

    for elem in board:
        if elem != 'X' and elem != 'O':
            return 'Running'

    return 'Tie'


# Осуществляется подготовка к игре
board = [int(i) for i in range(9)]
current_player = 'X'
print_board(board)
while is_game_ended(board, current_player) == 'Running':
    get_input(board, current_player)
    print_board(board)
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
if current_player == 'X':
    current_player = 'O'
else:
    current_player = 'X'
if is_game_ended(board, current_player) == 'Tie':
    print('Игра закончилась вничью')
else:
    print(f'Выиграл игрок {current_player}')