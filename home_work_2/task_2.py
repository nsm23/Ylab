from random import choice
from termcolor import colored


def draw_board(board):
    matrix = []
    [matrix.append(board[i:i + 10]) for i in range(0, 91, 10)]
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\r''\n'.join(table))


def variant_loose():
    combinations = []
    for i in range(1, 92, 10):
        line = [i for i in range(i, i + 10)]
        [combinations.append(line[i:i + 5]) for i in range(6)]
    for i in range(1, 11):
        line = [i for i in range(i, i + 91, 10)]
        [combinations.append(line[i:i + 5]) for i in range(6)]
    for i in range(5, 11):
        line = [i for i in range(i, i * 9 + 2, 9)]
        for j in range(len(line) - 4):
            combinations.append(line[j:j + 5])
    from_range = 60
    for i in range(96, 91, -1):
        line = [i for i in range(from_range, i + 1, 9)]
        from_range -= 10
        for j in range(len(line) - 4):
            combinations.append(line[j:j + 5])
    to_range = 101
    for i in range(1, 7):
        line = [i for i in range(i, to_range, 11)]
        to_range -= 10
        for j in range(len(line) - 4):
            combinations.append(line[j:j + 5])
    for i in range(11, 52, 10):
        line = [i for i in range(i, 101, 11)]
        for j in range(len(line) - 4):
            combinations.append(line[j:j + 5])
    return combinations


def step_on_board(step, symbol):
    board[step - 1] = symbol


def cancel_step(step):
    board[step - 1] = step


def result():
    for combination in combinations:
        if combination in [
            board[combination[0] - 1] == "X", board[combination[1] - 1] == "X",
            board[combination[2] - 1] == "X", board[combination[3] - 1] == "X",
            board[combination[4] - 1] == "X"
        ]:
            return '0'
        elif combination in [
            board[combination[0] - 1] == "0", board[combination[1] - 1] == "0",
            board[combination[2] - 1] == "0", board[combination[3] - 1] == "0",
            board[combination[4] - 1] == "0"
        ]:
            return 'X'
    return False


def take_input():
    global step
    variants_to_step = [i for i in board if str(i) not in 'XO']
    try:
        step = input("Куда поставим " + 'X' + "? :")
        step = int(step)
        if step not in variants_to_step:
            raise ValueError
    except ValueError:
        print("Ячейка должна быть от 0 до 100 и свободной.")
        take_input()


def computer():
    variants_to_step = [i for i in board if str(i) not in 'XO']
    if not variants_to_step:
        return 'no more moves'
    for variant in range(len(variants_to_step)):
        v = choice(variants_to_step)
        variants_to_step.remove(v)
        step_on_board(v, 'O')
        if not result():
            cancel_step(v)
            return v
        cancel_step(v)
    return 'loose'


board = [i for i in range(1, 101)]
combinations = variant_loose()
game_over = False
people = True
while not game_over:
    draw_board(board)
    if people:
        symbol = "X"
        take_input()
    else:
        print('step computer:')
        symbol = "O"
        step = computer()
    if step == 'no more moves':
        print("Well done!")
        game_over = True
        win = "No one"
    elif step == 'loose':
        print('You won!')
        win = 'X'
        game_over = True
    else:
        step_on_board(step, symbol)
        win = result()
        if win:
            game_over = True
        else:
            game_over = False
    people = not people
draw_board(board)
print(f"Champion  -  {win}")
