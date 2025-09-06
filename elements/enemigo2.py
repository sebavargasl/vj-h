import pygame
import random
from pygame.locals import (RLEACCEL)


class Enemy2(pygame.sprite.Sprite):

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        # nos permite invocar métodos o atributos de Sprite
        super(Enemy2, self).__init__()
        enemigo2png = pygame.image.load('assets/enemigo2/enemigo2.png').convert_alpha()
        enemigo2_scaled = pygame.transform.scale(enemigo2png, (64, 64))
        self.surf = enemigo2_scaled
        # la posicion inicial es generada aleatoriamente, al igual que la velocidad
        self.rect = self.surf.get_rect(
            center=(
                SCREEN_WIDTH + 100,
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(8, 10)


    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()