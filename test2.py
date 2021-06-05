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
pygame.display.flip() # буффер

rect = pygame.draw.rect(screen, BLUE, (50, 200, 50, 100))
pygame.display.update(rect) # тек төртбұрышты жаңартады

flRunning = True

while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
            pygame.quit()

    clock.tick(FPS)