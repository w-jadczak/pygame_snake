import random

import config
from utils.color import Color
from geometry.drawable import Drawable
from geometry.position import Position


class Food(Drawable):
    def __init__(self):
        block = config.BLOCK_SIZE
        cols = config.WINDOW_X // block
        rows = config.WINDOW_Y // block
        x = random.randrange(cols) * block
        y = random.randrange(rows) * block
        super().__init__(position=Position(x, y), block_size=block, color=Color.red)

    def spawn(self):
        self.blocks.pop()
        self.blocks.append(Position(random.randrange(config.WINDOW_X), random.randrange(config.WINDOW_Y)))