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
pygame.display.set_caption("PyGame Test App2")

FPS = 60
clock = pygame.time.Clock()

screen.fill(WHITE)

pygame.draw.rect(screen, BLUE, (10, 100, 50, 100), 3)
pygame.draw.line(screen, GREEN, (200, 20), (350, 50), 3)
pygame.draw.aaline(screen, GREEN, (200, 40), (350, 70), 3)
pygame.draw.lines(screen, RED, True, [(200, 80), (250, 80), (300, 200)], 3)
pygame.draw.aalines(screen, RED, True, [(300, 80), (350, 80), (400, 200)], 3)
pygame.draw.polygon(screen, BLACK, [(150, 210), (180, 250), (90, 290), (30, 230)], 3)
pygame.draw.circle(screen, BLUE, (650, 100), 40, 2)
pygame.draw.ellipse(screen, BLUE, (600, 250, 150, 50), 3)
pi = 3.14
pygame.draw.arc(screen, RED, (500, 300, 150, 50), pi/2, 2*pi, 3)

pygame.display.update() 

flRunning = True

while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
            pygame.quit()

    clock.tick(FPS)