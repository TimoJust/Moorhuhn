""" Importanweisungen damit Musik gespielt werden kann 
    Autor: Sven Radzabov 
"""

import pygame
import sys
pygame.init()

# sound
pygame.mixer.init()
pygame.mixer.music.load('Startmusik.ogg')
pygame.mixer.music.play()

# Zum Testen der Ausgabe



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










