import pygame
from figure import Figure
import random

SCREEN_WIDTH = 1380
SCREEN_HEIGHT = 580

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2000)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Sprite Demo App")

bg_surf = pygame.image.load("images/back1.jpg").convert()

figures = pygame.sprite.Group()

fig_images = [
    'ball_bear.png', 'ball_fox.png', 'ball_panda.png', 'ball_lemur.png',
    'ball_tiger.png', 'ball_puppy.png', 'ball_kitten.png', 'ball_hed.png',
    'ball_lion.png', 'ball_owl.png', 'ball_pantera.png', 'ball_rabbit.png',
    'ball_sn_lpd.png', 'ball_squ.png']
fig_surf = [pygame.image.load('images/' + image) for image in fig_images]

def create_figure(group):
    index = random.randint(0, len(fig_surf)-1)
    figure = fig_surf[index]
    speed = random.randint(1, 4)
    from_x = random.randint(30, SCREEN_WIDTH-30)
    
    group.add(Figure(figure, from_x, speed))

FPS = 60
clock = pygame.time.Clock()
flRunning = True

while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
            pygame.quit()
        elif event.type == pygame.USEREVENT:
            create_figure(figures)

    
    screen.blit(bg_surf, (0,0))
  
    figures.draw(screen)
    figures.update(SCREEN_HEIGHT)
    
    pygame.display.update()

    clock.tick(FPS)