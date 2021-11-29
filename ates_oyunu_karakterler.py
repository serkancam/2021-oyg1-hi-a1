import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,renk,secim):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,20))
        self.image.fill(renk)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.hiz=0
        self.secim=secim
    def update(self):
        self.hiz=0
        tuslar = pygame.key.get_pressed()
        if self.secim==0:
            if tuslar[pygame.K_LEFT]:
                self.hiz=-5
            elif tuslar[pygame.K_RIGHT]:
                self.hiz=5
        elif self.secim==1:
            if tuslar[pygame.K_a]:
                self.hiz=-5
            elif tuslar[pygame.K_d]:
                self.hiz=5
        self.rect.x+=self.hiz
        if self.rect.left>360:
            self.rect.right=0
        elif self.rect.right<0:
            self.rect.left=360

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,renk):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((10,15))
        self.image.fill(renk)
        self.rect = self.image.get_rect()
        self.rect.centerx=x
        self.rect.bottom=y
    def update(self):
        self.rect.y-=10
        if self.rect.bottom<0:
            self.kill()