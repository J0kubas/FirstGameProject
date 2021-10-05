import pygame, random
from player import Player
from enemy import *


WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

enemy_vel = 1
level = 0
enemy_wave = 5
enemies = []

moving_sprites = pygame.sprite.Group()
player = Player(100,100)
moving_sprites.add(player)

def redraw_window():

    WIN.fill(WHITE)

    for enemy in enemies:
        enemy.draw(WIN)

    moving_sprites.draw(WIN)
    moving_sprites.update()
    pygame.display.update()




def main():#
    global enemy_vel, level, enemies, enemy_wave
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        if len(enemies) == 0:
            level += 1
            enemy_wave += 5
            for i in range(enemy_wave):
                enemy = Enemy(random.randrange(WIDTH, WIDTH+1500), random.randrange(5,HEIGHT-5))
                enemies.append(enemy)




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.animate()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player.stop_animating()
        for enemy in enemies:
            enemy.move(enemy_vel)
        redraw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
