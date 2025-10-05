import sys

import config
import pygame

from events.event import Event
from events.game_over import GameOver
from game_objects.score import Score
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
    score = Score()
    food = Food()
    ate_food = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == Event.GAME_OVER_EVENT:
                GameOver().show(screen, score.value)


        if snake.get_rect().colliderect(food.get_rect()):
            ate_food = True
            score.add(10)
            food.spawn()
            config.FPS += 1

        snake.update(ate_food)
        screen.fill(Color.white)
        food.draw(screen)
        snake.draw(screen)
        score.draw(screen)
        pygame.display.flip()
        ate_food = False
        fps.tick(config.FPS)


if __name__ == '__main__':
    main()
