import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

screen_width = 800
screen_height = int(600 * 0.8)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PyGame Test App")

FPS = 60
clock = pygame.time.Clock()

screen.fill(WHITE)
pygame.display.update()

surf = pygame.Surface((screen_width, 200))
bita = pygame.Surface((50, 10))

surf.fill(BLUE)
bita.fill(RED)

bx, by = 0, 150
x, y = 0, 0

flRunning = True

while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
            pygame.quit()

    surf.fill(BLUE)
    surf.blit(bita, (bx, by))

    if bx < screen_width:
        bx += 5
    else:
        bx = 0
    
    if y < screen_height:
        y += 1
    else:
        y = 0

    screen.fill(WHITE)
    screen.blit(surf, (x, y))
    pygame.display.update()
    
    clock.tick(FPS)