import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

screen_width = 800
screen_height = int(600 * 0.8)

x_obj, y_obj = screen_width // 2, screen_height // 2
speed_obj = 5

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PyGame Test App")

FPS = 60
clock = pygame.time.Clock()

screen.fill(WHITE)
pygame.display.update()

flRunning = True

while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
            pygame.quit()

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        x_obj -= speed_obj
    elif pressed[pygame.K_RIGHT]:
        x_obj += speed_obj
    elif pressed[pygame.K_UP]:
        y_obj -= speed_obj
    elif pressed[pygame.K_DOWN]:
        y_obj += speed_obj

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (x_obj, y_obj, 20, 30))
    pygame.display.update()

    clock.tick(FPS)