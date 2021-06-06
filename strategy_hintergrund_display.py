"""
Autor: Timo Just
In diesem Pattern geht es ausschließlich um die Optik und Schrift der Hintergründe
Es können beliebig neue Hintergründe hinzugefügt werden, um diese dann per Methodenaufruf in strategy_spielstufe_auswählen zu nutzen.
"""
from settings import *
from strategy_button_display import*

class IDisplay_Hintergrund_Behavior:
    def display(self):
        raise NotImplementedError
class Hintergrund:
    def __init__(self, sha: IDisplay_Hintergrund_Behavior):
        self.auswählen = sha
    def hintergrund_anzeigen(self):
        self.auswählen.display(self)

#Hintergrund der Startseite
class Startseite_Optik(IDisplay_Hintergrund_Behavior):
    def display(self):
        #Hintergrund Farbe
        screen.fill(SLATEGRAY_3)
        #Überschrift: Schriftart, Größe und Position
        font = pygame.font.SysFont("comicsansms", 100)
        spieltitel = font.render("Dyonysos", True, (0, 0, 0))
        spieltitel_position = (400,40)
        screen.blit(spieltitel,spieltitel_position)
        #Hier der Text, für die Spielbeschreibung, leider funktioniert hier(font.render) Escape-Code \n für nächste Zeile nicht. Hier noch for-Schleife einbauen!
        font = pygame.font.SysFont("comicsansms", 30)
        spielbeschreibung_zeile1 = font.render("Der Weingott Dionysos lässt Bier vom Himmel regnen und bereitet Dir ein grandioses", True, (0, 0, 0))
        spielbeschreibung_position = (30,200)
        screen.blit(spielbeschreibung_zeile1,spielbeschreibung_position)
        spielbeschreibung_zeile2 = font.render("Fest. Sammle alle Biere und Schnäpse und werde zum ultimativen Bierkönig.", True, (0, 0, 0))
        spielbeschreibung_position = (30,240)
        screen.blit(spielbeschreibung_zeile2,spielbeschreibung_position)
        spielbeschreibung_zeile3 = font.render("Doch Achtung die Göttin Hera ist nicht zur Feier eingeladen und versucht Euer Fest", True, (0, 0, 0))
        spielbeschreibung_position = (30,280)
        screen.blit(spielbeschreibung_zeile3,spielbeschreibung_position)
        spielbeschreibung_zeile4 = font.render("zu verhindern indem Sie Wasser vom Himmel regnen lässt.", True, (0, 0, 0))
        spielbeschreibung_position = (30,320)
        screen.blit(spielbeschreibung_zeile4,spielbeschreibung_position)
        spielbeschreibung_zeile5 = font.render("In diesem Spiel geht es darum so viel Bier wie möglich einzusammeln bevor das Fest", True, (0, 0, 0))
        spielbeschreibung_position = (30,360)
        screen.blit(spielbeschreibung_zeile5,spielbeschreibung_position)
        spielbeschreibung_zeile6 = font.render("zu Ende ist. Hier können sich echte Helden in Ihrem Geschick beweisen.", True, (0, 0, 0))
        spielbeschreibung_position = (30,400)
        screen.blit(spielbeschreibung_zeile6,spielbeschreibung_position)
        #Hier Text für den Start-Button
        font = pygame.font.SysFont("comicsansms", 60)
        spielstart = font.render("Spiel starten", True, (0, 0, 0))
        spielstart_position = (400,600)
        screen.blit(spielstart,spielstart_position)
        einhorn = pygame.image.load("einhorn.png")
        screen.blit(einhorn,(200,480))
        pygame.display.update()

#Hintergrund_Namen_eingeben
class Namenseingabe_Hintergrund(IDisplay_Hintergrund_Behavior):
    def display(self):
        #Hintergrund Farbe
        screen.fill(SLATEGRAY_3)
        #Schrift
        font = pygame.font.SysFont("comicsansms", 35)
        text = font.render("Es wird nur Alkohol regnen, wenn Dionysos deinen Namen kennt !", True, (0, 0, 0))
        text_position = (90,80)
        screen.blit(text,text_position)
        font = pygame.font.SysFont("comicsansms", 60)
        spiel_weiter = font.render("Drücke weiter!", True, (0, 0, 0))
        spiel_weiter_position = (400,600)
        screen.blit(spiel_weiter,spiel_weiter_position)

#Hintergrund der Seite für die Heldenauswahl -> Zugriff auf die Bilder der Buttons aus Strategy_Button_display
class Startseite_Heldenauswahl_Optik(IDisplay_Hintergrund_Behavior):
    def display(self):
        screen.fill(SLATEGRAY_3)
        font = pygame.font.SysFont("comicsansms", 60)
        text = font.render("Wähle deinen Helden!", True, (0, 0, 0))
        text_position = (350,80)
        screen.blit(text,text_position)
        mariabutton.button_anzeigen()
        jackbutton.button_anzeigen()
        pygame.display.update()

#Hintergrund der Seite für die Levelauswahl -> Zugriff auf die Bilder der Buttons aus Strategy_Button_display
class Startseite_Levelauswahl_Optik(IDisplay_Hintergrund_Behavior):
    def display(self):
        screen.fill(SLATEGRAY_3)
        font = pygame.font.SysFont("comicsansms", 60)
        text = font.render("Wähle dein Level!", True, (0, 0, 0))
        text_position = (420,80)
        screen.blit(text,text_position)
        pennybutton.button_anzeigen()
        kneipebutton.button_anzeigen()
        bahnhofbutton.button_anzeigen()
        pygame.display.update()

#Hintergründe der einzelnen Level
class Penny_Optik(IDisplay_Hintergrund_Behavior):
    def display(self):
        penny = pygame.image.load("penny.jpg")        
        screen.blit(penny,position)
        pygame.display.update()
class Kneipe_Optik(IDisplay_Hintergrund_Behavior):
    def display(self):
        kneipe = pygame.image.load("kneipe.jpg")
        screen.blit(kneipe,position)
        pygame.display.update()
class Bahnhof_Optik(IDisplay_Hintergrund_Behavior):
    def display(self):
        bahnhof = pygame.image.load("bahnhof.jpg")
        screen.blit(bahnhof,position)
        pygame.display.update()

#Hintergrund Spielende
class Spielende_Hintergrund (IDisplay_Hintergrund_Behavior):
    def display(self):
        screen.fill(SLATEGRAY_3)
        nochmal_spielen_button.button_anzeigen()
        nicht_weiter_spielen.button_anzeigen()
        bart = pygame.image.load("bart.png")
        screen.blit(bart,(750,400))
        smile = pygame.image.load("drunk-emoji.png")
        screen.blit(smile,(1125,25))
        rick = pygame.image.load("rick.png")
        screen.blit(rick,(180,143))
        pygame.display.update()

#Hier Instanziierung
penny = Hintergrund(Penny_Optik)
kneipe = Hintergrund(Kneipe_Optik)
bahnhof = Hintergrund(Bahnhof_Optik)
startseite = Hintergrund (Startseite_Optik)
startseite_Levelauswahl = Hintergrund(Startseite_Levelauswahl_Optik)
startseite_Heldenauswahl = Hintergrund(Startseite_Heldenauswahl_Optik)
namenseingabe = Hintergrund(Namenseingabe_Hintergrund)
spielende = Hintergrund(Spielende_Hintergrund)

#penny.hintergrund_anzeigen()
#kneipe.hintergrund_anzeigen()
#bahnhof.hintergrund_anzeigen()
#startseite.hintergrund_anzeigen()
#startseite.hintergrund_anzeigen()
#startseite.hintergrund_anzeigen()
#namenseingabe.hintergrund_anzeigen()
#spielende.hintergrund_anzeigen()

