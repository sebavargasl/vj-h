import pygame
import random

class Life(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        obj=pygame.image.load("assets/powerups/vida.png")
        obj_scaled=pygame.transform.scale(obj,(60,60))
        self.surf = obj_scaled
        self.rect = self.surf.get_rect(
            center=(
                random.randint(20,SCREEN_WIDTH-20),
                -20
            )
        )
        self.speed = 2
        self.SCREEN_HEIGHT=SCREEN_HEIGHT

    def update(self):
        self.rect.top += self.speed
        if self.rect.top > self.SCREEN_HEIGHT:
            self.kill()