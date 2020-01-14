import sys,pygame
from bullets import Bullet
def check_event(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)
            
def check_keydown_event(event, ai_settings, screen, ship, bullets):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.moving_right=True
        elif event.key == pygame.K_LEFT:
            ship.moving_left=True 
        elif event.key == pygame.K_SPACE:
            firing_bullets(ai_settings, screen, ship,bullets)


def check_keyup_event(event,ship):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right=False
        elif event.key == pygame.K_LEFT:
                ship.moving_left=False

def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bgcolor)
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def firing_bullets(ai_settings, screen, ship, bullets):
    if len(bullets)<ai_settings.bullets_allowed:
        new_bullet=Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
