import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

screen_width = 800
screen_height = int(800*0.8)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rect property demo")

screen.fill(WHITE)
pygame.display.update()

FPS = 60
clock = pygame.time.Clock()
flRunning = True

ground = screen_height - 70
jump_force = 30
move_speed = jump_force + 1

hero = pygame.Surface((20, 30))
hero.fill(BLUE)
hero_rect = hero.get_rect(centerx = screen_width // 2)
hero_rect.bottom = ground 

update_rect = pygame.Rect((hero_rect.x, 0, hero_rect.width, ground))

while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and hero_rect.bottom == ground:
                move_speed = -jump_force

    if move_speed <= jump_force:
        if move_speed + hero_rect.bottom < ground:
            hero_rect.bottom += move_speed

            if move_speed < jump_force:
                move_speed += 1
        else:
            hero_rect.bottom = ground
            move_speed = jump_force + 1


    screen.fill(WHITE)
    screen.blit(hero, hero_rect)
    pygame.display.update(update_rect)

    clock.tick(FPS)