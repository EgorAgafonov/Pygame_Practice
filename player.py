import sys
import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('images/1.png'))
        self.sprites.append(pygame.image.load('images/2.png'))
        self.sprites.append(pygame.image.load('images/3.png'))
        self.sprites.append(pygame.image.load('images/4.png'))
        self.sprites.append(pygame.image.load('images/5.png'))
        self.sprites.append(pygame.image.load('images/6.png'))
        self.sprites.append(pygame.image.load('images/7.png'))
        self.sprites.append(pygame.image.load('images/8.png'))
        self.sprites.append(pygame.image.load('images/9.png'))
        self.sprites.append(pygame.image.load('images/10.png'))
        self.sprites.append(pygame.image.load('images/11.png'))
        self.sprites.append(pygame.image.load('images/12.png'))
        self.sprites.append(pygame.image.load('images/13.png'))
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
                self.is_animating = False
            self.image = self.sprites[int(self.current_sprite)]