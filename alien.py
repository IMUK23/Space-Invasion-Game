import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        super().__init()
        self.screen=screen
        self.ai_settings=ai_settings
        #loading the image of the alien from the computer file
        self.image=pygame.image.load('images\alien.bmp')
        self.rect=self.image.get_rect()

        #start the image of the alien from the left most corner of the screen
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        #storing the position of the alien
        self.x=float(self.rect.x)
    
    def blitme():
        self.screen.blit(self.image,self.rect)

