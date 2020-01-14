import sys,pygame
from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group 
from bullets import Bullet
def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.width,ai_settings.height))
    pygame.display.set_caption("Space Invasion")
    ship=Ship(ai_settings,screen)
    bullets=Group()
    while True:
        gf.check_event(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)
        pygame.display.flip()
run_game()

    
