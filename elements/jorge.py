"""
Hola este es modulo Jorge,
este modulo manejara la creacion y movimiento de Jorge
"""

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


JorgePNG = pygame.image.load('assets/JorgeVJ.png')
JorgePNG_scaled = pygame.transform.scale(JorgePNG, (80, 80))


class Player(pygame.sprite.Sprite):
    
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super(Player, self).__init__()
        self.surf = JorgePNG_scaled
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.vidas=3
        
        # POR HACER (2.3): Crear lista de proyectiles
        self.projectiles=pygame.sprite.Group()

        #las balas tienen un cooldown de 1000 ticks
        self.cooldown=1000
        self.ultimo_tiro=0


    def update(self, pressed_keys):
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -4)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 4)
        if pressed_keys[K_a]:
            self.rect.move_ip(-4, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(4, 0)
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height
        
        # POR HACER (2.3): Actualizar la posición de los proyectiles
        self.projectiles.update()

    
    def shoot(self, mouse_pos): 
        #si aun no se cumple el tiempo del cooldown, no se puede disparar
        tiempo_actual=pygame.time.get_ticks()
        if tiempo_actual-self.ultimo_tiro<self.cooldown:
            return
        
        # POR HACER (2.3): Crear y calcular dirección proyectil
        direction=(mouse_pos[0]-self.rect.centerx, mouse_pos[1]-self.rect.centery)
        length=math.hypot(direction[0],direction[1])
        direction=(direction[0]/length,direction[1]/length)

        projectile=Projectile(self.rect.center,direction,self.screen_width,self.screen_height)
        self.projectiles.add(projectile)

        #actualizamos el tick del ultimo disparo
        self.ultimo_tiro=tiempo_actual
    
    def perder_vida(self):
        self.vidas-=1
        

        