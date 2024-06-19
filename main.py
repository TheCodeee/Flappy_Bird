x = 1200
y = 900


# imports 
import pygame 
from random import randint
        

# colors 
white = (255, 255, 255)

# Initialize 
pygame.init()
pygame.mixer.init()


pipe_up = pygame.image.load("pipeup.png")
pipe_up = pygame.transform.scale(pipe_up, (100, 500))
pipe_down = pygame.image.load("pipedown.png")
pipe_down = pygame.transform.scale(pipe_down, (100, 500))


# images
background = pygame.image.load("bg.jpg")
background = pygame.transform.scale(background, (x, y))


ground = pygame.image.load("ground.png")
ground = pygame.transform.scale(ground, (1300, 225))


bird = pygame.image.load("bird.png")
bird = pygame.transform.scale(bird, (80, 60))


# Variables 
pipe_counter = 0
bird_velo = 0
bird_accn = 1
bird_velo_max = 5
bird_pos = 200
ground_pos = 0
ground_velocity = -5
clock = pygame.time.Clock()
screen = pygame.display.set_mode((x, y))
running = True


# Class 
class makepipe:
    def pipe(self):
        self.pipe_y = randint(-400, -100)
        self.pipe_x = 800
        self.pipe_x -= ground_velocity
        screen.blit(pipe_up, (self.pipe_x, self.pipe_y))
        screen.blit(pipe_down, (self.pipe_x, self.pipe_y + 700))


# Loop
while running:

    pipe_counter += 1
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                bird_velo = -12
                bird_accn = 1
                pygame.mixer.music.load("flap.mp3")
                pygame.mixer.music.play()


    bird_velo += bird_accn


    if bird_velo == bird_velo_max:
        bird_accn = 0


    bird_pos += bird_velo


    ground_pos += ground_velocity


    if ground_pos == -60:
        ground_pos = 0


    if bird_pos >= 635 or bird_pos <= 0:
        running = False
        

    screen.fill((white))

    screen.blit(background, (0, 0))
        
    screen.blit(ground, (ground_pos, 675))
    screen.blit(bird, (500, bird_pos))
    

    pygame.display.update()

pygame.quit()
