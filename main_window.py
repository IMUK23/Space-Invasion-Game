import sys,pygame
from setting import Settings
from ship import Ship
import game_functions as gf
def run_game():
    pygame.init()
    ##ai_setting is an object of Setting class
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.width,ai_settings.height))
    pygame.display.set_caption("Space Invasion")
    ship=Ship(screen)
    while True:
        gf.check_events(ship)
        screen.fill(ai_settings.bgcolor)        
        ship.blitme()
        pygame.display.flip()
run_game()

