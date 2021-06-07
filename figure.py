import pygame

class Figure(pygame.sprite.Sprite):
    def __init__(self, surf, x, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center = (x, 0))
        self.speed = speed


    def update(self, *args):
        if self.rect.y < args[0]-20:
            self.rect.y += self.speed
        else:
            self.kill()
    