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

        super().__init__(position=Position(x, y), block=block, color=Color.red)

