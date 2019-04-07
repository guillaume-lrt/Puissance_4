# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 18:26:56 2018

@author: Guillaume
"""

import pygame, os
import time

class Image():

    x_size = 800

    def __init__(self):
        BoardImg = pygame.image.load('Board.png')
        Yellow_boardImg = pygame.image.load('Yellow_board.png')
        YellowImg = pygame.image.load('Yellow.png')
        Red_boardImg = pygame.image.load('Red_board.png')
        RedImg = pygame.image.load('Red.png')

        self.Board = pygame.transform.scale(BoardImg, (x_size, int(int(x_size*1498)/1730)))
        self.Red = pygame.transform.scale(RedImg, (int(203*(x_size/1730)),int(204*(x_size/1730))))
        self.Yellow = pygame.transform.scale(YellowImg, (int(203*(x_size/1730)),int(204*(x_size/1730))))
        self.Red_board = pygame.transform.scale(Red_boardImg, (int(216*(x_size/1730)),int(214*(x_size/1730))))
        self.Yellow_board = pygame.transform.scale(Yellow_boardImg, (int(216*(x_size/1730)),int(214*(x_size/1730))))

class style():

    class text():
        def __init__(self,Font,size,texte,color):
            ''' font = "timesnewroman"
                size = 175'''
            self.a = pygame.font.SysFont(Font,size).render(texte, True, color)

    class color():
        def __init__(self):
            self.black = (0,0,0)
            self.white = (255,255,255)
            self.red = (235,40,40)
            self.yellow = (255,200,15)


# style.text("timesnewroman",175,"Red Won",style.color.white).a



class game():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()

    def __init__(self):
        self.puissance = 4




    def loop(self):
        crashed = False

        while not crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True

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
                        x = min(x_red,x_yellow)
                        is_interval = [A[0] <= x <= A[1] for A in interval]
                        for i in range(7):
                            if is_interval[i] == True:
                                if is_coin[0][i] == 0:
                                    j = 0
                                    while j < 6 and is_coin[j][i] == 0:
                                        j += 1
                                    is_coin[j-1][i] += whosplaying + 1
                                    whosplaying = abs(whosplaying-1)
                                    x_change_counter = 3



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

            gameDisplay.fill(white)
            Red(x_red,y_red)
            Yellow(x_yellow,y_yellow)
            for i in range(6):
                for j in range(7):
                    if is_coin[i][j] != 0:
                        x,y = coordinates[i][j]
                        if is_coin[i][j] == 1:  #red coin
                            Red_board(x,y)
                        else:                   #yellow coin
                            Yellow_board(x,y)

            Board(x_board,y_board)

            pygame.display.update()
            clock.tick(60)

            result = game_state(is_coin)
            if result == 1:
                print('Red Won')
                display_text(text_red)
                time.sleep(5)
                pygame.quit()
                quit()
            if result == 2:
                print('Yellow Won')
                display_text(text_yellow)
                time.sleep(5)
                pygame.quit()
                quit()

        pygame.quit()
        quit()








os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

font = pygame.font.SysFont("timesnewroman", 175)

text_red = font.render("Red Won", True, (235, 0, 0))
text_yellow = font.render("Yellow Won", True, (235,200, 0))

display_width = 1000
display_height = 850

puissance_n = 4 #choose a number between 3 and 4

black = (0,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Puissance 4')
clock = pygame.time.Clock()



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

def display_text(text):
    gameDisplay.blit(text,
        (display_width // 2 - text.get_width() // 2, display_height // 2 - text.get_height() // 2 - 375))
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

is_coin = [[0 for _ in range(7)] for _ in range(6)]
# 0 if no coin
# 1 if red coin
# 2 if yellow coin

interval = [(round(0.1+dx*i,6)*1000,round(0.16+dx*i,6)*1000) for i in range(7)]
'''
[(0.1, 0.16), (0.2115, 0.2715), (0.323, 0.383), (0.4345, 0.4945), (0.546, 0.606), (0.6575, 0.7175), (0.769, 0.829)]
'''

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
    '''check all neighbours. If same color, check neigbours in same direction '''
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



whosplaying = 0

x_change = 0
y_change = 0

x_change_counter = 3

crashed = False

def game_loop():
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

    #whosplaying


            if whosplaying == 0 and x_red == display_width*2 and y_red == display_height*2:
                x_red = display_width*0.45
                y_red = display_height*0.01
            if whosplaying == 1 and x_yellow == display_width*2 and y_yellow == display_height*2:
                x_yellow = display_width*0.45
                y_yellow = display_height*0.01


    #deplacement

    #        if event.type == pygame.KEYDOWN:
    #            if event.key == pygame.K_LEFT:
    #                x_change = -10
    #            elif event.key == pygame.K_RIGHT:
    #                x_change = 10
    #        if event.type == pygame.KEYUP:
    #            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
    #                x_change = 0
    #        if event.type == pygame.KEYDOWN:
    #            if event.key == pygame.K_UP:
    #                y_change = -4
    #            elif event.key == pygame.K_DOWN:
    #                y_change = 4
    #        if event.type == pygame.KEYUP:
    #            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
    #                y_change = 0

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
                    x = min(x_red,x_yellow)
                    is_interval = [A[0] <= x <= A[1] for A in interval]
                    for i in range(7):
                        if is_interval[i] == True:
                            if is_coin[0][i] == 0:
                                j = 0
                                while j < 6 and is_coin[j][i] == 0:
                                    j += 1
                                is_coin[j-1][i] += whosplaying + 1
                                whosplaying = abs(whosplaying-1)
                                x_change_counter = 3


    #delta x = 0.1115

    #delta y = 0.132
        if whosplaying == 0:
            #x_red += x_change
            #y_red += y_change
            x_red = x_position[x_change_counter]
            y_red = display_height*0.01
            x_yellow = display_width*2
            y_yellow = display_height*2
        if whosplaying == 1:
            x_yellow = x_position[x_change_counter]
            y_yellow = display_height*0.01
            x_red = display_width*2
            y_red = display_height*2

        gameDisplay.fill(white)
        Red(x_red,y_red)
        Yellow(x_yellow,y_yellow)
        for i in range(6):
            for j in range(7):
                if is_coin[i][j] != 0:
                    x,y = coordinates[i][j]
                    if is_coin[i][j] == 1:  #red coin
                        Red_board(x,y)
                    else:                   #yellow coin
                        Yellow_board(x,y)

        Board(x_board,y_board)

        pygame.display.update()
        clock.tick(60)

        result = game_state(is_coin)
        if result == 1:
            print('Red Won')
            # screen.fill((255, 255, 255))
            display_text(text_red)
            time.sleep(5)
            pygame.quit()
            quit()
        if result == 2:
            print('Yellow Won')
            display_text(text_yellow)
            time.sleep(5)
            pygame.quit()
            quit()

    pygame.quit()
    quit()


game_loop()
