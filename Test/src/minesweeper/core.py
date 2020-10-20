'''
Created on Oct 17, 2020

@author: Filipe
'''

import numpy as np
import random as rng
import os

os.system('clear')
MAX_RETRIES = 1000

class MinesweeperGame:
    def __init__(self, lines, columns, bombs):
        self.lines = lines
        self.columns = columns
        self.bombs = bombs
        self.field = np.zeros((lines, columns), dtype=int)
        
    def inside_range(self, line, column):
        try:
            if line < 0 or column < 0: raise IndexError("list index out of range")
            _ = self.field[line][column]
            return True
        except IndexError:
            return False

    def is_bomb(self, line, column):
        return self.inside_range(line, column) and self.field[line][column] == 9

    def is_bomb_or_field_limit(self, line, column):
        return (not self.inside_range(line, column)) or self.field[line][column] == 9
    
    def is_corner(self, line, column):
        return (line == 0 or line == self.lines - 1) and (column == 0 or column == self.columns - 1)

    def is_near_center(self, testL, testC, centerL, centerC):
        lineCheck = testL >= centerL - 1 and testL <= centerL + 1
        columnCheck = testC >= centerC - 1 and testC <= centerC + 1
        return lineCheck and columnCheck

    def is_surrounded(self, line, column):
        ul = self.is_bomb_or_field_limit(line - 1, column - 1)
        un = self.is_bomb_or_field_limit(line - 1, column)
        ur = self.is_bomb_or_field_limit(line - 1, column + 1)
        nl = self.is_bomb_or_field_limit(line, column - 1)
        nr = self.is_bomb_or_field_limit(line, column + 1)
        dl = self.is_bomb_or_field_limit(line + 1, column - 1)
        dn = self.is_bomb_or_field_limit(line + 1, column)
        dr = self.is_bomb_or_field_limit(line + 1, column + 1)
        
        return ul and un and ur and nl and nr and dl and dn and dr

    def update_bomb_count(self, line, column):
        if not self.is_bomb_or_field_limit(line - 1, column - 1): self.field[line - 1][column - 1] += 1
        if not self.is_bomb_or_field_limit(line - 1, column): self.field[line - 1][column] += 1
        if not self.is_bomb_or_field_limit(line - 1, column + 1): self.field[line - 1][column + 1] += 1
        if not self.is_bomb_or_field_limit(line, column - 1): self.field[line][column - 1] += 1
        if not self.is_bomb_or_field_limit(line, column + 1): self.field[line][column + 1] += 1
        if not self.is_bomb_or_field_limit(line + 1, column - 1): self.field[line + 1][column - 1] += 1
        if not self.is_bomb_or_field_limit(line + 1, column): self.field[line + 1][column] += 1
        if not self.is_bomb_or_field_limit(line + 1, column + 1): self.field[line + 1][column + 1] += 1

    def put_bomb(self, line, column, centerL, centerC):
        
        isBomb = self.is_bomb_or_field_limit(line, column)
        isSurounded = self.is_surrounded(line, column)
        isCorner = self.is_corner(line, column)
        isNearCenter = self.is_near_center(line, column, centerL, centerC)
        
        if isBomb or isSurounded or isCorner or isNearCenter: return False
        
        cell = self.field[line][column]
        self.field[line][column] = 9
        
        ul = self.is_bomb(line - 1, column - 1) and self.is_surrounded(line - 1, column - 1)
        un = self.is_bomb(line - 1, column) and self.is_surrounded(line - 1, column)
        ur = self.is_bomb(line - 1, column + 1) and self.is_surrounded(line - 1, column + 1)
        nl = self.is_bomb(line, column - 1) and self.is_surrounded(line, column - 1)
        nr = self.is_bomb(line, column + 1) and self.is_surrounded(line, column + 1)
        dl = self.is_bomb(line + 1, column - 1) and self.is_surrounded(line + 1, column - 1)
        dn = self.is_bomb(line + 1, column) and self.is_surrounded(line + 1, column)
        dr = self.is_bomb(line + 1, column + 1) and self.is_surrounded(line + 1, column + 1)
        
        neighborOK = not (ul or un or ur or nl or nr or dl or dn or dr)
        
        if not neighborOK:
            self.field[line][column] = cell
            return False
        else:
            self.update_bomb_count(line, column)
            return True

    def generate_field(self, centerL, centerC):
        bombsDeployed = 0
        maxRetries = MAX_RETRIES
        for _ in range(self.bombs):
            while maxRetries > 0:
                line = rng.randint(0, self.lines)
                column = rng.randint(0, self.columns)
                if self.put_bomb(line, column, centerL, centerC):
                    maxRetries = MAX_RETRIES
                    bombsDeployed += 1
                    break;
                maxRetries -= 1
            if maxRetries == 0: break                
        bombsLeft = self.bombs - bombsDeployed
        self.bombs -= bombsLeft
































    