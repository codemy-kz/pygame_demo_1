import pygame

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (239, 228, 176)

pygame.init()

screen_width = 800
screen_height = int(600 * 0.8)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PyGame Font Test App")

FPS = 60
clock = pygame.time.Clock()

font = pygame.font.Font("YandexSDLight.ttf", 24)
text_surf = font.render("Сәлем Қазақтар!", 1, RED, YELLOW)
text_pos = text_surf.get_rect(center = (screen_width // 2, screen_height // 2))

def draw_text():
    screen.fill(WHITE)
    screen.blit(text_surf, text_pos)
    pygame.display.update()

draw_text()

flRunning = True

while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pygame.mouse.get_rel()

    if pygame.mouse.get_focused() and text_pos.collidepoint(pygame.mouse.get_pos()):
        btns = pygame.mouse.get_pressed()
        if btns[0]:
            text_pos.move_ip(pygame.mouse.get_rel())
            draw_text()
            
    clock.tick(FPS)