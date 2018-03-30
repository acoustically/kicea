from kicea.window.window import Window, Location
from kicea.window.color import Color
from kicea.screen.screen import Screen
from kicea.screen.cursor.cursor import Cursor

class TextBox(Window):
    
    def __init__(self, location, text):
        self.__foreground = -1
        self.__text = text
        super().__init__(location, len(text), 1)

    @property  
    def location(self):
        return super().location

    @location.setter
    def location(self, location):
        self.close()
        super().location = location
        self.open()

    @property
    def width(self):
        return super().width 

    @width.setter
    def width(self, width):
        if(len(text) < width):
            width = len(text)
        self.close()
        super().width = width
        self.open()

    @property
    def height(self):
        return super().height 

    @height.setter
    def height(self, height):
        super().height = height
    
    def set_text_color(self, *args):
        if(len(args) == 3):
            self.__foreground = Color.foreground(args[0], args[1], args[2])
     
    def open(self):
        super().open()
        if self.__foreground != -1:
            Cursor.move(super().location.x, super().location.y)
            Screen.print(self.__foreground + super().background + self.__text)
            Color.reset()

