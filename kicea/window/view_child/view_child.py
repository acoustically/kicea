from kicea.window.window import Window, Location
from kicea.window.view.view import View

class ViewChild(Window):

    def __init__(self, location, width, height):
        super(ViewChild, self).__init__(location, width, height)

    def _set_parent(self, view):
        super()._set_parent(view)
        parent_location = view.get_location()
        self.set_location(Location(parent_location.x + super().get_location().x, parent_location.y + super().get_location().y))

    
