import time

import pygame

import config
from utils.color import Color


class GameOver:

    def __init__(self):
        self.font = pygame.font.SysFont('times new roman', 50)

    def show(self, screen : pygame.Surface, score: int):
        game_over_surface = self.font.render(
            'Your Score is : ' + str(score), True, Color.red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (config.WINDOW_X // 2, config.WINDOW_Y // 4)
        screen.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        time.sleep(5)
        pygame.quit()
        quit()