import pygame
import random
from pygame.locals import (RLEACCEL)


class Enemy3(pygame.sprite.Sprite):

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        # nos permite invocar métodos o atributos de Sprite
        super(Enemy3, self).__init__()
        enemigo3png = pygame.image.load('assets/enemigo3/enemigo3.png').convert_alpha()
        enemigo3_scaled = pygame.transform.scale(enemigo3png, (64, 64))
        self.surf = enemigo3_scaled
        # la posicion inicial es generada aleatoriamente, al igual que la velocidad
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0,SCREEN_WIDTH),
                -self.surf.get_height(),
            )
        )
        self.speed = random.randint(5, 7)
        self.SCREEN_HEIGHT = SCREEN_HEIGHT

    def update(self):
        self.rect.move_ip(0,self.speed)
        if self.rect.top > self.SCREEN_HEIGHT:
            self.kill()