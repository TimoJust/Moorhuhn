import pygame
from settings import *


class ISprite:
    def update(self):
        raise NotImplementedError


class Ball(ISprite):
    def __init__(self, x, y, sx, sy, image):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.image = image
        self.ball_rect = image.get_rect()

    def update(self):
        # Ballbewegung
        self.x = self.x + self.sx
        self.y = self.y + self.sy
        self.ball_rect.topleft = (self.x, self.y)

        if self.ball_rect.right > WIDTH or self.ball_rect.left < 0:
            self.sx = self.sx * -1
        if self.ball_rect.bottom > HEIGHT or self.ball_rect.top < 0:
            self.sy = self.sy * -1

    def render(self, screen):
        screen.blit(self.image, self.ball_rect)
