import random

class Model:
    _AREA_SIZE_X = 50.0
    _AREA_SIZE_Y = 30.0

    _MAX_DISTANCE_ERROR = 2.0


    def __init__(self):
        self._x = self._AREA_SIZE_X / 2
        self._y = self._AREA_SIZE_Y / 2


    def move_to(self, normal_x, normal_y):
        error_x = self._get_distance_error()
        self._x = normal_x * self._AREA_SIZE_X + error_x

        error_y = self._get_distance_error()
        self._y = normal_y * self._AREA_SIZE_Y + error_y


    def _get_distance_error(self):
        return random.uniform(-self._MAX_DISTANCE_ERROR, self._MAX_DISTANCE_ERROR)


    def get_normal_location(self):
        normal_x = self._x / self._AREA_SIZE_X
        normal_y = self._y / self._AREA_SIZE_Y

        return normal_x, normal_y