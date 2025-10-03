import config
from geometry.bounded_position import BoundedPosition
from utils.color import Color
from geometry.drawable import Drawable
from controllers.movement_controller import MovementController


class Snake(Drawable):
    def __init__(self, controller: MovementController):
        super().__init__(position=BoundedPosition(config.WINDOW_X // 2, config.WINDOW_Y // 2))
        self.controller = controller
        self.color = Color.green

    def update(self) -> None:
        self.position = self.controller.next_position(self.position)
        self.controller.handle_input()
        self.body.insert(0, self.position)
        self.body.pop()

