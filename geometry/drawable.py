from typing import List

import pygame

import config
from utils.color import Color
from geometry.position import Position


class Drawable:
    def __init__(self, position: Position, block_size: int = config.BLOCK_SIZE, color = Color.white):
        self.color = color
        self.block_size = block_size
        self.position: Position = position
        self.blocks: List[Position] = [self.position]

    def draw(self, surface: pygame.Surface) -> None:
        for x, y in self.blocks:
            pygame.draw.rect(surface, self.color, pygame.Rect(x, y, self.block_size, self.block_size))

    def get_rect(self, index: int = 0) -> pygame.Rect:
        """Return a pygame.Rect representing block from drawable object."""
        x, y = self.blocks[index]   # head = first element
        return pygame.Rect(x, y, self.block_size, self.block_size)