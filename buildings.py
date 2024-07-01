import sys
import pygame


class House(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('images/house_1.png'))
        self.sprites.append(pygame.image.load('images/house_2.png'))
        self.sprites.append(pygame.image.load('images/house_3.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def animate(self):

        self.is_animating = True

    def update(self, speed: int):
        if self.is_animating:
            self.current_sprite += speed
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
            self.image = self.sprites[int(self.current_sprite)]
