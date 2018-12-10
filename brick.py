import bricks
import pygame, sys
from pygame.locals import*

ORANGE = (0, 102, 71)
RED = (255, 0, 0)
GREEN = (0, 0, 255)
BLUE = (255, 209, 63)
YELLOW = (255, 0, 255)
SPACE = 5
HEIGHT = 20
x_number_bricks = 9


pygame.init()
main_Surface = pygame.display.set_mode((500, 250), 0, 32)
pygame.display.set_caption("Brick Pyramid")

WIDTH = (500 - (x_number_bricks * SPACE))/x_number_bricks

x = 0
y = 250 - HEIGHT
for q in range(5):
    x = (WIDTH * SPACE) * q
for b in range(x_number_bricks):
    my_brick = bricks.Brick(WIDTH, HEIGHT, ORANGE, main_Surface)
    my_brick.draw_brick(x, y)
    x = x = WIDTH + SPACE
    pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            pygame.exit()
