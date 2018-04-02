from kicea.window.window import Window, Location
from kicea.window.view_child.view_child import ViewChild
from kicea.window.color import Color
from kicea.screen.screen import Screen
from kicea.screen.cursor.cursor import Cursor

class TextBox(ViewChild):
    
    def __init__(self, location, text):
        self.__foreground = -1
        self.__text = text
        super().__init__(location, len(text), 1)

    def set_location(self, location):
        self._close()
        super().set_location(location)
        self._open()
    
    def set_width(self, width):
        if(len(text) < width):
            width = len(text)
        self._close()
        super().set_width(width)
        self._open()

    def set_text_color(self, *args):
        if(len(args) == 3):
            self.__foreground = Color.foreground(args[0], args[1], args[2])
     
    def _open(self):
        Cursor.move(super().get_location().x, super().get_location().y)
        if self.__foreground != -1:
            if self.get_background() != -1:
                Screen.print(super().get_background() + self.__foreground + self.__text)
            else:
                Screen.print(self.__foreground + self.__text)
        else:
            if super().get_background() != -1:
                Screen.print(super().get_background() + self.__text)    
            else:
                Screen.print(self.__text)    
      
        Color.reset()
