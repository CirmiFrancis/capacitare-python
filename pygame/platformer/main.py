# PYTHON 3
# python3 --version
# pip3 --version
# pip3 install pygame
# python3 -m pygame --version

# ========================================================================

import pygame
from pygame.locals import *

# init game & music
pygame.init()
pygame.mixer.init()

# screen size
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# window's title
pygame.display.set_caption('Platformer')

# music
pygame.mixer.music.load("pygame/platformer/assets/audio/music/megaman2-flashman.mp3")
pygame.mixer.music.play(-1)

# define game variables
tile_size = 50

# load images
bg_img = pygame.image.load('pygame/platformer/assets/imgs/bgs/bg-sky.jpeg')

def draw_grid():
	for line in range(0, 20):
		pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
		pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))

# WHILE RUN
run = True
while run:

    screen.blit(bg_img, (0,0))

    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.mixer.music.stop()
pygame.quit()