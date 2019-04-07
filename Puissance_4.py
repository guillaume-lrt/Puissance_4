# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 11:37:39 2018

@author: Guillaume
"""

#rouge = 1;31;47
#bleu = 1;34;47
#invisible = 1;37;47

import time
nb_column = 8
puissance = 4
vitesse = 0.2

class Puissance():
    def __init__(self,n,p,v):
        self.grid = [['\x1b[1;37;47m o' for i in range(n)] for j in range(n)]
        self.turn = 0
        self.n = n  #size
        self.p = p   #puissance(4 par default)
        self.v = v


    def rep_grid(self):
        for i in range(20):
            print('\n')
        t = 1
        while t < 10 and t < self.n+1:
            print(' ',t,'', end='')
            t += 1
        while t < self.n+1:
            print(' ',t,end='')
            t += 1
        print('')
        for i in range(self.n-1):
            print('┃',end='')
            for j in range(self.n):
                r = self.grid[i][j]
                print(r + '\x1b[0;0;0m','', end='')
                print('┃', end='')
                print('',end='')
            if i < self.n - 2:
                print('\n'+'┃'+('━━━┃')*(int(self.n) - 1) + '━━━┃')
        print('\n'+'┃'+('━━━━')*(int(self.n) - 1) + '━━━┃')

    def position(self,a):
        if a < 1 or a > self.n:
            return 'Not in the grid'
        else:
            i = 0
            while self.grid[i][a-1] != '\x1b[1;31;47m o' and self.grid[i][a-1] != '\x1b[1;34;47m o' and i < self.n-1:
                i += 1
            x,y = i-1,a-1
        return x,y

    def visualisation(self,a):
        if a < 1 or a > self.n:
            return 'Not in the grid'
        else:
            x,y = self.position(a)
            i = 0
            while i != x+1  and i < self.n-1:
                if self.turn == 0:
                    self.grid[i-1][y] = '\x1b[1;31;47m o'
                elif self.turn == 1:
                    self.grid[i-1][y] = '\x1b[1;34;47m o'
                self.rep_grid()
                self.grid[i-1][y] = '\x1b[1;37;47m o'
                time.sleep(self.v)
                i += 1
            x = i-1
            print('\x1b[1;37;47m x','\x1b[1;37;47m y' + '\x1b[0;0;0m')
            time.sleep(self.v)
            if self.turn == 0:
                self.grid[x][y] = '\x1b[1;31;47m o'
                self.turn = 1
            elif self.turn == 1:
                self.grid[x][y] = '\x1b[1;34;47m o'
                self.turn = 0

    def neighbours(self,x,y):
        dia1 = []
        dia2 = []
        col = []
        lin = []
#        print(x,y)
        i = 0
        while (x+i < self.n-1) and (y+i < self.n) and i < self.p:
            dia1.append(self.grid[x+i][y+i])
            i += 1
        i = 1
        while (x-i >= 0) and (y-i >= 0) and i < self.p:
            dia1.insert(0,self.grid[x-i][y-i])
            i += 1
        i = 0
        while (x+i < self.n-1) and (y-i >= 0) and i < self.p:
            dia2.append(self.grid[x+i][y-i])
            i += 1
        i = 1
        while (x-i >= 0) and (y+i < self.n) and i < self.p:
            dia2.insert(0,self.grid[x-i][y+i])
            i += 1
        i = 0
        while (x-i >= 0) and i < self.p:
            col.append(self.grid[x-i][y])
            i += 1
        i = 1
        while (x+i < self.n-1) and i < self.p:
            col.insert(0,self.grid[x+i][y])
            i += 1
        i = 0
        while (y-i >= 0) and i < self.p:
            lin.append(self.grid[x][y-i])
            i += 1
        i = 1
        while (y+i < self.n) and i < self.p:
            lin.insert(0,self.grid[x][y+i])
            i += 1
        return dia1,dia2,col,lin


    def win(self,a):
        status = 0
        A = ['\x1b[1;31;47m o' for i in range(self.p)]
        B = ['\x1b[1;34;47m o' for i in range(self.p)]
        x,y = self.position(a)
        D,E,C,L = self.neighbours(x+1,y)
#        print(L)
#        print(C)
        sep_col = [C[i:self.p+i] for i in range(len(C)-self.p+1)]
        sep_dia1= [D[i:self.p+i] for i in range(len(D)-self.p+1)]
        sep_dia2 = [E[i:self.p+i] for i in range(len(E)-self.p+1)]
        sep_lin = [L[i:self.p+i] for i in range(len(L)-self.p+1)]
#        print(A)
#        print(sep_lin)
#        print(sep_col)
        if A in sep_col:
            status = 1
        if B in sep_col:
            status = 2
        if A in sep_lin:
            status = 1
        if B in sep_lin:
            status = 2
        if A in sep_dia1:
            status = 1
        if B in sep_dia1:
            status = 2
        if A in sep_dia2:
            status = 1
        if B in sep_dia2:
            status = 2
        return status



    def play(self):
        self.rep_grid()
        a = input('Choose a column: ')
        a = int(a)
        self.visualisation(a)
        while self.win(a) == 0:
            self.rep_grid()
            a = input('Choose a column: ')
            a = int(a)
            self.visualisation(a)
        if self.win(a) == 1:
            self.rep_grid()
            print('\x1b[1;31;47m' + 'Red win'+ '\x1b[0;0;0m')
            runfile('C:/Users/ptitg/Documents/@CS projects/Puissance_4/Puissance_4.py', wdir='C:/Users/ptitg/Documents/@CS projects/Puissance_4')
        elif self.win(a) == 2:
            self.rep_grid()
            print('\x1b[1;34;47m' + 'Blue win'+ '\x1b[0;0;0m')
            runfile('C:/Users/ptitg/Documents/@CS projects/Puissance_4/Puissance_4.py', wdir='C:/Users/ptitg/Documents/@CS projects/Puissance_4')

a = Puissance(nb_column,puissance,vitesse)
a.play()
