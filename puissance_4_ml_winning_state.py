'''
Board visualisation:

     1  2  3  4  5  6  7
  6                    42
  5                    ..
  4                    ..
  3  .                 21
  2  8  9  10 11 12 13 14
  1  1  2  3  4  5  6  7


'''

import random
import copy

def ij_to_k(i,j):
    '''i-th row and j-th column'''
    return (i-1)*7+j

def k_to_ij(k):
    i = k//7
    j = k - (i-1)*7
    return i,j


def direction(dir,x,y,xmax,ymax):
    '''
        Give the position of the neighbour y1,x1 of x,y in direction dir
        dir:  1    2     3
              5  (x,y)   4
              6    7     8
    '''

    if dir == 0:
        return y,x
    if x == 0:
        if dir in (1,5,6):
            return None,None
        if y != 0:
            if dir == 2:
                return y-1,x
            if dir == 3:
                return y-1,x+1
        if y != ymax:
            if dir == 7:
                return y+1,x
            if dir == 8:
                return y+1,x+1
        if dir == 4:
            return y,x+1
    elif x == xmax:
        if dir in (3,4,8):
            return None,None
        if y != 0:
            if dir == 2:
                return y-1,x
            if dir == 1:
                return y-1,x-1
        if y != ymax:
            if dir == 7:
                return y+1,x
            if dir == 6:
                return y+1,x-1
        if dir == 5:
            return y,x-1
    if y == 0:
        if dir in (1,2,3):
            return None,None
        if x != 0:
            if dir == 5:
                return y,x-1
            if dir == 6:
                return y+1,x-1
        if x != xmax:
            if dir == 4:
                return y,x+1
            if dir == 8:
                return y+1,x+1
        if dir == 7:
            return y+1,x
    elif y == ymax:
        if dir in (6,7,8):
            return None,None
        if x != 0:
            if dir == 5:
                return y,x-1
            if dir == 1:
                return y-1,x-1
        if x != xmax:
            if dir == 4:
                return y,x+1
            if dir == 3:
                return y-1,x+1
        if dir == 2:
            return y-1,x
    else:
        if dir == 1:
            return y-1,x-1
        if dir == 2:
            return y-1,x
        if dir == 3:
            return y-1,x+1
        if dir == 4:
            return y,x+1
        if dir == 8:
            return y+1,x+1
        if dir == 7:
            return y+1,x
        if dir == 6:
            return y+1,x-1
        if dir == 5:
            return y,x-1


def get_neighbour(lis,dir,x,y):
    '''
    lis = is_coin
    '''
    xmax = len(lis[0])-1
    ymax = len(lis)-1
    y1,x1 = direction(dir,x,y,xmax,ymax)
    if y1 != None:
        return lis[y1][x1]
    return None


def game_state(lis):
    '''
        check all neighbours. If same color, check neigbours in same direction
        if same color in a given direction, check the next coin in the same direction and count 1
    '''
    if lis == None:
        return None
    if len(lis[0]) == 1:
        return None
    if all([lis[0][i]!=0 for i in range(7)]):
        return 'Tie'
    xmax = len(lis[0])-1
    ymax = len(lis)-1
    for x in range(7):
        y = 5
        while y >= 0 and lis[y][x] != 0:    #check only values which are != from 0
            color = lis[y][x]
            for dir in range(1,5):
                count = 1
                nei = get_neighbour(lis,dir,x,y)
                if nei == color:
                    count += 1
                    y1,x1 = direction(dir,x,y,xmax,ymax)
                    if y1 != None:
                        if get_neighbour(lis,dir,x1,y1) == color:
                            count += 1
                            y2,x2 = direction(dir,x1,y1,xmax,ymax)
                            if y2 != None:
                                if get_neighbour(lis,dir,x2,y2) == color:
                                    count += 1

                dir = 9 - dir        #opposite direction
                nei = get_neighbour(lis,dir,x,y)
                if nei == color:
                    count += 1
                    y1,x1 = direction(dir,x,y,xmax,ymax)
                    if y1 != None:
                        if get_neighbour(lis,dir,x1,y1) == color:
                            count += 1
                            y2,x2 = direction(dir,x1,y1,xmax,ymax)
                            if y2 != None:
                                if get_neighbour(lis,dir,x2,y2) == color:
                                    count += 1

                if count >= 4:          #puissance n => end the game
                    return color
            y -= 1
    return None

def play_coin(is_coin_var,game_str,whosplaying):
    '''
        update is_coin
    '''
    choice = [i for i in range(7)]
    is_coin_var_2 = copy.deepcopy(is_coin_var)
    game_str_2 = copy.deepcopy(game_str)
    has_played = False
    while not has_played:
        r = random.choice(choice)
        if is_coin_var_2[0][r] == 0:   #top of the game
            has_played = True
            j = 0
            while j < 6 and is_coin_var_2[j][r] == 0:
                j += 1
            is_coin_var_2[j-1][r] = whosplaying
            game_str_2 += str(r+1)
            return is_coin_var_2,game_str_2

is_coin = [[0 for _ in range(7)] for _ in range(6)]
# 0 if no coin
# 1 if red coin
# 2 if yellow coin

which_row_to_play = [1 for _ in range(7)]

game_str = ''

list_game_str = [game_str]

list_corresp_outp = [0]
#0 if no winner
#1 if red wins
#2 if yellow wins

player = 1

for _ in range(100):
    is_coin = [[0 for _ in range(7)] for _ in range(6)]   #initialize a new game
    game_str = ''
    state = game_state(is_coin)
    while state == None:
        if game_str not in list_game_str:
            list_game_str.append(game_str)
            list_corresp_outp.append(0)

        new_is_coin, new_game_str = play_coin(is_coin,game_str,player)  #play in the list and in the string
        player = abs(player - 3)
        is_coin, game_str = new_is_coin, new_game_str
        state = game_state(is_coin)  #state of the game

        # print(game_str,'\n')
        # for i in is_coin:
        #     print(i)
        # print('')
        # print(list_corresp_outp[-1],'\n')

    if game_str not in list_game_str:
        list_game_str.append(game_str)
        if state == 'Tie':
            list_corresp_outp.append(0)
        else:
            list_corresp_outp.append(state)

print(list_game_str,'\n')
print('')
print(list_corresp_outp,'\n')




    # player_play = ''
    # player_play = input('Player {}, choose a column between 1 and 7: '.format(player))
    # if player_play == 'exit':
    #     break
    # player = abs(player - 3)
    # game_str += str(player_play)
    # print(game_str)
