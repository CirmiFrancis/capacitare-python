# PYTHON 3
# python3 --version
# pip3 --version
# pip3 install pygame
# python3 -m pygame --version

# ========================================================================

# import pygame.examples.aliens as aliens
# aliens.main()

# ========================================================================

# import pygame
# pygame.init()
# print("Pygame initialized successfully!")

# ========================================================================

import pygame
import sys

pygame.init()

pygame.display.set_caption('Ball')

size = width, height = 620, 480
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("pygame/learning/ball.png")
ball = pygame.transform.scale(ball, (50, 50))
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()