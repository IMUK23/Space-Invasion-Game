import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        super().__init__()
        self.screen=screen

        #Creating the Bullet Rect at (0,0) then changing the position#
        self.rect=pygame.Rect(0,0,ai_settings.bullets_width,ai_settings.bullets_height)
        #Bullet will move from ship center and top and where the ship go bullet move from there only so that's why we are here giving bullet rect as ship rect#
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top

        #storing the Bullets location 
        self.y=float(self.rect.y)

        self.color=ai_settings.bullets_color
        self.speed_factor=ai_settings.bullets_speed_factor
    def update(self):
        #Move bullet up the screeen
        self.y -= self.speed_factor
        self.rect.y=self.y
    def draw_bullet(self):
        #Draw bullet to screen
        pygame.draw.rect(self.screen,self.color,self.rect)
