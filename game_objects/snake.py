import pygame

import config
from events.event import Event
from geometry.position import Position
from utils.color import Color
from geometry.drawable import Drawable
from controllers.movement_controller import MovementController


class Snake(Drawable):
    def __init__(self, controller: MovementController):
        super().__init__(position=Position(config.WINDOW_X // 2, config.WINDOW_Y // 2))
        self.controller = controller
        self.color = Color.green

    def update(self, ate_food: bool) -> None:
        self.check_gm_conditions()
        self.position = self.controller.next_position(self.position)
        self.controller.handle_input()
        self.blocks.insert(0, self.position)
        if not ate_food:
            self.blocks.pop()
            return
        self.controller.speed +=0.5

    def check_gm_conditions(self):
        if self._self_collision() or self._wall_collision():
            pygame.event.post(pygame.event.Event(Event.GAME_OVER_EVENT))

    def _wall_collision(self) -> bool:
        head = self.blocks[0]
        block = config.BLOCK_SIZE

        return (
                head.x < 0
                or head.y < 0
                or head.x + block > config.WINDOW_X
                or head.y + block > config.WINDOW_Y
        )

    def _self_collision(self) -> bool:
        if len(self.blocks) < 2:
            return False
        head_rect = self.get_rect(0)
        return any(head_rect.colliderect(self.get_rect(i)) for i in range(1, len(self.blocks)))
