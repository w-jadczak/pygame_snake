import pygame

from utils.color import Color


class Score:
    def __init__(self):
        self.value: int = 0
        self.score_font = pygame.font.SysFont('times new roman', 20)
        self.color = Color.black

    def draw(self, screen: pygame.Surface):
        score_surface = self.score_font.render('Score : ' + str(self.value), True, self.color)
        score_rect = score_surface.get_rect()
        screen.blit(score_surface, score_rect)

    def add(self, score: int = 0):
        self.value += score