import pygame
from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP

pygame.init()

gameExit = False

right_click = False
clicking = False
offset = [0, 0]

lead_X = 50
lead_Y = 50
width = 40
height = 40
radius = 10
vel = 5

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)

FPS = 60
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Mouse Folowing")

while not gameExit:
    mx, my = pygame.mouse.get_pos()
    loc = [mx, my]
    rot = 0
    gameDisplay.blit(pygame.transform.rotate(gameDisplay, rot), (loc[0] + offset[0], loc[1] + offset[1]))

    if clicking:
        radius += 1
    if right_click:
        radius -= 1

    gameDisplay.blit(pygame.transform.rotate(gameDisplay, rot), (loc[0] + offset[0], loc[1] + offset[1]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                clicking = True
            if event.button == 3:
                right_click = True
            if event.button == 4:
                offset[1] -= 10
            if event.button == 5:
                offset[0] += 10
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                clicking = False

    gameDisplay.fill(yellow)
    pygame.draw.circle(gameDisplay, blue, (mx, my), radius)
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
quit()