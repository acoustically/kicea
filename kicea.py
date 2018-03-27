from cursor.cursor import Cursor
from screen.screen import Screen
from getch import getch
import time
import sys

Screen.clear()
screen_width, screen_height = Screen.size()
print(str(screen_width) + " " + str(screen_height))
key = getch()
Screen.print(key)

