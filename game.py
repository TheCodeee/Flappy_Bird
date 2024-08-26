import pygame as pg

class game:
    def __init__(self):
        # Game Variables
        self.groundx = 0
        self.groundy = 710
        self.screenx = 1600
        self.screeny = 970
        self.gameover = False

        # bird Variables 
        self.accn = 2
        self.terminalVelo = 10
        self.bird_velo = 0

        # gameSprites 
        self.birdx = self.screenx/2 - 100
        self.birdy = self.screeny/3
        self.bird = pg.image.load("bird.png")
        self.bird = pg.transform.scale(self.bird, (self.screenx/14, self.screeny/15))
        self.bird_rect = self.bird.get_rect()
        self.bg = pg.image.load("bg.jpg")
        self.bg = pg.transform.scale(self.bg, (self.screenx, self.screeny))
        self.ground = pg.image.load("ground.png")
        self.ground = pg.transform.scale(self.ground, (1700, 300))
