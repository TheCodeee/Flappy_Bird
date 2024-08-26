import pygame as pg
from random import randint

class pipes:
    def __init__(self):
        self.pipedown = pg.image.load("pipedown.png")
        self.pipeup = pg.image.load("pipeup.png")

        self.rect_up = self.pipeup.get_rect()
        self.rect_down = self.pipedown.get_rect()
        self.distance = 100
        self.rect_up.y = randint(100, 700)
        self.rect_down.y = self.rect_up.y + self.distance
        self.rect_down.x = 1700
        self.rect_up.x = 1700
