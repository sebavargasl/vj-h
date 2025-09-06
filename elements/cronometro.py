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

import random
from pygame.locals import (RLEACCEL)

class Tiempo(pygame.sprite.Sprite):
    def __init__(self, pos=(900,10), letra="algerian",tamaño=40 ,color=(255,255,255)):
        self.pos= pos
        self.letra=pygame.font.SysFont(letra,tamaño) 
        self.color= color
        #empezar a contar el tiempo
        self.empezar=pygame.time.get_ticks()
    
    def imagen(self, pantalla):
        tiempo= (pygame.time.get_ticks()-self.empezar)//1000 #calculamos el tiempo actual en segundos

        #obtenemos los minutos y segundos
        minutero=tiempo//60
        segundero=tiempo%60

        #creamos el "texto" que queremos mostrar
        reloj=f"{minutero}:{segundero}"
        #dibujar la imagen
        imagen=self.letra.render(reloj,True,self.color)
        pantalla.blit(imagen,self.pos)
