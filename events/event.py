from dataclasses import dataclass

import pygame


@dataclass(slots=True)
class Event:
    GAME_OVER_EVENT = pygame.USEREVENT + 1
