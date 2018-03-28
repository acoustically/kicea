from kicea import Cursor
from kicea import Screen
from kicea import Window, Location
from kicea import TextBox
from getch import getch
import time
import sys

Screen.clear()
screen_width, screen_height = Screen.size()
window = Window(Location(10, 10), 20, 20)
print(window)
window.set_background(255, 0 ,0)
window.open()
key = getch()
window.close()
Cursor.move(1, 1)
key = getch()
text_box = TextBox(Location(20, 20), "test")
text_box.set_background(255, 0, 0)
text_box.set_text_color(0, 0, 255)
text_box.open()
key = getch()
text_box.close()
key = getch()


Screen.print(key)

