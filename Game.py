import pygame
from pygame import K_ESCAPE
from pygame.draw import circle

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)

gameDisplay = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Hello World")

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print ("you pressed the A key")

        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill(yellow)
    pygame.draw.rect(gameDisplay, red, [400, 300, 10, 160])
    pygame.draw.circle(gameDisplay, blue, [200, 600], 50)

    pygame.display.update()

pygame.quit()
quit()