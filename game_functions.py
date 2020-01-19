import sys,pygame
from bullets import Bullet
from alien import Alien
def check_event(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)
            #if Q is pressed game will exit 
        elif event.type == pygame.K_q:
            system.exit()
            
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

def update_screen(ai_settings, screen, ship, alien, bullets):
    screen.fill(ai_settings.bgcolor)
    ship.blitme()
    alien.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
#creating the fleet of aliens 
def get_number_aliens_x(ai_settings,alien_width):
    #determine the number of aliens in a row
    available_space=ai_settings.width-2*alien_width
    number_aliens_x=int(available_space/alien_width)
    return number_aliens_x
def get_number_rows(ai_settings,ship_height,alien_height):
    available_space_y=(ai_settings.height-(3 * alien_height) - ship_height)
    number_rows=int(available_space_y/(2 * alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number ,row_number):
    alien=Alien(ai_settings,screen)
    alien_width=alien.rect.width
    alien.x=alien_width + 2 * alien_width * alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
    """creating the full fleet of aliens
    creating an alien and finding the number of aliens in a row
    spacing between each alien is equal to one"""
    #creating first row of aliens
    alien=Alien(ai_settings,screen)
    number_aliens_x=get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows=get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    #creating rowise fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)
    
def update_bullets(ai_settings,screen,ship,aliens,bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(ai_settings,screen,ship,aliens,bullets)
    
def check_bullet_alien_collision(ai_settings,screen,ship,aliens,bullets):
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)


def firing_bullets(ai_settings, screen, ship, bullets):
    if len(bullets)<ai_settings.bullets_allowed:
        new_bullet=Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_fleet_edges(ai_settings,aliens):
#Dropping the Fleet
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y =((alien.rect.y)+(ai_settings.fleet_drop_speed))
    ai_settings.fleet_direction *= -1.00
    #Update the position of fleet

def update_aliens(ai_settings,aliens):
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
