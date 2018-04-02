from kicea.screen.screen import Screen
from kicea.screen.cursor.cursor import Cursor
from kicea.window.color import Color

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return "<Location x = " + str(self.x) + " y = " + str(self.y) + ">"

class Window:
    def __init__(self, location, width, height):
        self.__location = location
        self.__width = width
        self.__height = height
        self.__background = -1
        self.__keydown_listener = None            
        self.__parent = None

    def get_location(self):
        return self.__location

    def set_location(self, location):
        if(type(location) is Location):
            self._close()
            self.__location = location
            self._open()

    def get_width(self):
        return self.__width

    def set_width(self, width):
        if(type(width) is int):
            self._close()
            self.__width = width
            self._open()

    def get_height(self):
        return self.__height
    
    def set_height(self, height):
        if(type(height) is int):
            self.close()
            self.__height = height
            self.open()
    
    def get_background(self):
        return self.__background
    
    def set_background(self, *args):
        if len(args) == 3:
            self.__background =  Color.background(args[0], args[1], args[2])
        else:
            raise Exception

    def _open(self):
        for j in range(self.__height):
            Cursor.move(self.__location.x, self.__location.y + j)
            blank = ""
            for i in range(self.__width):
                blank += " "
            if self.__background == -1:
                Screen.print(blank)
            else:
                Screen.print(self.__background + blank)
            Color.reset()
        
    def _close(self):
        for j in range(self.__height):
            Cursor.move(self.__location.x, self.__location.y + j)
            blank = ""
            for i in range(self.__width):
                blank += " "
            Screen.print(blank)
   
    def _set_parent(self, parent):
        if issubclass(type(parent), Window):
            self.__parent = parent

    def get_parent(self):
        return self.__parent    

    @property
    def parent(self):
        return self.__parent

    @property
    def keydown_listener(self):
        pass    

    @keydown_listener.setter
    def keydown_listener(self, keydown_listener):
        self.__keydown_listener = keydown_listener

    def __repr__(self):
        return (self.__location.__repr__() 
                + "\n<size width = " + str(self.__width) + " height = " + str(self.__height) + ">" 
                + "\n<background = " + str(self.__background) + ">")
               
