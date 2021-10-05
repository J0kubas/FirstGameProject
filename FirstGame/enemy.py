import pygame,os

class Ship:
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.healt = health
        self.ship_img = None
        self.laser_image = None
        self.lasers = []
        self.cool_down_counter = 0
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

class Enemy(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health=health)
        ship_img = pygame.image.load(os.path.join("FirstGame\\Assets","Asteroid (anim1).png"))
        self.ship_img = ship_img
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.x -= vel
      

