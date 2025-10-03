from typing import List

import pygame

import config
from utils.color import Color
from position import Position


class Drawable:
    def __init__(self, position: Position, block: int = config.BLOCK_SIZE,  color = Color.white ):
        self.color = color
        self.block = block
        self.position: Position = position
        self.body: List[Position] = [self.position]

    def draw(self, surface: pygame.Surface) -> None:
        for x, y in self.body:
            pygame.draw.rect(surface, self.color, pygame.Rect(x, y, self.block, self.block))
