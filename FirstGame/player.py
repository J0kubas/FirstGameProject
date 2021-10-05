import pygame, os
class Player(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y,health = 100,shields = 100):
        super().__init__()
        """ self.image = pygame.Surface([16,16])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y] """
        self.sprites = []
        self.is_animating = False
        self.size_x = 50
        self.size_y = 50
        self.animation_speed = 0.2
        Spaceship_image = pygame.image.load(os.path.join('FirstGame','Assets','SpaceShip (moving2).png'))
        self.sprites.append(pygame.transform.scale(Spaceship_image,(self.size_x,self.size_y)))
        Spaceship_image = pygame.image.load('FirstGame/Assets/SpaceShip (moving2).png')
        self.sprites.append(pygame.transform.scale(Spaceship_image,(self.size_x,self.size_y)))
        Spaceship_image = pygame.image.load('FirstGame/Assets/SpaceShip (moving3).png')
        self.sprites.append(pygame.transform.scale(Spaceship_image,(self.size_x,self.size_y)))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = [pos_x,pos_y]
    def animate(self):
        self.is_animating = True
    def stop_animating(self):
        self.is_animating = False
    def update(self):
        if self.is_animating == True:
            self.current_sprite += self.animation_speed
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
            self.image = self.sprites[int(self.current_sprite)]
        else:
            self.image = self.sprites[0]