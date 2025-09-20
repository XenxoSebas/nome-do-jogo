import pygame
import random

pygame.init()
yellow = (226,178,13)
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)

gameDisplay = pygame.display.set_mode((800, 800))
pygame.display.set_caption("movimento")

cor = red
timer=0
cores= [white,yellow,red,green]
pos = [0,0]

jogoAberto = True
while jogoAberto == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogoAberto = False
    gameDisplay.fill(black)

    pygame.draw.rect(gameDisplay, cor, (pos, (50, 50)))
    timer +=1
    if timer ==90:
        cor = random.choice(cores)
        timer = 0
        pos[0] += 10
        pos[1] += 10
        if pos[0]==800 or pos[1]==800:
            pos[0]=0
            pos[1]=0
    pygame.display.update()

pygame.quit()
quit()