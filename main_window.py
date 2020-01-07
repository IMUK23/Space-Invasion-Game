import sys,pygame
def run_game():
    pygame.init()
    screen=pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Space Invasion")
    bgcolor=(230,230,230)
    while True:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                sys.exit()
        screen.fill(bgcolor)        
        pygame.display.flip()
run_game()

