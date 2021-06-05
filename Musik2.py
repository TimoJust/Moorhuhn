import pygame
import sys
pygame.init()

pygame.mixer.init()
#pygame.mixer.music.load('Startmusik.ogg')
#pygame.mixer.music.play()

class Musik:
     def play():
         raise NotADirectoryError

class StartbildschirmMusik(Musik):
     def play(self):
         pygame.mixer.music.load('Startmusik.ogg')
         pygame.mixer.music.play()

class Level1Musik(Musik):
     def play(self):
         pygame.mixer.music.load('Level1.ogg')
         pygame.mixer.music.play()

class Level2Musik(Musik):
     def play(self):
         pygame.mixer.music.load('Level2.ogg')
         pygame.mixer.music.play()

class Level3Musik(Musik):
     def play(self):
         pygame.mixer.music.load('Level2.ogg')
         pygame.mixer.music.play()

class Hintergrundmusik(Musik):
     def play(self):
         pygame.mixer.music.load('hintergrundmusik.ogg')
         pygame.mixer.music.play()


class Ausgabe:
     def __init__(self, sp: Musik):
         self.abspielen = sp

     def spiele(self):
         self.abspielen.play()



# Zum importieren in die einzelnen Level

# Startbildschirm

meinMusikStartbildschirm = StartbildschirmMusik()
meineausgabe=Ausgabe(meinMusikStartbildschirm)
meinMusikStartbildschirm.play()

#level1

level1meinMusikStartbildschirm = Level1Musik()
level1meineausgabe=Ausgabe(level1meinMusikStartbildschirm)
level1meinMusikStartbildschirm.play()

#level2

level2meinMusikStartbildschirm = Level2Musik()
level2meineausgabe=Ausgabe(level1meinMusikStartbildschirm)
level2meinMusikStartbildschirm.play()

#level3

level3meinMusikStartbildschirm = Level3Musik()
level3meineausgabe=Ausgabe(level1meinMusikStartbildschirm)
level3meinMusikStartbildschirm.play()

# Endbildschirm/ Hintergrundmusik
hintergrundmusikmeinMusikStartbildschirm = Hintergrundmusik()
hintergrundmusikmeineausgabe=Ausgabe(hintergrundmusikmeinMusikStartbildschirm)
hintergrundmusikmeinMusikStartbildschirm.play()



clock = pygame.time.Clock()

#Farbe
black = (0,0,0)

#Fenster
width = 20
heigh = 20
size = (width, heigh)
win = pygame.display.set_mode(size)



# game loop

while True:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()



     pygame.display.flip()
     clock.tick(60)
