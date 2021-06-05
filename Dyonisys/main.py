import pygame
import os
import random
import time
from factorymethotpattern import *



# Settings
WEISS=(255,255,255)
WIDTH = 1250
HEIGHT = 938
FPS = 60
sprite_list = [] 
liste_spawn =[80,70,60,50,40,30,20,10]

# Initialisierung
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mooralk")
clock = pygame.time.Clock()



#Score 
pygame.time.set_timer(pygame.USEREVENT, 1000)
score_value=0
time_value=90
font =pygame.font.SysFont(None, 50)
textX=50
textY=50
timeX=WIDTH-50
timeY=50

# Hier Grafiken einbinden
game_folder = os.path.dirname(__file__)
image_dict = {}
#handListe = [pygame.image.load(os.path.join(game_folder, "handauf.png")),pygame.image.load(os.path.join(game_folder, "handzu.png"))]
image_dict["bier"] = pygame.image.load(os.path.join(game_folder, "biercartoon.png"))
image_dict["radler"] = pygame.image.load(os.path.join(game_folder, "jaegermeister.png"))
image_dict["cola"] = pygame.image.load(os.path.join(game_folder, "cafe.png"))
image_dict["wasserflasche"]= pygame.image.load(os.path.join(game_folder, "wasserflasche.png"))
image_dict["bierdose"]= pygame.image.load(os.path.join(game_folder, "bierdose.png"))
image_dict["handauf"]= pygame.image.load(os.path.join(game_folder, "handauf.png"))
bg=pygame.image.load("hintergrund2.jpg")
#skalierung der Bilder
bier = image_dict["bier"]
bier_klein = pygame.transform.scale(bier, (75,75))
bier_gross = pygame.transform.scale(bier, (100,100))
radler = image_dict["radler"]
radler_klein = pygame.transform.scale(radler, (75,75))
radler_gross = pygame.transform.scale(radler, (100,100))
cola = image_dict["cola"]
cola_klein = pygame.transform.scale(cola, (75,75))
cola_gross = pygame.transform.scale(cola, (100,100))
wasserflasche = image_dict["wasserflasche"]
wasserflasche_klein = pygame.transform.scale(wasserflasche, (50,50))
wasserflasche_gross = pygame.transform.scale(wasserflasche, (75,75))
bierdose = image_dict["bierdose"]
bierdose_klein = pygame.transform.scale(bierdose, (50,50))
bierdose_gross = pygame.transform.scale(bierdose, (75,75))

#Scorboard Funktion 
def scoreboard():
    scoreboard_score=font.render(str(score_value),True,WEISS)
    screen.blit(scoreboard_score,[textX, textY])
    scoreboard_time=font.render(str(time_value),True,WEISS)
    screen.blit(scoreboard_time,[timeX, timeY])

def randomzahl(self,anzahl):
    self.randomzahl=random.randint(1,anzahl)
    return self.randomzahl

def redrawGameWindow():    
    screen.blit(bg,(0,0))
    scoreboard()
    

running = True
#start_ticks=pygame.time.get_ticks() #starter tic
while running:
    # Game Loop
    clock.tick(FPS)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT: 
            time_value -= 1
            if time_value ==88: 
                #Random Factory für X mal starten
                #for i in range(1, 10):
                #    factory=fmp.Client()
                #    factory.main()
            #    factory=Client()
             #   factory.play()
                pass
        if event.type == pygame.QUIT:
            running = False
   

    # Update
    for sprite in sprite_list:
        #solange Sprite im Fenster ist -> Update
        if sprite.x >= -30 and sprite.x <= WIDTH+30:
            sprite.update()
        else:
            #ansonsten Sprite entfernen
            sprite_list.remove(sprite)
            #Score +
            score_value+=1
            #neuen Sprite erzeugen
            factory=Client()
            factory.play()

    # Rendern
    redrawGameWindow()
    #Sprites Rendern
    for sprite in sprite_list:
        sprite.render(screen)
    #Hand Rendern
    x,y=pygame.mouse.get_pos()
    screen.blit(image_dict["handauf"],(x-80,y-80))
    # Display
    pygame.display.flip()
pygame.quit()
