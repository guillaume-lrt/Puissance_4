# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 18:26:56 2018

@author: Guillaume
"""

import pygame, os
import time
import random
import copy

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()


display_width = 1000
display_height = 850

puissance_n = 4 #choose a number between 3 and 4

'''colors'''
black = (0,0,0)
white = (255,255,255)
red = (235, 0, 0)
yellow = (235,200, 0)

'''Textes'''

def write_text(text,font,size,color):
    return pygame.font.SysFont(font,size).render(text,True,color)

text_red = write_text("Red Won","arial",150,red)
text_yellow = write_text("Yellow Won",'arial',150,yellow)
text_tie = write_text("It's A Tie",'arial',150,white)
texte_intro_1 = write_text("Move With ← and →", 'arial',75, white)
texte_intro_2 = write_text("Press 'space' To Play", 'arial',75, white)
texte_intro_two_player_white = write_text("Two Players",'arial',75,white)
texte_intro_IA_white = write_text("IA",'arial',75,white)
texte_intro_two_player_black = write_text("Two Players",'arial',75,black)
texte_intro_IA_black = write_text("IA",'arial',75,black)
texte_play_again = write_text("Press 'space' To Play Again",'arial',75,white)
texte_exit_white = write_text("Exit",'arial',75,white)
texte_exit_black = write_text("Exit",'arial',75,black)

'''Display the window'''
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Puissance 4')
clock = pygame.time.Clock()

'''Images'''
TitleImg_1 = pygame.image.load('Title_1.png')
TitleImg_2 = pygame.image.load('Title_2.png')
BoardImg = pygame.image.load('Board.png')
Yellow_boardImg = pygame.image.load('Yellow_board.png')
YellowImg = pygame.image.load('Yellow.png')
Red_boardImg = pygame.image.load('Red_board.png')
RedImg = pygame.image.load('Red.png')

x_size = 800
TitleImg_1 = pygame.transform.scale(TitleImg_1,(x_size,int(int(x_size*262)/1202)))
TitleImg_2 = pygame.transform.scale(TitleImg_2,(x_size,int(int(x_size*256)/1183)))
BoardImg = pygame.transform.scale(BoardImg, (x_size, int(int(x_size*1498)/1730)))
RedImg = pygame.transform.scale(RedImg, (int(203*(x_size/1730)),int(204*(x_size/1730))))
YellowImg = pygame.transform.scale(YellowImg, (int(203*(x_size/1730)),int(204*(x_size/1730))))
Red_boardImg = pygame.transform.scale(Red_boardImg, (int(216*(x_size/1730)),int(214*(x_size/1730))))
Yellow_boardImg = pygame.transform.scale(Yellow_boardImg, (int(216*(x_size/1730)),int(214*(x_size/1730))))


'''Display Images'''
def Title(Img,x,y):
    gameDisplay.blit(Img,(x,y))

def Board(x,y):
    gameDisplay.blit(BoardImg, (x,y))

def Yellow_board(x,y):
    gameDisplay.blit(Yellow_boardImg, (x,y))

def Yellow(x,y):
    gameDisplay.blit(YellowImg, (x,y))

def Red_board(x,y):
    gameDisplay.blit(Red_boardImg, (x,y))

def Red(x,y):
    gameDisplay.blit(RedImg, (x,y))

def plus(a,b):
    return tuple(map(sum, zip(a, b)))

def display_text(text,width,height):
    '''
        center if width = 0 and height = 0
    '''
    gameDisplay.blit(text,
        ((display_width - text.get_width()) // 2 + width, (display_height - text.get_height()) // 2 + height))
    pygame.display.flip()


x_board = display_width*0.1
y_board = display_height*0.15


x_red = display_width*2
y_red = display_height*2
x_yellow = display_width*2
y_yellow = display_height*2


dx = 0.1115      #space between the x coordinates of two coins
dy = 0.112       #space between the y coordinates of two coins

coordinates = [[(round(0.117+dx*i,6)*1000,round(0.698-dy*j,6)*1000) for i in range(0,7)] for j in range(5,-1,-1)]
'''
coordinates =
[(117.0, 138.0), (228.5, 138.0), (340.0, 138.0), (451.5, 138.0), (563.0, 138.0), (674.5, 138.0), (786.0, 138.0)]
[(117.0, 250.0), (228.5, 250.0), (340.0, 250.0), (451.5, 250.0), (563.0, 250.0), (674.5, 250.0), (786.0, 250.0)]
[(117.0, 362.0), (228.5, 362.0), (340.0, 362.0), (451.5, 362.0), (563.0, 362.0), (674.5, 362.0), (786.0, 362.0)]
[(117.0, 474.0), (228.5, 474.0), (340.0, 474.0), (451.5, 474.0), (563.0, 474.0), (674.5, 474.0), (786.0, 474.0)]
[(117.0, 586.0), (228.5, 586.0), (340.0, 586.0), (451.5, 586.0), (563.0, 586.0), (674.5, 586.0), (786.0, 586.0)]
[(117.0, 698.0), (228.5, 698.0), (340.0, 698.0), (451.5, 698.0), (563.0, 698.0), (674.5, 698.0), (786.0, 698.0)]
'''

x_position = [round(0.117+dx*i,6)*1000 for i in range(7)]
'''
[117.0, 228.5, 340.0, 451.5, 563.0, 674.5, 786.0]
'''

is_coin = [[0 for _ in range(7)] for _ in range(6)]
# 0 if no coin
# 1 if red coin
# 2 if yellow coin

interval = [(round(0.1+dx*i,6)*1000,round(0.16+dx*i,6)*1000) for i in range(7)]
'''
[(0.1, 0.16), (0.2115, 0.2715), (0.323, 0.383), (0.4345, 0.4945), (0.546, 0.606), (0.6575, 0.7175), (0.769, 0.829)]
'''

def button (msg, x, y, w, h, nc, nct, mc, mct, action=None ):
    '''
        x: x position of the left corner of the button
        y: y position
        w: width
        h: height
        nc: normal color
        nct: normal color text
        mc: mouse color
        mct: mouse color text
    '''
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    bool = False
    two_player = False
    IA = False

    if (x+w > mouse[0] > x) and (y+h > mouse[1] > y):   #underliing effect of the mouse
        text_choice = write_text(msg,"freesansbold.ttf",50,mct)
        pygame.draw.rect(gameDisplay, mc, (x, y, w, h))
        gameDisplay.blit(text_choice,(x+(w//2), y+(h//2)))
        pygame.display.flip()

        if (click[0] == 1 and action != None):
            if  (action == "two_player"):
                two_player = True
                IA = False
            elif  (action == "IA"):
                 IA = True
                 two_player = False
            bool = True

    else:
        text_choice = write_text(msg,"freesansbold.ttf",50,nct)
        gameDisplay.blit(text_choice,(x+(w//2), y+(h//2)))
        pygame.display.flip()

    return bool,two_player,IA


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
            return None
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
            return None
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
            return None
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
            return None
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
    if direction(dir,x,y,xmax,ymax) == None:
        return None
    else:
        y1,x1 = direction(dir,x,y,xmax,ymax)
        return lis[y1][x1]


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
        while y >= 0 and lis[y][x] != 0:
            color = lis[y][x]
            for dir in range(1,5):
                count = 1
                nei = get_neighbour(lis,dir,x,y)
                if nei == color:
                    count += 1
                    if direction(dir,x,y,xmax,ymax) != None:
                        y1,x1 = direction(dir,x,y,xmax,ymax)
                        if get_neighbour(lis,dir,x1,y1) == color:
                            count += 1
                            if direction(dir,x1,y1,xmax,ymax) != None:
                                y2,x2 = direction(dir,x1,y1,xmax,ymax)
                                if get_neighbour(lis,dir,x2,y2) == color:
                                    count += 1

                dir = 9 - dir        #opposite direction
                nei = get_neighbour(lis,dir,x,y)
                if nei == color:
                    count += 1
                    if direction(dir,x,y,xmax,ymax) != None:
                        y1,x1 = direction(dir,x,y,xmax,ymax)
                        if get_neighbour(lis,dir,x1,y1) == color:
                            count += 1
                            if direction(dir,x1,y1,xmax,ymax) != None:
                                y2,x2 = direction(dir,x1,y1,xmax,ymax)
                                if get_neighbour(lis,dir,x2,y2) == color:
                                    count += 1

                if count >= puissance_n:          #puissance n => end the game
                    return color
            y -= 1
    return None

def display_game(whosplaying,x_change_counter,is_coin):
    for i in range(6):
        for j in range(7):
            if is_coin[i][j] != 0:
                x,y = coordinates[i][j]
                if is_coin[i][j] == 1:  #red coin
                    Red_board(x,y)
                else:                   #yellow coin
                    Yellow_board(x,y)
    Board(x_board,y_board)

def play_coin(x,is_coin_var,whosplaying):
    '''
        update is_coin
    '''
    is_coin_var_2 = copy.deepcopy(is_coin_var)
    is_interval = [A[0] <= x <= A[1] for A in interval]
    has_played = False
    for i in range(7):
        if is_interval[i] == True:
            if is_coin_var_2[0][i] == 0:
                has_played = True
                j = 0
                while j < 6 and is_coin_var_2[j][i] == 0:
                    j += 1
                is_coin_var_2[j-1][i] += whosplaying + 1
                return has_played,is_coin_var_2
    return has_played,is_coin_var_2


def IA_play(is_coin):
    '''
        IA is player 2 i.e yellow
        Assume it is IA turn to play i.e whosplaying == 1
    '''
    is_coin_v = copy.deepcopy(is_coin)
    choice = [i for i in range(7)]
    for i in range(7):
        has_played,is_coin_2 = play_coin(x_position[i],is_coin_v,1)    #IA plays
        if has_played:
            result = game_state(is_coin_2)
            if result == 2:
                return i

    for j in range(7):
        has_played,is_coin_3 = play_coin(x_position[j],is_coin_v,0)   #player plays
        if has_played:
            result = game_state(is_coin_3)
            if result == 1:   #if player has a winning play
                return j

    for i in range(7):
        has_played,is_coin_2 = play_coin(x_position[i],is_coin_v,1)   #IA plays
        if has_played:
            for t in range(7):
                A = [game_state(play_coin(x_position[t],play_coin(x_position[j],is_coin_2,0)[1],1)[1]) == 2 for j in range(7)]
                if sum(A) >= 5:  #if for 5 play j over 7 by player, \exist a winning play 't'
                    return i

                if any([game_state(play_coin(x_position[j],play_coin(x_position[t],is_coin_2,1)[1],0)[1]) == 1 for j in range(7)]):  #IA plays, if \exist a winning play j
                    return i
    r = random.choice(choice)
    print('Random: ',r)
    return r

whosplaying = 0

x_change, y_change = 0, 0

x_change_counter = 3

two_player, IA = False, False

left, right = False, False

text_width = texte_intro_two_player_black.get_width()+10
text_height = texte_intro_two_player_black.get_height()


done = False   #welcome screen
while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
                right = False
            if event.key == pygame.K_RIGHT:
                right = True
                left = False
        # bool,two_player,IA = button ("Two Player", display_width//2 - 75, display_height//2 - 50, 500, 100, white, black, black, white, "two_player" )
        # bool,two_player,IA = button ("IA", display_width//2 - 75, display_height//2 - 50, 150, 100, white, black, black, white, "IA" )
        # if bool:
            # done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if left:
                    two_player = True
                    done = True
                elif right:
                    IA = True
                    done = True

        if event.type == pygame.QUIT:
            quit()

    gameDisplay.fill(black)
    Title(TitleImg_2,(display_width - TitleImg_2.get_width()) // 2,50)
    display_text(texte_intro_1,0,-100)
    display_text(texte_intro_2,0,50)
    if left:
        pygame.draw.rect(gameDisplay,white,(130,585,text_width,text_height))
        display_text(texte_intro_two_player_black,-200,200)
    if right:
        pygame.draw.rect(gameDisplay,white,(530,585,text_width,text_height))
        display_text(texte_intro_IA_black,200,200)
    if not left:
        #pygame.draw.rect(gameDisplay,white,(125,600,text_tp_width,text_tp_height))
        display_text(texte_intro_two_player_white,-200,200)
    if not right:
        display_text(texte_intro_IA_white,200,200)
    pygame.display.update()
    clock.tick(10)


left, right, down = False, False, False
done = False
while not done:
    if two_player:
        crashed = False
        while not crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

        #whosplaying

                if whosplaying == 0 and x_red == display_width*2 and y_red == display_height*2:
                    x_red = display_width*0.45
                    y_red = display_height*0.01
                if whosplaying == 1 and x_yellow == display_width*2 and y_yellow == display_height*2:
                    x_yellow = display_width*0.45
                    y_yellow = display_height*0.01

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if x_change_counter > 0:
                            x_change_counter -= 1
                    elif event.key == pygame.K_RIGHT:
                        if x_change_counter < 6:
                            x_change_counter += 1


            #change turn
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        x = x_position[x_change_counter]
                        has_played,is_coin = play_coin(x,is_coin,whosplaying)
                        if has_played:
                            whosplaying = abs(whosplaying-1)
                            x_change_counter = 3

        #delta x = 0.1115

        #delta y = 0.132

            if whosplaying == 0:
                x_red = x_position[x_change_counter]
                y_red = display_height*0.01
                x_yellow = display_width*2
                y_yellow = display_height*2
            if whosplaying == 1:
                x_yellow = x_position[x_change_counter]
                y_yellow = display_height*0.01
                x_red = display_width*2
                y_red = display_height*2

            gameDisplay.fill(black)
            Red(x_red,y_red)
            Yellow(x_yellow,y_yellow)

            display_game(whosplaying,x_change_counter,is_coin)

            pygame.display.update()
            clock.tick(60)

            result = game_state(is_coin)
            if result == 1:
                display_text(text_red,0,-360)
                crashed = True
            if result == 2:
                display_text(text_yellow,0,-360)
                crashed = True
            if result == 'Tie':
                display_text(text_tie,0,-360)
                crashed = True

    if IA:
        crashed = False
        while not crashed:
            if whosplaying == 0:
                x_red = x_position[x_change_counter]
                y_red = display_height*0.01
                x_yellow = display_width*2
                y_yellow = display_height*2

            gameDisplay.fill(black)
            Red(x_red,y_red)

            display_game(whosplaying,x_change_counter,is_coin)

            pygame.display.update()
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                if whosplaying == 0 and x_red == display_width*2 and y_red == display_height*2:
                    x_red = display_width*0.45
                    y_red = display_height*0.01
                if whosplaying == 1 and x_yellow == display_width*2 and y_yellow == display_height*2:
                    x_yellow = display_width*0.45
                    y_yellow = display_height*0.01

                if whosplaying == 0:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            if x_change_counter > 0:
                                x_change_counter -= 1
                        elif event.key == pygame.K_RIGHT:
                            if x_change_counter < 6:
                                x_change_counter += 1
                #change turn
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            x = x_position[x_change_counter]
                            has_played,is_coin = play_coin(x,is_coin,whosplaying)
                            if has_played:
                                x_change_counter = 3
                                whosplaying = abs(whosplaying-1)
                            has_played = False

            result = game_state(is_coin)
            if result == 1:
                display_text(text_red,0,-360)
                crashed = True
                whosplaying = 0
            if result == 2:
                display_text(text_yellow,0,-360)
                crashed = True
                whosplaying = 0
            if result == 'Tie':
                display_text(text_tie,0,-360)
                crashed = True
                whosplaying = 0

            if whosplaying == 1:
                x = random.choice([2,4])
                if  is_coin[-1][3] == 0:
                    is_coin[-1][3] = 2
                    has_played = True

                elif is_coin[-1][x] == 0:
                    is_coin[-1][x] = 2
                    has_played = True
                else:
                    has_played,is_coin_bis = play_coin(x_position[IA_play(is_coin)],is_coin,whosplaying)
                    if has_played:
                        is_coin = is_coin_bis
                if not has_played:
                    while not has_played:
                        print('WHILE')
                        has_played,is_coin_bis = play_coin(x_position[IA_play(is_coin)],is_coin,whosplaying)
                    is_coin = is_coin_bis
                x_change_counter = 3
                whosplaying = abs(whosplaying-1)
                has_played = False

    two_player, IA = False, False

# Play again

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
                right = False
                down = False
            if event.key == pygame.K_RIGHT:
                right = True
                left = False
                down = False
            if event.key == pygame.K_DOWN:
                left = False
                right = False
                down = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if left:
                    two_player = True
                elif right:
                    IA = True
                if left or right:
                    whosplaying = 0
                    x_change = 0
                    y_change = 0
                    x_change_counter = 3
                    is_coin = [[0 for _ in range(7)] for _ in range(6)]
                if down:
                    quit()

        if event.type == pygame.QUIT:
            quit()

    x_yellow = display_width*2
    y_yellow = display_height*2
    x_red = display_width*2
    y_red = display_height*2

    gameDisplay.fill(black)
    Red(x_red,y_red)
    Yellow(x_yellow,y_yellow)

    display_game(whosplaying,x_change_counter,is_coin)
    result = game_state(is_coin)
    if result == 1:
        #red won
        display_text(text_red,0,-360)
    if result == 2:
        #yellow won
        display_text(text_yellow,0,-360)
    if result == 'Tie':
        # it's a tie
        display_text(text_tie,0,-360)

    display_text(texte_play_again,0,-100)
    if left:
        pygame.draw.rect(gameDisplay,white,(130,585,text_width,text_height))
        display_text(texte_intro_two_player_black,-200,200)
    if right:
        pygame.draw.rect(gameDisplay,white,(530,585,text_width,text_height))
        display_text(texte_intro_IA_black,200,200)
    if down:
        pygame.draw.rect(gameDisplay,white,(330,700,text_width,text_height))
        display_text(texte_exit_black,0,315)

    if not left:
        display_text(texte_intro_two_player_white,-200,200)
    if not right:
        display_text(texte_intro_IA_white,200,200)
    if not down:
        display_text(texte_exit_white,0,315)

    pygame.display.update()
    clock.tick(10)


pygame.quit()
quit()
