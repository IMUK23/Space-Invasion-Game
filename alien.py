import pygame 
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        super().__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        #loading the image of the alien from the computer file
        self.image=pygame.image.load('alien.bmp')
        self.rect=self.image.get_rect()

        #start the image of the alien from the left most corner of the screen
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        #storing the position of the alien
        self.x=float(self.rect.x)
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return true
    
    def update(self):
        #Move the fleet to right => fleet_direection=1 and if fleet moves left => fleet_direction=-1
        
        self.x +=(self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
        self.rect.x =(self.x)
    
    

        
