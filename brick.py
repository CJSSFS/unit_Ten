# Chad Scott Jr
# 12/11/2018
# This program builds a pyramid of bricks with different colors on each row

import bricks
from pygame.locals import*
import pygame, sys

ORANGE = (255, 100, 0)
RED = (255, 0, 0)
GREEN = (0, 102, 71)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

SPACE = 5
HEIGHT = 20
colors = [ORANGE, RED, GREEN, BLUE, YELLOW]
number_bricks = 9


pygame.init()
main_Surface = pygame.display.set_mode((500, 250), 0, 32)
pygame.display.set_caption("Brick Pyramid")

WIDTH = (500 - (number_bricks * SPACE))/number_bricks

x = 0
y = 250 - HEIGHT

for c in range(5):
    x = (WIDTH + SPACE) * c  # this add a space + height to add a row of new bricks on the x row
    color = colors[c]
    for b in range(number_bricks):
        my_brick = bricks.Brick(WIDTH, HEIGHT, color, main_Surface)
        my_brick.draw_brick(x, y)
        x += WIDTH + SPACE
    number_bricks = number_bricks - 2
    y = y - HEIGHT - SPACE  # This subtracts the height - space to take 2 bricks away
# from the row above the previous row and makes a new row of bricks

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
