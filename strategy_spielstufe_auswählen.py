#Autor: Timo Just
#Strategy Pattern erstellt um die einzelnen Spielstufen, hier derzeit Startbildschirm,Heldenauswahl, Levelauswahl... dem State Pattern zu übergeben. beliebig erweiterbar um z.B. Spielmodusauswahl oder ähnlich
#Dieses Pattern erstellt je nach Spielstufe das Verhalten, was passiert wenn auf Button X,Y gedrückt
#Es können beliebig die Reihenfolgen oder grundsätzlich Spielstufen geändert werden in dem unter if event.type == MOUSEBUTTONDOWN... eine Alternative eingefügt wird

import pygame
from strategy_hintergrund_display import*
from strategy_ausführen import*
#from strategy_button_position import* -> hier hätte ich gerne [x, y = pygame.mouse.get_pos(); pygame.Rect(...) und .collidepoint(x, y) eingespart) -> funktioniert leider nicht :( ]

class ISpielstufe_Behavior:
    def ausführen(self):
        raise NotImplementedError
#Startbildschirm
class Spielstufe_Startbildschirm(ISpielstufe_Behavior):
    def ausführen(self):
        #programm_schließen.button_ausführen()
        #Schleife Startbildschirm: Besteht aus Hintergrund, der lokalen Variable für die Mausposition, der lokalen Variablen für die Koordinaten des Buttons 
        #sowie der if-Anweisung für die Bedingung beim Klicken auf den Button
        while True:
            #Import des Hintergrundbildes aus strategy_hintergrund_display
            startseite.hintergrund_anzeigen()
            #Mausposition
            x, y = pygame.mouse.get_pos()
            #Position der Schrift "Start" als erstelltes Dreieck
            button_start = pygame.Rect(390,620, 380, 80)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #Hier wird das Verhalten erstellt: Was passiert wenn Mausklick und gleichzeitig Mausposition in erstelltem Rechteck
                if event.type == MOUSEBUTTONDOWN and button_start.collidepoint(x, y):
                    #Dann Wechsel zur nächsten bzw. gewünschten Spielstufe
                    spielstufe_Namenseingabe.spielstufe_ausführen()
#Namenseingabe
class Spielstufe_Namenseingabe(ISpielstufe_Behavior):
    def ausführen(self):
        schrift_namenseingabe = pygame.font.SysFont("comicsansms", 35)
        spielername = ""
        eingabe_button = pygame.Rect(390,342.5,140,50)
        farbe_eingabe_aktiv = pygame.Color(BLAU)
        farbe_eingabe_passiv = pygame.Color(SCHWARZ)
        farbe_eingabe_button = farbe_eingabe_passiv
        eingabe_aktiv = False
        while True:
            namenseingabe.hintergrund_anzeigen()
            #Hier wird das Rechteck erzeugt
            pygame.draw.rect(screen,farbe_eingabe_button,eingabe_button,5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if eingabe_button.collidepoint(event.pos):
                        eingabe_aktiv = True
                    else:
                        eingabe_aktiv = False
                if event.type == pygame.KEYDOWN:
                    if eingabe_aktiv == True:
                        if event.key ==pygame.K_BACKSPACE:
                            spielername = spielername[:-1]
                        else:
                            spielername += event.unicode
                x, y = pygame.mouse.get_pos()
                button_weiter = pygame.Rect(390,600, 380, 80)
                if event.type == MOUSEBUTTONDOWN and button_weiter.collidepoint(x, y):
                    spielstufe_Heldenauswahl.spielstufe_ausführen()
            if eingabe_aktiv:
                farbe_eingabe_button = farbe_eingabe_aktiv
            else:
                farbe_eingabe_button = farbe_eingabe_passiv
            text_eingabe = schrift_namenseingabe.render(spielername,True,SCHWARZ)
            screen.blit(text_eingabe,(eingabe_button.x+7.5,eingabe_button.y+2.5))
            eingabe_button.w = max(100,text_eingabe.get_width()+10)
            pygame.display.update()
#Heldenauswahl
class Spielstufe_Heldenauswahl(ISpielstufe_Behavior):
    def ausführen(self):
        while True:
            startseite_Heldenauswahl.hintergrund_anzeigen()
            x, y = pygame.mouse.get_pos()
            button_held_1 = pygame.Rect(192.5, 232.5, 255, 255)
            button_held_2 = pygame.Rect(832.5, 232.5, 255, 255)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()    
                if event.type == MOUSEBUTTONDOWN and (button_held_1.collidepoint(x, y) or button_held_2.collidepoint(x, y)):
                    spielstufe_Levelauswahl.spielstufe_ausführen()   
#Levelauswahl
class Spielstufe_Levelauswahl(ISpielstufe_Behavior):
    def ausführen(self):
        while True:      
            startseite_Levelauswahl.hintergrund_anzeigen()
            x, y = pygame.mouse.get_pos()
            button_level_1 = pygame.Rect(192.5, 232.5, 255, 255)
            button_level_2 = pygame.Rect(512.5, 232.5, 255, 255)
            button_level_3 = pygame.Rect(832.5, 232.5, 255, 255)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN and button_level_1.collidepoint(x, y):
                    while True:
                        penny.hintergrund_anzeigen()
                        programm_schließen.button_ausführen()
                if event.type == MOUSEBUTTONDOWN and button_level_2.collidepoint(x, y):
                    while True:
                        bahnhof.hintergrund_anzeigen()
                        programm_schließen.button_ausführen()
                if event.type == MOUSEBUTTONDOWN and button_level_3.collidepoint(x, y):
                    while True:
                        kneipe.hintergrund_anzeigen()
                        programm_schließen.button_ausführen()

class Spielstufe:
    def __init__(self, sla: ISpielstufe_Behavior):
        self.sla = sla
    def spielstufe_ausführen(self):
        self.sla.ausführen(self)

spielstufe_Startbildschirm = Spielstufe(Spielstufe_Startbildschirm)
spielstufe_Namenseingabe = Spielstufe(Spielstufe_Namenseingabe)
spielstufe_Heldenauswahl = Spielstufe(Spielstufe_Heldenauswahl)
spielstufe_Levelauswahl = Spielstufe(Spielstufe_Levelauswahl)
spielstufe_Übergabe_Spiellogik = Spielstufe(Spielstufe_Startbildschirm)
#spielstufe_Startbildschirm.spielstufe_ausführen()
#spielstufe_Namenseingabe.spielstufe_ausführen()
#spielstufe_Heldenauswahl.spielstufe_ausführen()
#spielstufe_Levelauswahl.spielstufe_ausführen()
#spielstufe_Übergabe_Spiellogik.spielstufe_ausführen()
