from model import Model
from view import View

class Presenter:
    def __init__(self, model, view):
        self._init_model(model)
        self._init_view(view)


    def _init_model(self, model):
        self._model = model


    def _init_view(self, view):
        self._view = view
        self._update_rover_view_location()
        self._view.set_mouse_click_event_handler(self._mouse_click_event_handler)


    def _update_rover_view_location(self):
        normal_x, normal_y = self._model.get_normal_location()
        self._view.move_rover_to(normal_x, normal_y)


    def _mouse_click_event_handler(self, normal_x, normal_y):
        self._model.move_to(normal_x, normal_y)
        self._update_rover_view_location()


    def show(self):
        self._view.show()