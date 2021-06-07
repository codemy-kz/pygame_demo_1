import pygame
import random

SCREEN_WIDTH = 1380
SCREEN_HEIGHT = 580

class Ball(pygame.sprite.Sprite):
    def __init__(self, surf, x, speed, score):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = surf.get_rect(center = (x, 0))
        self.speed = speed
        self.score = score
        
    def update(self, *args):
        if self.rect.y < args[0] - 20:
            self.rect.y += self.speed
        else:
            self.kill()


pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

pygame.time.set_timer(pygame.USEREVENT, 2000)

pygame.mixer.music.load('sounds/bird.mp3')
pygame.mixer.music.play(-1)

s_catch = pygame.mixer.Sound('sounds/catch.ogg')

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite collide Demo")

balls_data = (
    {'path':'ball_bear.png', 'score':20},
    {'path':'ball_fox.png', 'score':15},
    {'path':'ball_hed.png', 'score':10},
    {'path':'ball_kitten.png', 'score':10},
    {'path':'ball_lemur.png', 'score':10},
    {'path':'ball_lion.png', 'score':20},
    {'path':'ball_owl.png', 'score':10},
    {'path':'ball_panda.png', 'score':20},
    {'path':'ball_pantera.png', 'score':15},
    {'path':'ball_puppy.png', 'score':15},
    {'path':'ball_rabbit.png', 'score':10},
    {'path':'ball_sn_lpd.png', 'score':15},
    {'path':'ball_squ.png', 'score':10},
    {'path':'ball_tiger.png', 'score':20},
)
balls_surf = [pygame.image.load('images/' + data['path']).convert_alpha() for data in balls_data]

balls = pygame.sprite.Group()

bg_surf = pygame.image.load("images/back1.jpg").convert()
telega = pygame.image.load("images/telega.png").convert_alpha()
telega_pos = telega.get_rect(center = (SCREEN_WIDTH//2, SCREEN_HEIGHT-40))
bg_score = pygame.image.load("images/score_fon.png").convert_alpha()
font = pygame.font.Font('YandexSDLight.ttf', 34)

def create_ball():
    index = random.randint(0, len(balls_surf)-1)
    x = random.randint(20, SCREEN_WIDTH-20)
    speed = random.randint(1, 4)
    balls.add(Ball(balls_surf[index], x, speed, balls_data[index]['score']))

telega_speed = 10
game_score = 0
def ball_collide():
    global game_score
    for ball in balls:
        if telega_pos.collidepoint(ball.rect.center):
            s_catch.play()
            game_score += ball.score
            ball.kill()

FPS = 60
clock = pygame.time.Clock()
flRunning = True

while flRunning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
            pygame.quit()
        elif event.type == pygame.USEREVENT:
            create_ball()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        telega_pos.x -= telega_speed
        if telega_pos.x < 0:
            telega_pos.x = 0
    elif pressed[pygame.K_RIGHT]:
        telega_pos.x += telega_speed
        if telega_pos.x > SCREEN_WIDTH-telega_pos.width:
            telega_pos.x = SCREEN_WIDTH-telega_pos.width
        

    
    screen.blit(bg_surf, (0,0))
    screen.blit(bg_score, (0,0))
    font_surf = font.render(str(game_score), 1, ((94,138,14)))
    screen.blit(font_surf, (20, 10))
    balls.draw(screen)
    balls.update(SCREEN_HEIGHT)
    screen.blit(telega, telega_pos)
    
    ball_collide()

    pygame.display.update()

    clock.tick(FPS)


