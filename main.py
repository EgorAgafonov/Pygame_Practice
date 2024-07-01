import sys
import pygame
from player import Player
from buildings import House


# General setup
pygame.init()
clock = pygame.time.Clock()

# Game screen
screen_width = 1290
screen_height = 1024
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sprite animation')

# Creating sprites and groups
moving_player = pygame.sprite.Group()
moving_house = pygame.sprite.Group()
player = Player(screen_width / 2, screen_height / 2 + 195)
house = House(screen_width / 2, screen_height / 2)
moving_house.add(house)
moving_player.add(player)

# Text Variables
house_name = 'ДОМ БЫТА'
text_settings = pygame.font.Font('freesansbold.ttf', 24)


def run_game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    player.animate()
        house.animate()
        screen.fill((255, 255, 255))
        moving_house.draw(screen)
        moving_player.draw(screen)
        moving_house.update(0.1)
        moving_player.update(0.2)
        house_text = text_settings.render(house_name, False, 'black')
        screen.blit(house_text, (screen_width / 2 - 80, screen_height / 2 + 105))
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    run_game()
