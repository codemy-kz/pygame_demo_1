import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH*0.8)


pygame.init()

main_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mouse event demo")

main_surface.fill(WHITE)
pygame.display.update()

FPS = 60
clock  = pygame.time.Clock()

flRunning = True

sp = None
while flRunning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
            pygame.quit()
    
    pressed = pygame.mouse.get_pressed()

    if pressed[0]:
        pos = pygame.mouse.get_pos()
        if sp is None:
            sp = pos
        
            
        width = pos[0] - sp[0]
        height = pos[1] - sp[1]

        main_surface.fill(WHITE)
        pygame.draw.rect(main_surface, BLUE, (sp[0], sp[1], width, height), 3)
        pygame.display.update()        

    else:
        sp = None

    
    

    clock.tick(FPS)