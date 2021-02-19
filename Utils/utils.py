import random
from .ascii_text import player, cpu

a = [[' ', ' ', ' '],
     [' ', ' ', ' '],
     [' ', ' ', ' ']]


def print_board(a):
    print(a[0][0] + '|' + a[0][1] + '|' + a[0][2])
    print('-+-+-')
    print(a[1][0] + '|' + a[1][1] + '|' + a[1][2])
    print('-+-+-')
    print(a[2][0] + '|' + a[2][1] + '|' + a[2][2])
    print()


def valid(pos):
    return True if pos == ' ' else False


def player_invalid():
    return '\nPlayer move invalid turn skipped!'
    
    
def player_turn(usr_inp):
    for i in range(1, 10):
        if i == usr_inp:
            if i == 1:
                if valid(a[0][0]):
                    a[0][0] = 'O'
                else:
                    print(player_invalid())
            elif i == 2:
                if valid(a[0][1]):
                    a[0][1] = 'O'
                else:
                    print(player_invalid())
            elif i == 3:
                if valid(a[0][2]):
                    a[0][2] = 'O'
                else:
                    print(player_invalid())
            elif i == 4:
                if valid(a[1][0]):
                    a[1][0] = 'O'
                else:
                    print(player_invalid())
            elif i == 5:
                if valid(a[1][1]):
                    a[1][1] = 'O'
                else:
                    print(player_invalid())
            elif i == 6:
                if valid(a[1][2]):
                    a[1][2] = 'O'
                else:
                    print(player_invalid())
            elif i == 7:
                if valid(a[2][0]):
                    a[2][0] = 'O'
                else:
                    print(player_invalid())
            elif i == 8:
                if valid(a[2][1]):
                    a[2][1] = 'O'
                else:
                    print(player_invalid())
            elif i == 9:
                if valid(a[2][2]):
                    a[2][2] = 'O'
                else:
                    print(player_invalid())
    print('\nPlayer\'s move:')
    print_board(a)


def cpu_turn():
    r1 = random.randint(0, 2)
    r2 = random.randint(0, 2)
    if valid(a[r1][r2]):
        a[r1][r2] = 'X'
    else:
        print('\nCpu move is invalid turn skipped!')
    print('\nCpu\'s move:')
    print_board(a)


def win():
    if a[0][0] == a[0][1] == a[0][2] == 'O' or a[1][0] == a[1][1] == a[1][2] == 'O' or a[2][0] == a[2][1] == a[2][2] == 'O':
        player()
        return True
    elif a[0][0] == a[1][0] == a[2][0] == 'O' or a[0][1] == a[1][1] == a[2][1] == 'O' or a[0][2] == a[1][2] == a[2][2] == 'O':
        player()
        return True
    elif a[0][0] == a[1][1] == a[2][2] == 'O' or a[2][0] == a[1][1] == a[0][2] == 'O':
        player()
        return True
    elif a[0][0] == a[0][1] == a[0][2] == 'X' or a[1][0] == a[1][1] == a[1][2] == 'X' or a[2][0] == a[2][1] == a[2][2] == 'X':
        cpu()
        return True
    elif a[0][0] == a[1][0] == a[2][0] == 'X' or a[0][1] == a[1][1] == a[2][1] == 'X' or a[0][2] == a[1][2] == a[2][2] == 'X':
        cpu()
        return True
    elif a[0][0] == a[1][1] == a[2][2] == 'X' or a[2][0] == a[1][1] == a[0][2] == 'X':
        cpu()
        return True
