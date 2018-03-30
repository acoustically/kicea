from kicea import Cursor
from kicea import Screen
from kicea import Window, Location
from kicea import TextBox
from kicea import View
from getch import getch
import time
import sys

Screen.clear()
screen_width, screen_height = Screen.size()

view = View(Location(10, 10), 10, 10)
text_box = TextBox(Location(10, 10), "test")
text_box.set_background(255, 0, 0)
view.add_view(text_box)
print(text_box.parent)
view.open()


key = getch()


Screen.print(key)

