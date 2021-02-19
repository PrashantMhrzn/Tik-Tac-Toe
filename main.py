from Utils import utils
from Utils import ascii_text 

ascii_text.greeting()
utils.print_board(utils.a)    
while utils.win() != True:
    usr_inp = int(input('Player\'s Turn(1-9): '))
    if usr_inp < 1 or usr_inp > 9:
        print('Invalid input enter between 1-9!')
    else:
        utils.player_turn(usr_inp)
        utils.cpu_turn()