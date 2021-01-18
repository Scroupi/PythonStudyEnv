
import random
from funcs_XnO import *

main_loop = True
inner_loop = True

while main_loop:
    # creating game field every iteration
    global field
    field = [ [[],[],[]],
              [[],[],[]],
              [[],[],[]], ]
    # unpacking players side
    h_player,c_player = whosFirst()

    # Loop to define winner
    while inner_loop:
        if move(h_player,c_player,field):
            inner_loop = False
    
    quit_game = input('Do u wanna play more? Type Y or N: ')
    if quit_game == 'N':    
        main_loop = False
    inner_loop = True
