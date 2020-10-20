'''
Created on Oct 20, 2020

@author: Filipe
'''

from sty import fg
from core import MinesweeperGame

l  = int(input("Lines:   "))
c  = int(input("Columns: "))
r  = int(input("Bombs:   "))
cL = int(input("X:       ")) - 1
cC = int(input("Y:       ")) - 1
game = MinesweeperGame(l, c, r)
game.generate_field(cL, cC)
print("\nDeployed bomb count: " + str(game.bombs) + "\n")
for line in game.field:
    for cell in line:
        cellChar = ""
        if cell == 0:
            cellChar = fg(90, 90, 90) + "." + fg.rs
        elif cell == 1:
            cellChar = fg(0, 0, 255) + "1" + fg.rs
        elif cell == 2:
            cellChar = fg(0, 100, 220) + "2" + fg.rs
        elif cell == 3:
            cellChar = fg(0, 200, 180) + "3" + fg.rs
        elif cell == 4:
            cellChar = fg(0, 255, 0) + "4" + fg.rs
        elif cell == 5:
            cellChar = fg(200, 255, 10) + "5" + fg.rs
        elif cell == 6:
            cellChar = fg(255, 255, 20) + "6" + fg.rs
        elif cell == 7:
            cellChar = fg(255, 127, 30) + "7" + fg.rs
        elif cell == 8:
            cellChar = fg(255, 60, 30) + "8" + fg.rs
        elif cell == 9:
            cellChar = fg.red + "*" + fg.rs
        
        print(cellChar, end = " ")
    print("")