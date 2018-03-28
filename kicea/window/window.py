from kicea.screen.screen import Screen
from kicea.cursor.cursor import Cursor
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
 
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        if(type(location) is Location):
            self.__location = location

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if(type(width) is int):
            self.__width = width
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        if(type(height) is int):
            self.__height = height
    
    @property
    def background(self):
        return self.__background
    
    def set_background(self, *args):
        if len(args) == 3:
            self.__background =  Color.background(args[0], args[1], args[2])
        else:
            raise Exception

    def open(self):
        for j in range(self.__height):
            Cursor.move(self.__location.x, self.__location.y + j)
            blank = ""
            for i in range(self.__width):
                blank += " "
            Screen.print(self.__background + blank)
            Color.reset()
        
    def close(self):
        for j in range(self.__height):
            Cursor.move(self.__location.x, self.__location.y + j)
            blank = ""
            for i in range(self.__width):
                blank += " "
            Screen.print(blank)
        
    def __repr__(self):
        return (self.__location.__repr__() 
                + "\n<size width = " + str(self.__width) + " height = " + str(self.__height) + ">" 
                + "\n<background = " + str(self.__background) + ">")
               