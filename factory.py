import pygame
import os
import random
from sprites import *
from settings import *


class Factory:
    def __init__(self):
        self.sprite_list = []
        # Hier Grafiken einbinden
        self.image_dict = {}
        game_folder = os.path.dirname(__file__)
        self.image_dict["bier"] = pygame.image.load(
            os.path.join(game_folder, "bier.png"))

        #10.05.2021 Malte Background Image Anfang
        self.background_image = pygame.image.load(os.path.join(game_folder, "hintergrund.png"))
        #10.05.2021 Malte Background Image Ende   

    def generateSprites(self):
        # sprites
        for _ in range(30):
            ball = Ball(random.randint(20, WIDTH-20),
                        random.randint(20, HEIGHT-20), random.randint(2, 5), random.randint(2, 5), self.image_dict["bier"])
            self.sprite_list.append(ball)

    def generateSpriteFromMouse(self, x, y):
        ball = Ball(x, y, random.randint(2, 5),
                    random.randint(2, 5), self.image_dict["bier"])
        self.sprite_list.append(ball)

    def getSprites(self):
        return self.sprite_list
