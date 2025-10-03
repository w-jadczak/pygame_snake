import config
from position import Position


class BoundedPosition(Position):
    def _bounds(self, val: int, max_val: int) -> int:
        if val > max_val:
            return 0
        elif val < 0:
            return max_val
        return val

    @Position.x.setter
    def x(self, value: int):
        self._x = self._bounds(value, config.WINDOW_X)

    @Position.y.setter
    def y(self, value: int):
        self._y = self._bounds(value, config.WINDOW_Y)
