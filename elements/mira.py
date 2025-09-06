if __name__ == "__main__": # Solo para que no ejecutes este archivo
    import sys
    print(
        "\033[38;2;255;0;0mESTE MODULO NO DEBE EJECUTARSE. EJECUTAR main.py\033[0m\n"
        * 3
    )
    sys.exit()

import pygame
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT, RLEACCEL,K_w,K_a,K_s,K_d)
import math

from elements.projectile import Projectile

mirilla = pygame.image.load("assets/crosshair.png")
mirilla_scaled = pygame.transform.scale(mirilla, (40, 40))

class Mirilla(pygame.sprite.Sprite):
    
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT): 
        super(Mirilla, self).__init__()
    
        self.surf = mirilla_scaled
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
    

    def update(self): 
        
        # POR HACER (2.2): Mover la bala y eliminarla si se sale de la pantalla
        mouse_pos=pygame.mouse.get_pos()
        self.rect.center=mouse_pos
