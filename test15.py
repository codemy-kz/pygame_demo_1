import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(800*0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Image Demo")

car_surf = pygame.image.load("images/car.bmp").convert()
car_surf.set_colorkey((255, 255, 255))
car_pos = car_surf.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

car_up = car_surf
car_down = pygame.transform.flip(car_surf, 0, 1)
car_left = pygame.transform.rotate(car_surf, 90)
car_right = pygame.transform.rotate(car_surf, -90)

bg_surf = pygame.image.load("images/sand.jpg").convert()
# bg_surf = pygame.transform.scale(bg_surf, (bg_surf.get_width()//2, bg_surf.get_height()//2))
finish_surf = pygame.image.load("images/finish.png").convert_alpha()
screen.blit(bg_surf, (0, 0))
screen.blit(finish_surf, (0, 0))
screen.blit(car_surf, car_pos)

pygame.display.update()

car = car_up
speed = 5
FPS = 60
clock = pygame.time.Clock()
flRunning = True

while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
            pygame.quit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        car = car_left
        car_pos.x -= speed
        if car_pos.x < 0:
            car_pos.x = 0
    elif pressed[pygame.K_RIGHT]:
        car = car_right
        car_pos.x += speed
        if car_pos.x > SCREEN_WIDTH - car.get_width():
            car_pos.x = SCREEN_WIDTH - car.get_width()
    elif pressed[pygame.K_UP]:
        car = car_up
        car_pos.y -= speed
        if car_pos.y < 0:
            car_pos.y = 0
    elif pressed[pygame.K_DOWN]:
        car = car_down
        car_pos.y += speed
        if car_pos.y > SCREEN_HEIGHT - car_pos.height:
            car_pos.y = SCREEN_HEIGHT - car_pos.height

    screen.blit(bg_surf, (0,0))
    screen.blit(finish_surf, (0,0))
    screen.blit(car, car_pos)

    pygame.display.update()


    clock.tick(FPS)