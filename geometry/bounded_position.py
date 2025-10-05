import config
from geometry.position import Position


class BoundedPosition(Position):

    _MAX_X = config.WINDOW_X - config.BLOCK_SIZE
    _MAX_Y = config.WINDOW_Y - config.BLOCK_SIZE

    def __init__(self, x: int, y:int ):
        super().__init__(self._bounds(x, self._MAX_X), self._bounds(y, self._MAX_Y))

    def _bounds(self, val: int, max_val: int) -> int:
        if val > max_val:
            return 0
        elif val < 0:
            return max_val
        return val

    @Position.x.setter
    def x(self, value: int):
        self._x = self._bounds(value, self._MAX_X)

    @Position.y.setter
    def y(self, value: int):
        self._y = self._bounds(value, self._MAX_Y)
