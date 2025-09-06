if __name__ == "__main__": # Solo para que no ejecutes este archivo
    import sys
    print(
        "\033[38;2;255;0;0mESTE MODULO NO DEBE EJECUTARSE. EJECUTAR main.py\033[0m\n"
        * 3
    )
    sys.exit()

import pygame


class Projectile(pygame.sprite.Sprite):
    
    def __init__(self, pos, direction, SCREEN_WIDTH, SCREEN_HEIGHT): 
        super(Projectile, self).__init__()
        
        # POR HACER (2.0): Aspecto y parámetros iniciales de la bala
        self.surf=pygame.Surface((10,10))
        self.surf.fill((255,255,255))
        self.rect=self.surf.get_rect(center=pos)
    
        # POR HACER (2.1): Parámetros iniciales de la bala
        self.speed=10
        self.direction=direction
        self.screen_width=SCREEN_WIDTH
        self.screen_height=SCREEN_HEIGHT
    
        

    def update(self): 
        
        # POR HACER (2.2): Mover la bala y eliminarla si se sale de la pantalla
        self.rect.move_ip(self.direction[0]*self.speed,self.direction[1]*self.speed)

        if (self.rect.left<0 or self.rect.right>self.screen_width or self.rect.top<0 or self.rect.bottom>self.screen_height):
            self.kill()
