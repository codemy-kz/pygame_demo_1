import pygame
from figure import Figure

SCREEN_WIDTH = 1380
SCREEN_HEIGHT = 580

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Sprite Demo App")

bg_surf = pygame.image.load("images/back1.jpg").convert()

f1 = Figure("images/ball_bear.png", SCREEN_WIDTH//2, 1)

FPS = 60
clock = pygame.time.Clock()
flRunning = True

while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
            pygame.quit()

    
    screen.blit(bg_surf, (0,0))
    screen.blit(f1.image, f1.rect)

    f1.update(SCREEN_HEIGHT)
    
    pygame.display.update()

    clock.tick(FPS)