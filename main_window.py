import sys,pygame
from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group 
from alien import Alien
from bullets import Bullet  
def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.width,ai_settings.height))
    pygame.display.set_caption("Space Invasion")
    #creating ship on screen
    ship=Ship(ai_settings,screen)
    # creating alien on screen
    aliens=Group()
    #making bullets as group
    bullets=Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    while True:
        gf.check_event(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
        gf.update_aliens(ai_settings,aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        pygame.display.flip()
run_game()

    

