import pygame
import sys
import os
import random

os.environ["SDL_VIDEO_CENTERED"] = "1"

pygame.init()


SCREENWIDTH = 500
SCREENHEIGHT = 500
SCREENSIZE = [SCREENWIDTH, SCREENHEIGHT]
SCREEN = pygame.display.set_mode(SCREENSIZE)

pygame.display.set_caption("My first game in pygame")

LENGTH = 20
WIDTH = 20
RADIUS = 20

LOOPCOUNT = 100
MINPOS = 0
MAXPOS = 480

ZEROINTENSITY = 0
MAXINTENSITY = 255

SOLID = 0
for i in range(LOOPCOUNT):
    LEFT = random.randint(MINPOS, MAXPOS)
    TOP = random.randint(MINPOS, MAXPOS)
    rect1 = pygame.Rect(LEFT, TOP, LENGTH, WIDTH)

    COLOR = (random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY),
             random.randint(ZEROINTENSITY, MAXINTENSITY))

    pygame.draw.rect(SCREEN, COLOR, rect1, SOLID)

    CIRCLEPOS = (random.randint(MINPOS, MAXPOS), random.randint(MINPOS, MAXPOS))
    pygame.draw.circle(SCREEN, COLOR, CIRCLEPOS, RADIUS, SOLID)

pygame.display.update()

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()