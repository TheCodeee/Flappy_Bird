import pipe
import game 
import pygame as pg
from random import randint

pg.init()
clock = pg.time.Clock()

play = game.game()

# colors
white = (255, 255, 255)

# window
screen = pg.display.set_mode((play.screenx, play.screeny))
pg.display.set_caption("Flappy Bird")

while not play.gameover:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            play.gameover = True

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                play.bird_velo = -25

    play.birdy += play.bird_velo
    if play.bird_velo > play.terminalVelo: 
        play.bird_velo = play.terminalVelo
    play.bird_velo += play.accn

    if play.birdy < 0 or play.birdy > play.groundy:
        play.gameover = True 

    play.groundx -= 5
    if play.groundx <= -80:
        play.groundx = 0

    screen.blit(play.bg, (0, 0))
    screen.blit(play.ground, (play.groundx, play.groundy))
    screen.blit(play.bird, (play.birdx, play.birdy))

    clock.tick(60)
    pg.display.update()
pg.quit()
