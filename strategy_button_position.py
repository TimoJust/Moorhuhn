#Autor: Timo Just

import pygame
from pygame.locals import *
from settings import*

class IPosition_Behavior:
    def positionieren(self):
        raise NotImplementedError

#Position Startbutton
class Start_Button(IPosition_Behavior):
    def positionieren(self):
        self.x, self.y = pygame.mouse.get_pos()
        button_start = pygame.Rect(390,620, 380, 80)
        button_start.collidepoint(self.x, self.y)
        
#Position Heldenbuttons            
class Held_1_Button(IPosition_Behavior):
    def positionieren(self):
        x, y = pygame.mouse.get_pos()
        button_held_1 = pygame.Rect(192.5, 232.5, 255, 255)
        button_held_1.collidepoint(x, y)
class Held_2_Button(IPosition_Behavior):
    def positionieren(self):
        x, y = pygame.mouse.get_pos()
        button_held_2 = pygame.Rect(832.5, 232.5, 255, 255)
        button_held_2.collidepoint(x, y)

#Position Levelbuttons
class Level_1_Button(IPosition_Behavior):
    def positionieren(self):
        x, y = pygame.mouse.get_pos()
        button_level_1 = pygame.Rect(192.5, 232.5, 255, 255)
        button_level_1.collidepoint(x, y)
class Level_2_Button(IPosition_Behavior):
    def positionieren(self):
        x, y = pygame.mouse.get_pos()
        button_level_2 = pygame.Rect(512.5, 232.5, 255, 255)
        button_level_2.collidepoint(x, y)
class Level_3_Button(IPosition_Behavior):
    def positionieren(self):
        x, y = pygame.mouse.get_pos()
        button_level_3 = pygame.Rect(832.5, 232.5, 255, 255)
        button_level_3.collidepoint(x, y)

class Button_Position:
    def __init__(self, sbp: IPosition_Behavior):
        self.pos = sbp
    def button_position(self):
        self.pos.positionieren(self)

start_Button = Button_Position(Start_Button)
held_1_Button = Button_Position(Held_1_Button)
held_2_Button = Button_Position(Held_2_Button)
level_1_Button = Button_Position(Level_1_Button)
level_2_Button = Button_Position(Level_2_Button)
level_3_Button = Button_Position(Level_3_Button)

#start_Button.button_position()
#held_1_Button.button_position()
#held_2_Button.button_position()
#level_1_Button.button_position()
#level_2_Button.button_position()
#level_3_Button.button_position()

