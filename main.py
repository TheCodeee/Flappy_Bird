import pygame as pg
from random import randint

pg.init()

class game:
    def __init__(self):
        # Game Variables
        self.groundx = 0
        self.screenx = 1600
        self.screeny = 970
        self.gameover = False

        # gameSprites 
        self.birdx = self.screenx/2 - 100
        self.birdy = self.screeny/3
        self.bird = pg.image.load("bird.png")
        self.bird = pg.transform.scale(self.bird, (self.screenx/11, self.screeny/11))
        self.bg = pg.image.load("bg.jpg")
        self.bg = pg.transform.scale(self.bg, (self.screenx, self.screeny))
        self.ground = pg.image.load("ground.png")
        self.ground = pg.transform.scale(self.ground, (1700, 300))
        self.pipedown = pg.image.load("pipedown.png")
        self.pipeup = pg.image.load("pipeup.png")

    def pipes(self):
        pass

    def Flap(self):
        self.accn = 4
        self.terminalVelo = 10
        self.bird_velo = 0
        self.birdy += self.bird_velo
        if self.bird_velo > self.terminalVelo:
            self.bird_velo = self.terminalVelo
        self.bird_velo += self.accn

play = game()

# colors
white = (255, 255, 255)

# window
screen = pg.display.set_mode((play.screenx, play.screeny))
pg.display.set_caption("Flappy Bird")

while not play.gameover:
    play.Flap()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            play.gameover = True

        if event.type == pg.KEYDOWN:
            if event.type == pg.K_SPACE:
                play.bird_velo = -15
    
    play.groundx -= 5
    if play.groundx <= -80:
        play.groundx = 0

    screen.blit(play.bg, (0, 0))
    screen.blit(play.ground, (play.groundx, 710))
    screen.blit(play.bird, (play.birdx, play.birdy))

    pg.display.update()
pg.quit()
