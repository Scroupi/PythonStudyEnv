#Module func_XnO_game
# Functions:

#Move order
def whosFirst():
    import random
    # 1 stands for X , 0 stands for O

    print('Now random module will decide your fate, who\'ll be first) ')
    if random.randint(0,1) == 1:
        print('Good. You move first, you\'re playing as X ')
        h_player = 'X'
        c_player = 'O'
    else:
        print('You move second, you\'re playing as O ')
        h_player = 'O'
        c_player = 'X'

    return h_player, c_player

# Gettin' user input

def get_input():
    try:
        *choice, = int(input('Type row please, from 0 to 2: ')),int(input('Type column: '))
        return choice
    except:
        print('Type please 0 0,0 1,2 2 etc...')
        get_input()

# Getting computer move
def c_move(field):
    import random
    row = random.randint(0,2)
    column = random.randint(0,2)
    if field[row][column] != 'X' and field[row][column] != 'O':
        return row,column
    else:
        return c_move(field)


# Updating field by players moves
def field_update(field,player,*choice):
    (row,column) = choice
    if field[row][column] != 'X' and field[row][column] != 'O':
        field[row][column] = player
    else:
        print('That square is taken, please try again')
        sh_field(field)
        choice = get_input()
        field_update(field,player,*choice)
        
#Show field
def sh_field(field):
    print()
    for i in field:
        print(' '.join(map(str,i)))
                
# Here, im trying to parse everything in one function
# to iterate through inner_loop more easely
def move(h_player,c_player,field):
    if h_player == 'X':
        choice = get_input()
        
        field_update(field,h_player,*choice)
        if win_con(field,h_player):
            print('Congratz you\'ve won!!')
            return True

        sh_field(field)
        
        
        c_choice = c_move(field)
        
        field_update(field,c_player,*c_choice)
        if win_con(field,c_player):
            print('Computer has won!')
            return True
        sh_field(field)
        
    else:
        c_choice = c_move(field)
        field_update(field,c_player,*c_choice)
        if win_con(field,c_player):
            print('Computer has won!!')
            return True
        sh_field(field)
        
        choice = get_input()
        field_update(field,h_player,*choice)
        if win_con(field,h_player):
            print('Congratz you\'ve won!!')
            return True
        sh_field(field)
# Checking for win condition
''' field = 0 1 2, 0
            0 1 2, 1
            0 1 2  2   '''

def win_con(field,player):
    for i in range(len(field)):
        ls_col = []
        for k in range(len(field[i])):

            # row search

            str_row = ''.join(map(str,field[i]))
            if player * 3 == str_row:
                return True

            #column search

            ls_col.append(field[k][i])
            str_col = ''.join(map(str,ls_col))
            if player * 3 == str_col:
                return True

    # diagnol search
    for i,r in enumerate(field):
        ls_dia = []
        ls_negdia = []
        ls_dia.append(r[i])
        ls_negdia.append(r[-i-1])
        str_dia = ''.join(map(str,ls_dia))
        str_negdia = ''.join(map(str,ls_negdia))
        if player * 3 == str_dia:
            return True
            
        if player * 3 == str_negdia:
            return True

            
            
            
    










