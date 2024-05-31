# Importing the library
import pygame
import random
 
# Initializing Pygame modules
pygame.init()
 
#  Screen Vars
x = 600
y = 900

# Vars
gameover = False
running = True

backgr = pygame.image.load("bg.jpg")
backgr = pygame.transform.scale(backgr, (1100, 900))

gr = pygame.image.load("ground.png")
gr = pygame.transform.scale(gr, (1100, 300))

# Initializing surface
surface = pygame.display.set_mode((x, y))
 
# Initializing RGB Color
blue = (0, 0, 255)
white = (255, 255, 255)
 
# Changing surface color
surface.fill(white)
surface.blit(backgr, (0, 0))
surface.blit(gr, (0, 650))
pygame.display.flip()

# LOOOOOP
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()

