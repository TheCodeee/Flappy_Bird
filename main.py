# Importing the library
import pygame
import random
import time
 
# Initializing Pygame modules
pygame.init()

# time
clock = pygame.time.Clock()
dt = clock.tick(120)

#  Screen Vars
x = 600
y = 900

# Vars
gameover = False
running = True
velo_max = 2

backgr = pygame.image.load("bg.jpg")
backgr = pygame.transform.scale(backgr, (1100, 900))

gr_pos = 0
gr = pygame.image.load("ground.png")
gr = pygame.transform.scale(gr, (1100, 300))

bird_pos = 50
bird = pygame.image.load("bird.png")
bird = pygame.transform.scale(bird, (120, 80))


# Initializing surface
surface = pygame.display.set_mode((x, y))
 
# Initializing RGB Color
blue = (0, 0, 255)
white = (255, 255, 255)
 
# Changing surface color
surface.fill(white)


# LOOOOOP
while running:
    # GAME PHYSICS
    gravity = 1
    velo_y = 4
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                while velo_y == velo_max:
                    bird_pos -= velo_y
                    velo_y += gravity
    
    # BACKGROUND 
    surface.blit(backgr, (0, 0))
    surface.blit(gr, (gr_pos, 650))
    gr_pos -= 1
    if gr_pos == (-490):
        gr_pos = 0

    # BIRD Handeling 
    bird_pos += velo_max
    surface.blit(bird, (80, bird_pos))
    if bird_pos >= 600:
        running = False
    clock.tick(120)

    pygame.display.update()

pygame.quit()

