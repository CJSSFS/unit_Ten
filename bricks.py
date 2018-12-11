import pygame


class Brick:

    def __init__(self, width, height, color, main_surface):
        """
        This function gives the dimensions to build a brick
        :param width: this says how wide thr brick will be
        :param height: this says how tall the brick will be
        :param color: This gives the color of the brick
        :param main_surface:
        """
        self.main_surface = main_surface
        self.width = width
        self.height = height
        self.color = color

    def draw_brick(self, x, y):
        """
        This function draws a brick
        :param x: this gives the x dimension for the brick
        :param y: this gives the y dimension for the brick
        :return:
        """
        pygame.draw.rect(self.main_surface, self.color, (x, y, self.width, self.height), 0)
        pygame.display.update()
