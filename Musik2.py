""" 
Klasse von zum Abspielen von Musik in den einzelnen Leveln.
Autor: Sven Radzabov

Idee: Anwendung vom Strategy Pattern.
Unterschiedliche Implementierung der Methode play in jedem Level mit eigener Lautstärke 
und einem eigenen Lied.

 Formate müssen vom Typ "ogg" sein. 

"""

# Importe notwendiger Bibliotheken 
import pygame
import sys
pygame.init()

pygame.mixer.init()

#zum Test ob Lieder abgespielt werden können
#pygame.mixer.music.load('Startmusik.ogg')
#pygame.mixer.music.play()

# Interface: Jede Klasse die vom Interface erbt muss play() implementieren
class Musik:
     def play(self):
         raise NotADirectoryError
     
# Musik für den Startbildschirm 
class StartbildschirmMusik(Musik):
     def play(self):
         pygame.mixer.music.load('Startmusik.ogg') 
         pygame.mixer.music.play()
         pygame.mixer.music.set_volume(0.4)

# Musik für Level1
class Level1Musik(Musik):
     def play(self):
         pygame.mixer.music.load('Level1.ogg')
         pygame.mixer.music.play()
         pygame.mixer.music.set_volume(0.1)
     
# Musik für Level2
class Level2Musik(Musik):
     def play(self):
         pygame.mixer.music.load('Level2.ogg')
         pygame.mixer.music.play()
         pygame.mixer.music.set_volume(0.1)

# Musik für Level3
class Level3Musik(Musik):
     def play(self):
         pygame.mixer.music.load('Level2.ogg')
         pygame.mixer.music.play()
         pygame.mixer.music.set_volume(0.1)

# Musik für Level3
class Hintergrundmusik(Musik):
     def play(self):
         pygame.mixer.music.load('hintergrundmusik.ogg')
         pygame.mixer.music.play()
         pygame.mixer.music.set_volume(0.4)

# Initialisierung
class Ausgabe:
     def __init__(self, sp: Musik):
         self.abspielen = sp

     def spiele(self):
         self.abspielen.play(self)



# Zum importieren in die einzelnen Level

# Startbildschirm

meinMusikStartbildschirm = Ausgabe(StartbildschirmMusik)
#meinMusikStartbildschirm.spiele()


#level1

level1meinMusikStartbildschirm = Ausgabe(Level1Musik)
#level1meinMusikStartbildschirm.spiele()

#level2

level2meinMusikStartbildschirm = Ausgabe(Level2Musik)
#level2meinMusikStartbildschirm.spiele()

#level3

level3meinMusikStartbildschirm = Ausgabe(Level3Musik)
#level3meinMusikStartbildschirm.spiele()

# Endbildschirm/ Hintergrundmusik
hintergrundmusikmeinMusikStartbildschirm = Ausgabe(Hintergrundmusik)
#hintergrundmusikmeinMusikStartbildschirm.spiele()


clock = pygame.time.Clock()

""" Zum Testen der Klasse vor dem Zusammenführen """

#Farbe
#black = (0,0,0)

#Fenster
#width = 20
#heigh = 20
#size = (width, heigh)
#win = pygame.display.set_mode(size)



# game loop

#while True:
     #for event in pygame.event.get():
         #if event.type == pygame.QUIT:
             #pygame.quit()
             #sys.exit()



     #pygame.display.flip()
#clock.tick(60)
