from dataclasses import dataclass
from enum import Enum

import pygame

import config
from geometry.position import Position


class Direction(Enum):
    UP = (0, -1, pygame.K_UP)
    DOWN = (0, 1, pygame.K_DOWN)
    LEFT = (-1, 0, pygame.K_LEFT)
    RIGHT = (1, 0, pygame.K_RIGHT)

    @property
    def vector(self) -> tuple[int, int]:
        return self.value[0], self.value[1]

    @property
    def key(self) -> int:
        return self.value[2]


@dataclass
class MovementController:
    block: int = config.BLOCK_SIZE
    speed: int = 2
    direction: Direction = None

    _opposites = {
        Direction.UP: Direction.DOWN,
        Direction.DOWN: Direction.UP,
        Direction.LEFT: Direction.RIGHT,
        Direction.RIGHT: Direction.LEFT,
    }

    def handle_input(self) -> None:
        keys = pygame.key.get_pressed()
        direction = next((d for d in Direction if keys[d.key]), None)
        if direction:
            self.change_direction(direction)

    def change_direction(self, new_direction: Direction) -> None:
        self.direction = new_direction

    def next_position(self, position: Position) -> Position:
        x, y = position.x, position.y
        if not self.direction:
            return position
        dx, dy = self.direction.vector
        position.x += dx * self.speed
        position.y += dy * self.speed
        return position


