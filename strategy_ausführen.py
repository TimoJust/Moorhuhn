#Autor: Timo Just

import pygame
import sys
from pygame.locals import *

class IAktion_Behavior:
    def aktion(self):
        raise NotImplementedError
class Schließen(IAktion_Behavior):
    def aktion(self):
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()     
class Aktion:
    def __init__(self, sa: IAktion_Behavior):
        self.sa = sa
    def button_ausführen(self):
        self.sa.aktion(self)

programm_schließen = Aktion(Schließen)
#programm_schließen.button_ausführen()


