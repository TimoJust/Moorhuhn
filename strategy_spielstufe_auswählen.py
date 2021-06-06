"""
Autor: Timo Just
Strategy Pattern erstellt um die einzelnen Spielstufen/Ebenen zu erstellen, hier derzeit Startbildschirm,Namenseingabe, Heldenauswahl, Levelauswahl...
Dieses Pattern erstellt je nach Spielstufe das Verhalten, was passiert wenn auf Button X,Y gedrückt wird
Die Strategys werden dann in den Hauptteil übergeben. Es kann beliebig die Reihenfolgen oder grundsätzlich Spielstufe geändert werden. Jederzeit erweiterar und von außen aufrufbar.
"""
import pygame
import sys
import os
import random
import time
from factory import*
from settings import*
from hs import*
from pygame.locals import*
from strategy_hintergrund_display import*
from Musik2 import*

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
        meinMusikStartbildschirm.spiele()
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
        global spielername
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
                """
                Autor: Maurice Berger
                Nach der Levelauswahl wird das jeweilige Level gestartet...
                """
                player= spielername
                # Penny
                """
                Im Level Penny muss man möglichst viele Punkte in 60 Sekunden erreichen!
                Hierbei gibt es Bierdosen(+20Pkt) und Wasserflaschen(-20Pkt)
                Diese werden alle X Sekunden auf zufälliger Höhe und Seite in 3 verschiedenen Größen gespawnt
                Diese Sprites werden in der PennyFactory instanziert und erstellt
                Anschließend werden die Punkte angezeigt und die Top 3 Spieler des Penny-Highscore-Dictionaries ausgegegben
                -> Ende
                """
                pygame.mixer.music.stop()  
                if event.type == MOUSEBUTTONDOWN and button_level_1.collidepoint(event.pos):   
                    # Initialisierung Penny
                    # Initialisierung
                    pygame.init()
                    #Musik von Sven
                    level1meinMusikStartbildschirm.spiele()
                    
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))

                    pygame.display.set_caption("Dionysos")
                    clock = pygame.time.Clock()
                    pygame.time.set_timer(pygame.USEREVENT, 1000)
                    pygame.mouse.set_visible(False)
                    #
                    frame=0
                    frame_b=0
                    score_value=0
                    counter=0     
                    time_value=60

                    #Scorboard Funktion 
                    def scoreboard():
                        #Spielcockpit angezeigt
                        screen.blit(image_dict["score"], [0,HEIGHT-70])
                        scoreboard_score=font.render(str(score_value),True,WEISS)
                        #Punktestand : Score_Value          -> wird unten links angezeigt
                        screen.blit(scoreboard_score,[textX, textY])
                        scoreboard_anzeige_score=font.render("Punktestand:",True,WEISS,)
                        screen.blit(scoreboard_anzeige_score,[textX-240, textY])
                        #Zeit: Time_Value                   ->wird unten rechts angezeigt
                        scoreboard_anzeige_time=font.render("Zeit:",True,WEISS,)
                        screen.blit(scoreboard_anzeige_time,[timeX-150, timeY])
                        scoreboard_time=font.render(str(time_value),True,WEISS)
                        screen.blit(scoreboard_time,[timeX, timeY])
                    #Aktualisierung GameWindow
                    def redrawGameWindow():
                        #Hintergrund wird angezeigt    
                        screen.blit(bg3,(0,0))
                        scoreboard()
                    
                    #GameLoop Level Penny
                    running = True
                    #Anzeige Levelerklärung
                    draw_text('Penny-Level\n\nZiel:\nTrink so viel Alkohol wie möglich!\n\nZeit:  60 Sekunden\n\nBierdose =   +20 Punkte\n\nWasserflasche =   -200 Punkte')
                    time.sleep(5)
                    while running:
                        # Game Loop
                        clock.tick(FPS)

                        # Did the user click the window close button?
                        for event in pygame.event.get():
                            if event.type == pygame.USEREVENT: 
                                #Zeit läuft ab -1sek
                                time_value -= 1           
                                #PennyFactory nach x,y,... sek 10 mal starten
                                if time_value ==7 or time_value ==35 or time_value ==25 or time_value ==59 or time_value ==55 or time_value ==60 or time_value ==50 or time_value ==40 or time_value ==30 or time_value ==20 or time_value ==10: 
                                    #X Factory für _ mal starten
                                    for _ in range(1, 10):
                                        Client(PennyFactory())
                                #Wenn Zeit <1 Spielende mit Highscore Übertragung und Anzeige-> Spielabbruch
                                if time_value<1:
                                    draw_text("Das war´s " +player+"\n\n "+str(score_value)+" Punkte erreicht!")
                                    time.sleep(1)
                                    highscore_pennyHinzufügen(player,score_value)
                                    hs_pennyEintragen(p, top_n=3)
                                    highscore_pennyAnzeigen()
                                    time.sleep(1)
                                    running= False
                            if event.type == pygame.QUIT:
                                running = False

                        # Update
                        for sprite in sprite_list:
                            #solange Sprite im Fenster ist -> Update
                            if sprite.x >= -30 and sprite.x <= WIDTH+30:
                                sprite.update()
                            else:
                                print("Sprite entfernt")
                                #ansonsten Sprite entfernen
                                sprite_list.remove(sprite)
                                #Und neuen Sprite Spawnen
                                Client(PennyFactory())

                        # Rendern
                        redrawGameWindow()
                        
                        #Sprites Rendern
                        for sprite in sprite_list:
                            sprite.render(screen)

                        #Hand Rendern
                        x,y=pygame.mouse.get_pos()
                        screen.blit(hand[0],(x-20,y-20))

                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            #Geschlossene_Hand Rendern
                            screen.blit(hand[1],(x-20,y-20))
                            for sprite in sprite_list:
                                #Wenn Sprite getroffen +- Punkte zum Score zählen und Sprite entfernen
                                if sprite.getraenk_rect.collidepoint(event.pos):  #event.pos = Maus Position beim klick
                                    print("Treffer")                              
                                    if type(sprite)==Bierdose or type(sprite)==Bierflasche or type(sprite)==Bier:
                                        score_value+=20
                                    if type(sprite)==Limo or type(sprite)==Cafe or type(sprite)==Wasserflasche:
                                        score_value-=200
                                    sprite_list.remove(sprite)
                            frame = 0
                        # Display
                        pygame.display.flip()
                    pygame.mixer.music.stop()
                # Bahnhof
                """
                Im Level Bahnhof muss man möglichst viele Punkte sammeln!
                Man spielt gegen die Zeit
                Hierbei gibt es Bierflaschen(+1sek/+20Pkt) und Limo(-5sek.)
                Diese werden alle X Sekunden auf zufälliger Höhe und Seite in 3 verschiedenen Größen gespawnt
                Diese Sprites werden in der BahnhofFactory instanziert und erstellt
                Anschließend werden die Punkte angezeigt und die Top 3 Spieler des Bahnhof-Highscore-Dictionaries ausgegegben
                -> Ende
                """
                if event.type == MOUSEBUTTONDOWN and button_level_2.collidepoint(event.pos):
                    # Initialisierung Bahnhof
                    # Initialisierung
                    pygame.init()

                     #Musik von Sven
                    level2meinMusikStartbildschirm.spiele()

                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    pygame.display.set_caption("Dionysos - Bahnhof")
                    clock = pygame.time.Clock()
                    pygame.time.set_timer(pygame.USEREVENT, 1000)
                    pygame.mouse.set_visible(False)
                    #
                    counter=0
                    time_value=14
                    score_value=0
                    #Scorboard Funktion 
                    def scoreboard():
                        screen.blit(image_dict["scorebhf"], [0,HEIGHT-70])
                        scoreboard_score=font.render(str(score_value),True,WEISS)
                        screen.blit(scoreboard_score,[textX, textY])
                        scoreboard_anzeige_score=font.render("Punktestand:",True,WEISS,)
                        screen.blit(scoreboard_anzeige_score,[textX-240, textY])
                        scoreboard_anzeige_time=font.render("Zeit:",True,WEISS,)
                        screen.blit(scoreboard_anzeige_time,[timeX-150, timeY])
                        scoreboard_time=font.render(str(time_value),True,WEISS)
                        screen.blit(scoreboard_time,[timeX, timeY])
                        
                    #Aktualisierung GameWindow
                    def redrawGameWindow():    
                        screen.blit(bg1,(0,0))
                        scoreboard()
                    draw_text('Bahnhof-Level\n\nZiel: Betrinke dich so lange wie möglich um den Highscore zu erreichen!\n\n\n\nBierflasche= + 1 sek.\n                     +20Punkte\n\nLimo = -5 sek.')
                    time.sleep(4)
                    running = True
                    while running:
                        # Game Loop
                        clock.tick(FPS)

                        # Did the user click the window close button?
                        for event in pygame.event.get():
                            if event.type == pygame.USEREVENT: 
                                time_value -= 1           
                                #Factory nach x sek starten
                                if counter==0:
                                    for _ in range(1, 7):
                                        Client(BahnnhofFactory())
                                    counter=5
                                counter-=1
                                if time_value<1:
                                    draw_text("Das war´s " +player+"\n\n "+str(score_value)+" Punkte erreicht!")
                                    time.sleep(1)
                                    highscore_bhfHinzufügen(player,score_value)
                                    hs_bhfEintragen(b, top_n=3)
                                    highscore_bhfAnzeigen()
                                    time.sleep(1)
                                    running= False
                            if event.type == pygame.QUIT:
                                running = False
                    

                        # Update
                        for sprite in sprite_list:
                            #solange Sprite im Fenster ist -> Update
                            if sprite.x >= -30 and sprite.x <= WIDTH+30:
                                sprite.update()
                            else:
                                print("Sprite entfernt")
                                #ansonsten Sprite entfernen
                                sprite_list.remove(sprite)
                                Client(BahnnhofFactory())

                        # Rendern
                        redrawGameWindow()
                
                        #Sprites Rendern
                        for sprite in sprite_list:
                            sprite.render(screen)
                        #Hand Rendern
                        x,y=pygame.mouse.get_pos()
                        screen.blit(hand[0],(x-20,y-20))

                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            #Geschlossene_Hand Rendern
                            screen.blit(hand[1],(x-20,y-20))
                            for sprite in sprite_list:
                                if sprite.getraenk_rect.collidepoint(event.pos):  #event.pos = Maus Position beim klick
                                    print("Treffer")
                                           
                                    if type(sprite)==Bierflasche:
                                        time_value+=1
                                        score_value+=20
                                    if type(sprite)==Limo:
                                        time_value-=5
                                    sprite_list.remove(sprite)
                        # Display
                        pygame.display.flip()
                    pygame.mixer.music.stop()
                    
                #Kneipe
                """
                Im Level Kneipe muss man sich möglichst schnell betrinken!
                Die zeit wird gestoppt
                Hierbei gibt es Bier(+Betrunkenheit), Jägermeister(+++Betrunkenheit)  und Cafe(-Betrunkenheit)
                Diese werden alle X Sekunden auf zufälliger Höhe und Seite in 3 verschiedenen Größen gespawnt
                Diese Sprites werden in der KneipeFactory instanziert und erstellt
                Anschließend die Zeit angezeigt und die Top 3 schnellsten Spieler des Kneipe-Highscore-Dictionaries ausgegegben
                -> Ende
                """
                if event.type == MOUSEBUTTONDOWN and button_level_3.collidepoint(event.pos):
                    # Initialisierung
                    pygame.init()
                    
                     #Musik von Sven
                    level3meinMusikStartbildschirm.spiele()

                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    pygame.display.set_caption("Dionysos")
                    clock = pygame.time.Clock()
                    pygame.time.set_timer(pygame.USEREVENT, 1000)
                    pygame.mouse.set_visible(False)
                    #
                    frame=0
                    frame_b=0
                    score_value=794
                    counter=0
                    time_value=-7
                    health_bar_width=1
                    def Leberwert(surface,x,y,value,maxvalue):
                        xx=16
                        for hp in range(value):
                            pygame.draw.rect(surface, SCHWARZ, (x+xx,y,100,24), 0)
                            xx+= int(max(min(value / float(maxvalue) * health_bar_width, health_bar_width), 0))



                    #Scorboard Funktion 
                    def scoreboard():
                        screen.blit(image_dict["scorekneipe"], [0, HEIGHT-70])
                        scoreboard_anzeige_time=font.render("Zeit:",True,WEISS,)
                        screen.blit(scoreboard_anzeige_time,[timeX-150, timeY])
                        scoreboard_time=font.render(str(time_value),True,WEISS)
                        screen.blit(scoreboard_time,[timeX, timeY])

                    #Aktualisierung GameWindow
                    def redrawGameWindow():    
                        screen.blit(bg,(0,0))
                        scoreboard()
                        Leberwert(screen,0,HEIGHT-46,score_value,1)

                    draw_text('Kneipe-Level\n\nZiel: Betrinke dich so schnell wie möglich!\n\n-> Bekämpfe deine Nüchternheit und ertränke den Balken in Alkohol\n\n\n\nBier= Wirksamkeit +\n\nJägermeister= Wirksamkeit +++\n\nCafe= Wirksamkeit -')
                    time.sleep(5)                    
                    running = True
                    while running:
                        # Game Loop
                        clock.tick(FPS)

                        # Did the user click the window close button?
                        for event in pygame.event.get():
                            if event.type == pygame.USEREVENT: 
                                time_value += 1           
                                #Factory nach x sek starten
                                if counter==0:
                                    for _ in range(1, 7):
                                        Client(KneipeFactory())
                                    counter=5
                                counter-=1
                                if score_value<0:
                                    draw_text("Das war´s " +player+"\n\nDu hast "+str(time_value)+" Sekunden Gebraucht um dich zu betrinken!\n\n\n\nHerzlichen Glückwunsch! ")
                                    time.sleep(1)
                                    highscore_kneipeHinzufügen(player,time_value)
                                    hs_kneipeEintragen(k, top_n=3)
                                    highscore_kneipeAnzeigen()
                                    time.sleep(1)
                                    running= False
                            if event.type == pygame.QUIT:
                                running = False
                    

                        # Update
                        for sprite in sprite_list:
                            #solange Sprite im Fenster ist -> Update
                            if sprite.x >= -30 and sprite.x <= WIDTH+30:
                                sprite.update()
                            else:
                                print("Sprite entfernt")
                                #ansonsten Sprite entfernen
                                sprite_list.remove(sprite)
                                Client(KneipeFactory())

                        # Rendern
                        redrawGameWindow()
                        #scoreboard()
                        #kneipe.hintergrund_anzeigen()
                        #Sprites Rendern
                        for sprite in sprite_list:
                            sprite.render(screen)
                        #Hand Rendern
                        x,y=pygame.mouse.get_pos()
                        screen.blit(hand[0],(x-20,y-20))

                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            #Geschlossene_Hand Rendern
                            screen.blit(hand[1],(x-20,y-20))
                            for sprite in sprite_list:
                                if sprite.getraenk_rect.collidepoint(event.pos):  #event.pos = Maus Position beim klick
                                    print("Treffer")
                                
                                
                                    if type(sprite)==Bierdose or type(sprite)==Bierflasche or type(sprite)==Bier:
                                        score_value-=20
                                    if type(sprite)==Limo or type(sprite)==Cafe or type(sprite)==Wasserflasche:
                                        score_value+=20
                                    if type(sprite)==Jaegermeister:
                                        score_value-=50
                                    sprite_list.remove(sprite)
                            frame = 0
                        # Display
                        pygame.display.flip()
                    pygame.mixer.music.stop()

#Spielendbildschirm
class Spielende(ISpielstufe_Behavior):
    def ausführen(self):
        pygame.mouse.set_visible(True)
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
