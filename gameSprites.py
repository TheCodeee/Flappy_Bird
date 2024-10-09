import pygame as pg
pg.mixer.init()

class gameSprites:
    def __init__(self) -> None:
        pg.image.load('bg.jpg')
        pg.image.load('bird.png')
        pg.image.load('ground.png')
        pg.image.load('pipedown.png')
        pg.image.load('pipeup.png')

        pg.mixer.music('flap.mp3')
        pg.mixer.music('gameover.mp3')
