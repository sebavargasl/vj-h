import pygame

from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

from elements.jorge import Player

from elements.bug import Enemy

from elements.mira import Mirilla

def gameOver():
    pygame.init()

    ''' Creamos y editamos la ventana de pygame (escena) '''
    ''' 1.-definir el tamaño de la ventana'''
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 700

    ''' 2.- crear el objeto pantalla'''
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image = pygame.image.load("assets/gameover.png").convert()
    #arreglo las dimensiones de la imagen a la pantalla del juego
    background_image=pygame.transform.scale(background_image,(SCREEN_WIDTH,SCREEN_HEIGHT))

    ''' Preparamos el gameloop '''
    ''' 1.- creamos el reloj del juego'''

    clock = pygame.time.Clock()

    #creamos el loop siguiendo la misma logica, para cuando se omime escape o se cierra la ventana
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==QUIT:
                running=False
            elif event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    running=False
        
        screen.blit(background_image, [0, 0])
        pygame.display.flip()

        clock.tick(40)
    pygame.quit()