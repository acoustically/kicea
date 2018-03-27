import sys
from screen.screen import Screen

class Cursor():
    x = 0
    y = 0

    def move(x, y):
        Cursor.x = x
        Cursor.y = y
        Screen.print("\033[" + str(x) + ";" + str(y) + "H")
    
    def move_left(*x):
        if not x:
            Cursor.x -= 1
            Screen.print("\033[1D")
        else:
            Cursor.x -= x
            Screen.print("\033[" + str(x) + "D")

    def move_right(*x):
        if not x:
            Cursor.x += 1
            Screen.print("\033[1C")
        else:
            Cursor.x += x
            Screen.print("\033[" + str(x) + "C")
    
    def move_up(*y):
        if not y:
            Cursor.y -= 1
            Screen.print("\033[1A")
        else:
            Cursor.y -= y
            Screen.print("\033[" + str(x) + "A")
    
    def move_down(*y):
        if not y:
            Cursor.y += 1
            Screen.print("\033[1B")
        else:
            Cursor.y += y
            Screen.print("\033[" + str(x) + "B")
