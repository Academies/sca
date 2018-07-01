"""
Snake using Pygame
Maria V Zlatkova
CS50 at HSA, July 2018

Adapted from https://github.com/ternus
"""

import pygame
import sys
import time
import random
from pygame.locals import *

# Constants
FPS = 15
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRIDSIZE = 10
GRID_WIDTH = SCREEN_WIDTH / GRIDSIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRIDSIZE
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Initial setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
surface = pygame.Surface(screen.get_size()).convert()
clock = pygame.time.Clock()

def main():
    snake = Snake()
    apple = Apple()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    snake.point(UP)
                elif event.key == K_DOWN:
                    snake.point(DOWN)
                elif event.key == K_LEFT:
                    snake.point(LEFT)
                elif event.key == K_RIGHT:
                    snake.point(RIGHT)

        # Refill as snake moves so that the path it took doesn't remain black
        surface.fill((255,255,255))

        # Keep moving snake forward
        snake.move()

        # Check if snake reached apple
        check_eat(snake, apple)

        # Draw snake and apple on surface
        snake.draw(surface)
        apple.draw(surface)

        # Set up score indicator with the value of the snake length
        score = pygame.font.Font(None, 36).render(str(snake.length),
                                                  1, (10, 10, 10))
        score_position = score.get_rect()
        score_position.centerx = 20

        # Draw surface (background) and  score onto the window
        surface.blit(score, score.get_rect())
        screen.blit(surface, (0,0))

        # Update the contents of the entire display
        pygame.display.flip()

        # Delay snake movement for better gameplay
        clock.tick(FPS + snake.length / 3)

# Draw each rectangle that makes up the snake or apple
def draw_box(surface, color, position):
    pygame.draw.rect(surface,
                     color,
                     pygame.Rect((position[0], position[1]),
                                 (GRIDSIZE, GRIDSIZE)))

# Check whether snake reached and ate apple
def check_eat(snake, apple):
    if snake.get_head_position() == apple.position:
        snake.length += 1
        apple.randomize()

class Snake(object):
    def __init__(self):
        self.restart()
        self.color = (0,0,0)

    # Method returns the position of the head/front of the snake
    def get_head_position(self):
        return self.positions[0]

    # Method to initialize position, direction and length when game is restarted
    def restart(self):
        self.length = 1
        self.positions =  [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    # Method to point snake in new direction, specified by point
    def point(self, point):
        # If snake is moving left, and the new direction is right, do nothing
        # since it can't automatically move in the opposite direction onto itself
        # When the snake length is 1, moving in the oppsite direction is allowed
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    # Method to move snake forward
    def move(self):
        # Calculate current position and direction
        cur_position = self.positions[0]
        x, y = self.direction

        # Calculate new position to advance snake forward
        new_position = (((cur_position[0] + (x * GRIDSIZE)) % SCREEN_WIDTH),
                        (cur_position[1] + (y * GRIDSIZE)) % SCREEN_HEIGHT)

        # If snake tries to move in a grid where it is already located,
        # and its length is greater than 2, the game is lost
        if len(self.positions) > 2 and new_position in self.positions[2:]:
            self.restart()
        else:
            self.positions.insert(0, new_position)
            # As snake moves forward to take up new position,
            # its tail should also move forward
            if len(self.positions) > self.length:
                self.positions.pop()

    # Method to draw snake on surface
    def draw(self, surface):
        for p in self.positions:
            draw_box(surface, self.color, p)

class Apple(object):
    def __init__(self):
        self.position = (0,0)
        self.color = (255,0,0)
        self.randomize()

    # Method to place apple in random location
    def randomize(self):
        self.position = (random.randint(0, SCREEN_WIDTH - GRIDSIZE),
                         random.randint(0, SCREEN_HEIGHT - GRIDSIZE))

    # Method to draw apple
    def draw(self, surface):
        draw_box(surface, self.color, self.position)

if __name__ == '__main__':
    main()
