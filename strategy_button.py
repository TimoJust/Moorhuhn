import pygame
from settings import *

class IDisplay_Button_Behavior:
    def display(self):
        raise NotImplementedError
class Pennybutton(IDisplay_Button_Behavior):
    def display(self):
        pennybutton = pygame.image.load("pennybutton.jpg")
        pennybutton_rect = pennybutton.get_rect()
        pennybutton_rect.center = (320, 360)
        screen.blit(pennybutton,pennybutton_rect)
class Kneipebutton(IDisplay_Button_Behavior):
    def display(self):
        kneipebutton = pygame.image.load("kneipebutton.jpg")
        kneipebutton_rect = kneipebutton.get_rect()
        kneipebutton_rect.center = (960, 360)
        screen.blit(kneipebutton,kneipebutton_rect)
class Bahnhofbutton(IDisplay_Button_Behavior):
    def display(self):
        bahnhofbutton = pygame.image.load("bahnhofbutton.jpg")
        bahnhofbutton_rect = bahnhofbutton.get_rect()
        bahnhofbutton_rect.center = (640, 360)
        screen.blit(bahnhofbutton,bahnhofbutton_rect)
class Button:
    def __init__(self, dp: IDisplay_Button_Behavior):
        self.auswählen = dp
    def button_anzeigen(self):
        self.auswählen.display(self)

pennybutton = Button(Pennybutton)
kneipebutton = Button(Kneipebutton)
bahnhofbutton = Button(Bahnhofbutton)