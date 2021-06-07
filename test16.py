import pygame

BLACK = (0, 0, 0)
SCREEN_WIDTH = 1380
SCREEN_HEIGHT = 580

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Sprite Demo App")

fig_surf = pygame.image.load("images/ball_bear.png").convert_alpha()
fig_pos = fig_surf.get_rect(center = (SCREEN_WIDTH//2, 0))

speed = 1
FPS = 60
clock = pygame.time.Clock()
flRunning = True

while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
            pygame.quit()

    if fig_pos.y < SCREEN_HEIGHT-20:
        fig_pos.y += speed
    else:
        fig_pos.y = 0
    
    screen.fill(BLACK)
    screen.blit(fig_surf, fig_pos)

    pygame.display.update()

    clock.tick(FPS)