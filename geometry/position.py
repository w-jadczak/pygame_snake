from dataclasses import dataclass


@dataclass(slots=True)
class Position:
    _x: int
    _y: int

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int):
        self._x = value

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value: int):
        self._y = value

    def __iter__(self):
        """Allows unpacking object as (x, y)."""
        yield self.x
        yield self.y

    def __repr__(self) -> str:
        return f"Position(x={self.x}, y={self.y})"
