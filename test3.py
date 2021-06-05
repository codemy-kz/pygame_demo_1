import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

screen_width = 800
screen_height = int(600 * 0.8)

x_obj, y_obj = screen_width//2, screen_height // 2
speed_obj = 5

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PyGame Test App")

FPS = 60
clock = pygame.time.Clock()

screen.fill(WHITE)
pygame.display.update()

flLeft = flRight = flUp = flDown = False
flRunning = True

while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                flLeft = True
            elif event.key == pygame.K_RIGHT:
                flRight = True
            elif event.key == pygame.K_UP:
                flUp = True
            elif  event.key == pygame.K_DOWN:
                flDown = True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                flLeft = flRight = flUp = flDown = False

    if flLeft:
        x_obj -= speed_obj
    elif flRight:
        x_obj += speed_obj
    elif flUp:
        y_obj -= speed_obj
    elif flDown:
        y_obj += speed_obj

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (x_obj, y_obj, 20, 30))
    pygame.display.update()

    clock.tick(FPS)