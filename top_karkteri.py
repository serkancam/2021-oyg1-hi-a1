import pygame

class Top(pygame.sprite.Sprite):
    def __init__(self,x,y,renk,genislik,yukseklik):
        # super.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((genislik,yukseklik))
        self.image.fill(renk)
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
    def update(self):
        self.rect.x=self.rect.x+5

