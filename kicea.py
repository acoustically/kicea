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
text_box = TextBox(Location(0, 0), "test")
text_box.set_background(255, 0, 0)
view.add_view(text_box)

view.open()
getch()
view.close()

key = getch()


