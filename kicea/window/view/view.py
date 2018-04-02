from kicea.window.window import Window

class View(Window):
    
    def __init__(self, location, width, height):
        super().__init__(location, width, height)
        self.views = []
    
    def add_view(self, view):
        self.views.append(view)
        view._set_parent(self)
    
    def open(self):
        self._open()

    def _open(self):
        super()._open()
        for view in self.views:
            if issubclass(type(view), Window):
                view._open()
            else:   
                raise Exception
    
    def close(self):
        self._close()
 
    def _close(self):
        for view in self.views:
            if issubclass(type(view), Window):
                view._close()
            else:
                raise Exception

     
