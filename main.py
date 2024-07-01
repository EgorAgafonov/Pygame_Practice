import sys
import pygame
from player import Player


# General setup
pygame.init()
clock = pygame.time.Clock()

# Game screen
screen_width = 1290
screen_height = 1024
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sprite animation')

# Creating sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(100, 100)
moving_sprites.add(player)


def run_game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    player.animate()



        screen.fill((255, 255, 255))
        moving_sprites.draw(screen)
        moving_sprites.update(0.2)
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    run_game()
