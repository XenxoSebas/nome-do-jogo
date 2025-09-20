import pygame

pygame.init()

gameExit = False

lead_X = 50
lead_Y = 50
width = 20
height = 20
vel = 5
pygame.key.set_repeat(500, 100)

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)

FPS = 60
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Slitter")

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                lead_X -= vel
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                lead_X += vel
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                lead_Y -= vel
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                lead_Y += vel

    gameDisplay.fill(green)
    pygame.draw.rect(gameDisplay, red, [lead_X, lead_Y, width, height])

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
quit()