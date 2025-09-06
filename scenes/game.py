'''
Hola este es modulo game,
este modulo manejara la escena donde ocurre nuestro juego
'''

if __name__ == "__main__": # Solo para que no ejecutes este archivo
    import sys
    print(
        "\033[38;2;255;0;0mESTE MODULO NO DEBE EJECUTARSE. EJECUTAR main.py\033[0m\n"
        * 3
    )
    sys.exit()

import pygame

from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

from elements.jorge import Player

from elements.bug import Enemy

from elements.mira import Mirilla

from scenes.muerte import gameOver

from elements.cronometro import Tiempo

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
pygame.mixer.init()
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

def gameLoop():
    ''' iniciamos los modulos de pygame'''

    pygame.init()

    pygame.mixer.music.load("assets/musica/musica.mp3")
    pygame.mixer.music.play(-1)


    ''' Creamos y editamos la ventana de pygame (escena) '''
    ''' 1.-definir el tamaño de la ventana'''

    ''' 2.- crear el objeto pantalla'''
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image = pygame.image.load("assets/pixelBackground.jpg").convert()

    ''' Preparamos el gameloop '''
    #creamos las imagenes de los corazones, convert_alpha le quita el fondo negro a la imagen
    corazon=pygame.image.load("assets/corazon.png").convert_alpha()
    corazon=pygame.transform.scale(corazon,(50,50))

    ''' 1.- creamos el reloj del juego'''

    clock = pygame.time.Clock()
    ''' 2.- generador de enemigos'''

    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 600)

    ''' 3.- creamos la instancia de jugador'''
    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

    ''' 4.- contenedores de enemigos y jugador'''
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    #creacion de la mira
    mira=Mirilla(SCREEN_WIDTH,SCREEN_HEIGHT)
    all_sprites.add(mira)

    #creamos el cronometro
    cronometro= Tiempo()

    #creamos el puntaje
    puntaje=0
    letra_puntaje= pygame.font.SysFont("algerian", 25)


    ''' hora de hacer el gameloop '''
    # variable booleana para manejar el loop
    running = True

    # loop principal del juego

    while running:

        screen.blit(background_image, [0, 0])
        
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        
        # POR HACER (2.5): Pintar proyectiles en pantalla
        for projectile in player.projectiles:
            screen.blit(projectile.surf,projectile.rect)
        
        #tenemos en pantalla la cantidad de vidas que tiene el jugador, las imagenes las separamos entre 50 
        for i in range(player.vidas):
            screen.blit(corazon, (10+i*50,10))
        
        # POR HACER (2.5): Eliminar bug si colisiona con proyectil
        #tomamos el sistema de eliminaciones y lo vamos sumando al puntaje cada vez que matamos a un enemigo
        eliminaciones=pygame.sprite.groupcollide(enemies,player.projectiles,True,True)
        puntaje+=len(eliminaciones)
        
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        enemies.update()
        #actualizar la mira con el movimiento
        mira.update()
        
        choque= pygame.sprite.spritecollideany(player, enemies)
        if choque:
            #matamos al enemigo con el que choca y restamos una vida
            choque.kill()
            player.perder_vida()

            if player.vidas<=0:
                #si tiene 0 vidad se termina el juego
                player.kill()
                running = False
            #si se muere, se empieza el loop de la escena de muerte
                gameOver()
            
        cronometro.imagen(screen)

        #dibujamos el puntaje abajo de los corazones
        score=letra_puntaje.render(f"Score: {puntaje}", True, (255,255,255))
        screen.blit(score, (10, 60))

        pygame.display.flip()
        
        # iteramos sobre cada evento en la cola
        for event in pygame.event.get():
            # se presiono una tecla?
            if event.type == KEYDOWN:
                # era la tecla de escape? -> entonces terminamos
                if event.key == K_ESCAPE:
                    running = False

            # fue un click al cierre de la ventana? -> entonces terminamos
            elif event.type == QUIT:
                running = False
            
            elif event.type == ADDENEMY:
                new_enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            
            # POR HACER (2.4): Agregar evento disparo proyectil
            elif event.type==pygame.MOUSEBUTTONDOWN:
                player.shoot(pygame.mouse.get_pos())


        clock.tick(40)
