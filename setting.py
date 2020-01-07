### This will edit the setting of the game  ###
class Settings():
    def __init__(self):
        self.width=1200
        self.height=800
        self.bgcolor=(230,230,230)
         self.moving_right=False
        self.moving_left=False
    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
