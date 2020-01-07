import sys,pygame
from setting import Settings
def run_game():
    pygame.init()
    ##ai_setting is an object of Setting class
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.width,ai_settings.height))
    pygame.display.set_caption("Space Invasion")
    while True:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bgcolor)        
        pygame.display.flip()
run_game()

