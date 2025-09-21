import pygame
import random

pygame.init()

cell_size = 35
cols = 20
rows = 20
grid_width = 700
grid_height = 700
grid_Width = cols * cell_size
grid_Height = rows * cell_size

grid_x = 2
grid_y = 2
score1 = 0

player2_x = 5
player2_y = 5
score2 = 0

vel = 1
pygame.key.set_repeat(500, 100)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
dark_green = (0, 128, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (255, 0, 255)
orange = (255, 165, 0)  # Cor dos obstáculos

clock = pygame.time.Clock()
FPS = 10

tempo_total_segundos = 60
start_ticks = pygame.time.get_ticks()

gameDisplay = pygame.display.set_mode((grid_width, grid_height))
pygame.display.set_caption("Slitter")

def load_tilemap(filename):
    with open(filename, 'r') as f:
        tilemap = []
        for line in f:
            if not '#' in line:
                row = list(map(int, line.strip().split()))
                tilemap.append(row)
    return tilemap

tilemap = load_tilemap("map")
rows = len(tilemap)
cols = len(tilemap[0]) if rows > 0 else 0

spawn1_x = spawn1_y = spawn2_x = spawn2_y = 0

for y in range(rows):
    for x in range(cols):
        if tilemap[y][x] == 2:
            grid_x = spawn1_x = x
            grid_y = spawn1_y = y
        elif tilemap[y][x] == 3:
            player2_x = spawn2_x = x
            player2_y = spawn2_y = y

def draw_grid():
    for x in range(0, grid_Width, cell_size):
        pygame.draw.line(gameDisplay, dark_green, (x, 0), (x, grid_Height))
    for y in range(0, grid_Height, cell_size):
        pygame.draw.line(gameDisplay, dark_green, (0, y), (grid_Width, y))

def draw_tilemap():
    for y in range(rows):
        for x in range(cols):
            if tilemap[y][x] == 1:
                pygame.draw.rect(gameDisplay, blue, (x * cell_size, y * cell_size, cell_size, cell_size))
            elif tilemap[y][x] == 2:
                pygame.draw.rect(gameDisplay, purple, (x * cell_size, y * cell_size, cell_size, cell_size))
            elif tilemap[y][x] == 3:
                pygame.draw.rect(gameDisplay, red, (x * cell_size, y * cell_size, cell_size, cell_size))

def valid_movement(x, y):
    if x < 0 or x >= cols or y < 0 or y >= rows:
        return False
    if tilemap[y][x] == 1:
        return False
    if (x, y) in obstacles:
        return False
    return True

def get_random_empty_cell():
    while True:
        x = random.randint(0, cols - 1)
        y = random.randint(0, rows - 1)
        if tilemap[y][x] == 0 and (x, y) != (grid_x, grid_y) and (x, y) != (player2_x, player2_y) and (x, y) not in obstacles:
            return x, y

obstacles = []

def generate_obstacles(n=5):
    obstacles.clear()
    for _ in range(n):
        x, y = get_random_empty_cell()
        obstacles.append((x, y))

collectibles = []

def generate_collectibles(n=10):
    collectibles.clear()
    for _ in range(n):
        x, y = get_random_empty_cell()
        collectibles.append((x, y))

def call_gridmap():
    draw_grid()
    draw_tilemap()

generate_obstacles(5)
generate_collectibles(10)

gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

        if event.type == pygame.KEYDOWN:
            # player 1
            if event.key == pygame.K_a:
                novo_x = grid_x - vel
                if valid_movement(novo_x, grid_y):
                    grid_x = novo_x
            if event.key == pygame.K_d:
                novo_x = grid_x + vel
                if valid_movement(novo_x, grid_y):
                    grid_x = novo_x
            if event.key == pygame.K_w:
                novo_y = grid_y - vel
                if valid_movement(grid_x, novo_y):
                    grid_y = novo_y
            if event.key == pygame.K_s:
                novo_y = grid_y + vel
                if valid_movement(grid_x, novo_y):
                    grid_y = novo_y

            # player 2
            if event.key == pygame.K_LEFT:
                novo_x = player2_x - vel
                if valid_movement(novo_x, player2_y):
                    player2_x = novo_x
            if event.key == pygame.K_RIGHT:
                novo_x = player2_x + vel
                if valid_movement(novo_x, player2_y):
                    player2_x = novo_x
            if event.key == pygame.K_UP:
                novo_y = player2_y - vel
                if valid_movement(player2_x, novo_y):
                    player2_y = novo_y
            if event.key == pygame.K_DOWN:
                novo_y = player2_y + vel
                if valid_movement(player2_x, novo_y):
                    player2_y = novo_y

    if (grid_x, grid_y) == (player2_x, player2_y):
        grid_x, grid_y = spawn1_x, spawn1_y
        player2_x, player2_y = spawn2_x, spawn2_y

    for c in collectibles[:]:
        if (grid_x, grid_y) == c:
            score1 += 1
            collectibles.remove(c)
        elif (player2_x, player2_y) == c:
            score2 += 1
            collectibles.remove(c)

    if len(collectibles) == 0:
        generate_collectibles(10)

    gameDisplay.fill(green)

    call_gridmap()

    # obstáculos
    for ox, oy in obstacles:
        pygame.draw.rect(gameDisplay, orange, (ox * cell_size, oy * cell_size, cell_size, cell_size))

    # jogadores
    pygame.draw.rect(gameDisplay, purple, (grid_x * cell_size, grid_y * cell_size, cell_size, cell_size))
    pygame.draw.rect(gameDisplay, red, (player2_x * cell_size, player2_y * cell_size, cell_size, cell_size))

    # colecionáveis
    for cx, cy in collectibles:
        pygame.draw.circle(gameDisplay, yellow, (cx * cell_size + cell_size // 2, cy * cell_size + cell_size // 2), cell_size // 4)

    font = pygame.font.SysFont(None, 30)
    text1 = font.render(f"score1: {score1}", True, purple)
    gameDisplay.blit(text1, (10, 10))
    text2 = font.render(f"score2: {score2}", True, red)
    gameDisplay.blit(text2, (10, 40))

    segundos_passados = (pygame.time.get_ticks() - start_ticks) / 1000
    segundos_restantes = max(0, tempo_total_segundos - segundos_passados)
    tempo_texto = font.render(f"Tempo: {int(segundos_restantes)} segundos", True, black)
    gameDisplay.blit(tempo_texto, (grid_width - 200, 10))

    if segundos_restantes <= 0:
        print("Tempo esgotado!")
        print(f"Pontuação final do Player 1: {score1}")
        print(f"Pontuação final do Player 2: {score2}")
        gameExit = True

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
