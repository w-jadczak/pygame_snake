import sys

import config
import pygame

from utils.color import Color
from game_objects.food import Food
from controllers.movement_controller import MovementController
from game_objects.snake import Snake


def main():
    pygame.init()
    pygame.display.set_caption('SNAKE')
    screen = pygame.display.set_mode((config.WINDOW_X, config.WINDOW_Y))
    fps = pygame.time.Clock()
    controller = MovementController()
    snake = Snake(controller)
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        snake.update()

        screen.fill(Color.white)
        snake.draw(screen)
        food.draw(screen)
        pygame.display.flip()

        fps.tick(config.FPS)


if __name__ == '__main__':
    main()
