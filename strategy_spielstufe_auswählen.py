"""
Autor: Timo Just
Strategy Pattern erstellt um die einzelnen Spielstufen/Ebenen zu erstellen, hier derzeit Startbildschirm,Namenseingabe, Heldenauswahl, Levelauswahl...
Dieses Pattern erstellt je nach Spielstufe das Verhalten, was passiert wenn auf Button X,Y gedrückt wird
Die Strategys werden dann in den Hauptteil übergeben. Es kann beliebig die Reihenfolgen oder grundsätzlich Spielstufe geändert werden. Jederzeit erweiterar und von außen aufrufbar.
"""
import pygame
import sys
from pygame.locals import *
from strategy_hintergrund_display import*
#from strategy_button_position import* -> hier hätte ich gerne [x, y = pygame.mouse.get_pos(); pygame.Rect(...) und .collidepoint(x, y) eingespart) -> funktioniert leider nicht :( ]

class ISpielstufe_Behavior:
    def ausführen(self):
        raise NotImplementedError
class Spielstufe:
    def __init__(self, sla: ISpielstufe_Behavior):
        self.sla = sla
    def spielstufe_ausführen(self):
        self.sla.ausführen(self)

#Startbildschirm
class Spielstufe_Startbildschirm(ISpielstufe_Behavior):
    def ausführen(self):
        """Schleife Startbildschirm: Besteht aus Hintergrund, Koordinaten des Buttons der Start-Schrift
           sowie der if-Anweisung für die Bedingung beim Klicken auf den Button"""
        running = True
        while running:
            #Import des Hintergrundbildes aus strategy_hintergrund_display
            startseite.hintergrund_anzeigen()
            #Position der Schrift "Start" als erstelltes Rechteck
            button_start = pygame.Rect(390,620, 380, 80)
            for event in pygame.event.get():
                #Möglichkeit das Spiel zu beenden über x
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #Hier wird das Verhalten erstellt: Was passiert wenn Mausklick und gleichzeitig Mausposition in erstelltem Rechteck
                if event.type == MOUSEBUTTONDOWN and button_start.collidepoint(event.pos):
                    #jetzt Abbruch, damit im Hauptteil die nächste Stufe übergeben werden kann
                    running = False

#Klasse erstellt um den eingebenen Namen per Return zurück zu bekommen -> Übergabe an Highscore
"""class Gamer:
    def __init__(self):
        self.spielername = None

        return"""

#Namenseingabe
class Spielstufe_Namenseingabe(ISpielstufe_Behavior):
    def ausführen(self):
        schrift_namenseingabe = pygame.font.SysFont("comicsansms", 35)
        #spielername = Spielername
        #global spielername
        #spielername = Gamer
        spielername = ""
        eingabe_button = pygame.Rect(390,342.5,140,50)
        #Farbe des Rechtecks, zur Spielernamen Eingabe, wenn angeklickt
        farbe_eingabe_aktiv = pygame.Color(BLAU)
        #Farbe des Rechtecks, zur Spielernamen Eingabe, wenn außerhalb des Rechtecks angeklickt
        farbe_eingabe_passiv = pygame.Color(SCHWARZ)
        farbe_eingabe_button = farbe_eingabe_passiv
        eingabe_aktiv = False
        running = True
        while running:
            #Hier wieder: Import des Hintergrundbildes aus strategy_hintergrund_display
            namenseingabe.hintergrund_anzeigen()
            #Hier wird das Rechteck erzeugt, in dem der Name eingegeben werden kann
            pygame.draw.rect(screen,farbe_eingabe_button,eingabe_button,5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #Wenn im Bereich des Namenseingabefenster Maus gedrückt, dann Eingabe wahr
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if eingabe_button.collidepoint(event.pos):
                        eingabe_aktiv = True
                    else:
                        eingabe_aktiv = False
                if event.type == pygame.KEYDOWN:
                    #Wenn Eingabe wahr, dann per Backspace möglich die eingebenen Buchstaben zu löschen oder per Enter aus der Eingabe auszusteigen oder eingebene Buchstaben darzustellen.
                    if eingabe_aktiv == True:
                        if event.key == pygame.K_BACKSPACE:
                            spielername = spielername[:-1]
                        elif event.key == pygame.K_RETURN:
                            eingabe_aktiv = False
                        else:
                            spielername += event.unicode                        
                #Hier die Farbänderung, wenn Button geklickt(und somit eingabe_aktiv wahr), dann Rand des Eingabefensters blau, wenn nicht oder außerhalb, dann schwarz
                if eingabe_aktiv:
                    farbe_eingabe_button = farbe_eingabe_aktiv
                else:
                    farbe_eingabe_button = farbe_eingabe_passiv
                #Ab hier wieder die Koordinaten des Buttons "weiter", um bei "Kollision" in die nächste Spielstufe überzugehen
                button_weiter = pygame.Rect(390,600, 380, 80)
                if event.type == MOUSEBUTTONDOWN and button_weiter.collidepoint(event.pos):
                    running = False
            text_eingabe = schrift_namenseingabe.render(spielername,True,SCHWARZ)
            screen.blit(text_eingabe,(eingabe_button.x+7.5,eingabe_button.y+2.5))
            eingabe_button.w = max(150,text_eingabe.get_width()+10)
            pygame.display.update()
#print (spielername)

#Heldenauswahl
class Spielstufe_Heldenauswahl(ISpielstufe_Behavior):
    def ausführen(self):
        running = True
        while running:
            startseite_Heldenauswahl.hintergrund_anzeigen()
            button_held_1 = pygame.Rect(192.5, 232.5, 255, 255)
            button_held_2 = pygame.Rect(832.5, 232.5, 255, 255)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()    
                if event.type == MOUSEBUTTONDOWN and (button_held_1.collidepoint(event.pos) or button_held_2.collidepoint(event.pos)):
                    running = False   

#Levelauswahl
class Spielstufe_Levelauswahl(ISpielstufe_Behavior):
    def ausführen(self):
        running = True
        while running:      
            startseite_Levelauswahl.hintergrund_anzeigen()
            button_level_1 = pygame.Rect(192.5, 232.5, 255, 255)
            button_level_2 = pygame.Rect(512.5, 232.5, 255, 255)
            button_level_3 = pygame.Rect(832.5, 232.5, 255, 255)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN and button_level_1.collidepoint(event.pos):
                        running = False
                if event.type == MOUSEBUTTONDOWN and button_level_2.collidepoint(event.pos):
                        running = False
                if event.type == MOUSEBUTTONDOWN and button_level_3.collidepoint(event.pos):
                    running = False

#Spielendbildschirm
class Spielende(ISpielstufe_Behavior):
    def ausführen(self):
        spielende.hintergrund_anzeigen()
        button_nochmal_spielen = pygame.Rect(380, 200, 450, 100)
        button_beenden = pygame.Rect(380, 400, 450, 100)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN and button_nochmal_spielen.collidepoint(event.pos):
                        spielstufe_Startbildschirm.spielstufe_ausführen()
                        spielstufe_Namenseingabe.spielstufe_ausführen()
                        spielstufe_Heldenauswahl.spielstufe_ausführen()
                        spielstufe_Levelauswahl.spielstufe_ausführen()
                        spielstufe_Spielende.spielstufe_ausführen()
                if event.type == MOUSEBUTTONDOWN and button_beenden.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

#Hier Instanziierung
spielstufe_Startbildschirm = Spielstufe(Spielstufe_Startbildschirm)
spielstufe_Namenseingabe = Spielstufe(Spielstufe_Namenseingabe)
spielstufe_Heldenauswahl = Spielstufe(Spielstufe_Heldenauswahl)
spielstufe_Levelauswahl = Spielstufe(Spielstufe_Levelauswahl)
spielstufe_Spielende = Spielstufe(Spielende)

#Hier Methodenaufrufe von .spielstufe_ausführen() über die erstellten Instanzen 
#Hier kann Spiel aufgerufen werden wenn Raute entfernt bei #spielstufe_Startbildschirm.spielstufe_ausführen() zum testen
#spielstufe_Startbildschirm.spielstufe_ausführen()
#spielstufe_Namenseingabe.spielstufe_ausführen()
#spielstufe_Heldenauswahl.spielstufe_ausführen()
#spielstufe_Levelauswahl.spielstufe_ausführen()
#spielstufe_Spielende.spielstufe_ausführen()
