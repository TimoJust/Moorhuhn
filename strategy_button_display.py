"""Autor: Timo Just
In diesem Pattern geht es ausschließlich um die Optik, Schrift und Position der Buttons
Es können beliebig neue Helden- und/oder neue Levelbuttons hinzugefügt werden.
Die ganz unten erstellten Instanzen werden flexibel in den strategy_hintergrund_display Klassen genutzt, um auf dem Hintergrund die Buttons darzustellen. 
"""

import pygame
from settings import *

class IDisplay_Button_Behavior:
    def display(self):
        raise NotImplementedError
class Button:
    def __init__(self, sbd: IDisplay_Button_Behavior):
        self.auswählen = sbd
    def button_anzeigen(self):
        self.auswählen.display(self)

#Bilder der Buttons für die Level
class Penny_Button(IDisplay_Button_Behavior):
    def display(self):
        #In folgenden 4 Zeilen wird Bild geladen und Position bestimmt
        pennybutton = pygame.image.load("pennybutton.jpg")
        pennybutton_rect = pennybutton.get_rect()
        pennybutton_rect.center = (320, 360)
        screen.blit(pennybutton,pennybutton_rect)
        #Hier der Text über dem Levelbutton
        font = pygame.font.SysFont("comicsansms", 40)
        text = font.render("Penny", True, (0, 0, 0))
        text_position = (270,180)
        screen.blit(text,text_position)
class Kneipe_Button(IDisplay_Button_Behavior):
    def display(self):
        kneipebutton = pygame.image.load("kneipebutton.jpg")
        kneipebutton_rect = kneipebutton.get_rect()
        kneipebutton_rect.center = (960, 360)
        screen.blit(kneipebutton,kneipebutton_rect)
        font = pygame.font.SysFont("comicsansms", 40)
        text = font.render("Kneipe", True, (0, 0, 0))
        text_position = (900,180)
        screen.blit(text,text_position)
class Bahnhof_Button(IDisplay_Button_Behavior):
    def display(self):
        bahnhofbutton = pygame.image.load("bahnhofbutton.jpg")
        bahnhofbutton_rect = bahnhofbutton.get_rect()
        bahnhofbutton_rect.center = (640, 360)
        screen.blit(bahnhofbutton,bahnhofbutton_rect)
        font = pygame.font.SysFont("comicsansms", 40)
        text = font.render("Bahnhof", True, (0, 0, 0))
        text_position = (570,180)
        screen.blit(text,text_position)

#Bilder der Buttons für die Helden
class Maria_Cron_Button(IDisplay_Button_Behavior):
    def display(self):
        mariacronbutton = pygame.image.load("superhero.png")
        mariacronbutton_rect = mariacronbutton.get_rect()
        mariacronbutton_rect.center = (320, 360)
        screen.blit(mariacronbutton,mariacronbutton_rect)
        font = pygame.font.SysFont("comicsansms", 40)
        text = font.render("Wonder Maria Cron", True, (0, 0, 0))
        text_position = (160,180)
        screen.blit(text,text_position)
class Jack_Daniels_Button(IDisplay_Button_Behavior):
    def display(self):
        jackdanielsbutton = pygame.image.load("pirate.png")
        jackdanielsbutton_rect = jackdanielsbutton.get_rect()
        jackdanielsbutton_rect.center = (960, 360)
        screen.blit(jackdanielsbutton,jackdanielsbutton_rect)
        font = pygame.font.SysFont("comicsansms", 40)
        text = font.render("Captain Jack Daniels", True, (0, 0, 0))
        text_position = (780,180)
        screen.blit(text,text_position)

#Spielende
class Button_nochmal_spielen(IDisplay_Button_Behavior):
    def display(self):
        button = pygame.Rect(380, 200, 450, 100)
        pygame.draw.rect(screen,SCHWARZ,button)
        button_rand = pygame.Rect(380, 200, 450, 100)
        pygame.draw.rect(screen,BLAU,button_rand,10)
        font = pygame.font.SysFont("comicsansms", 40)
        text = font.render("Nochmal büdde!", True, WEISS)
        text_position = (400,220)
        screen.blit(text,text_position)
        pygame.display.update()
class Button_genug_ist_genug(IDisplay_Button_Behavior):
    def display(self):
        button = pygame.Rect(380, 400, 450, 100)
        pygame.draw.rect(screen,SCHWARZ,button)
        button_rand = pygame.Rect(380, 400, 450, 100)
        pygame.draw.rect(screen,BLAU,button_rand,10)
        font = pygame.font.SysFont("comicsansms", 40)
        text = font.render("Ich kann nicht mehr!", True, WEISS)
        text_position = (400,420)
        screen.blit(text,text_position)
        pygame.display.update()

#Hier Instanziierung
pennybutton = Button(Penny_Button)
kneipebutton = Button(Kneipe_Button)
bahnhofbutton = Button(Bahnhof_Button)
mariabutton = Button(Maria_Cron_Button)
jackbutton = Button(Jack_Daniels_Button)
nochmal_spielen_button = Button (Button_nochmal_spielen)
nicht_weiter_spielen = Button(Button_genug_ist_genug)

#Über diese Methodenaufrufe Zugriff auf einzelne Buttons
#pennybutton.button_anzeigen()
#kneipebutton.button_anzeigen()
#bahnhofbutton.button_anzeigen()
#mariabutton.button_anzeigen()
#jackbutton.button_anzeigen()
#nochmal_spielen_button.button_anzeigen()
#nicht_weiter_spielen.button_anzeigen()