import pygame
import os
import random
import time
from pygame.constants import MOUSEBUTTONDOWN

# Settings
WEISS=(255,255,255)
WIDTH = 1250
HEIGHT = 938
FPS = 60
sprite_list = [] 

# Initialisierung
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mooralk")
clock = pygame.time.Clock()

#Score 
score_value=0
time_value=90
font =pygame.font.SysFont(None, 50)
textX=50
textY=50
timeX=WIDTH-50
timeY=50


#Remaining Tries display init
remainingTriesCount_value = 5
remainingTriesCountX = WIDTH - (WIDTH/2 - 110)
remainingTriesCountY = 52
remainingTriesText_value = 'Anzahl Öffner:'
remainingTriesTextX = WIDTH - (WIDTH/2 + 150)
remainingTriesTextY = 50



# Hier Grafiken einbinden
game_folder = os.path.dirname(__file__)


#Sounds einbinden
flensburger_beer_plop = pygame.mixer.Sound(os.path.join(game_folder, "Flensburger_Plop.wav"))
water_sound = pygame.mixer.Sound(os.path.join(game_folder, "Wasser_zischen.wav"))



image_dict = {}
#handListe = [pygame.image.load(os.path.join(game_folder, "handauf.png")),pygame.image.load(os.path.join(game_folder, "handzu.png"))]
image_dict["bier"] = pygame.image.load(os.path.join(game_folder, "bier.png"))
image_dict["radler"] = pygame.image.load(os.path.join(game_folder, "beer1.gif"))
image_dict["cola"] = pygame.image.load(os.path.join(game_folder, "cola.png"))
image_dict["handauf"]= pygame.image.load(os.path.join(game_folder, "handauf.png"))
bg=pygame.image.load(os.path.join(game_folder, "hintergrund2.jpg"))
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

#Scoreboard Funktion 
def scoreboard():
    scoreboard_score=font.render(str(score_value),True,WEISS)
    screen.blit(scoreboard_score,[textX, textY])
    scoreboard_time=font.render(str(time_value),True,WEISS)
    screen.blit(scoreboard_time,[timeX, timeY])



#Remaining Tries display
def remainingTries():
    remainingTries_count=font.render(str(remainingTriesCount_value),True,WEISS)
    screen.blit(remainingTries_count,[remainingTriesCountX, remainingTriesCountY])
    remainingTries_text=font.render(str(remainingTriesText_value),True,WEISS)
    screen.blit(remainingTries_text,[remainingTriesTextX, remainingTriesTextY])


def redrawGameWindow():    
    screen.blit(bg,(0,0))
    scoreboard()
    remainingTries()
    

#Creator
class IGetraenkCreator:
    def holeGetraenk(self):
        #Delegation der Objekterstellung an Subklasse 
        var = RandomGetraenkeFactory()
        self.getraenk = var.createGetraenk() 
        #weitere verarbeitung 
        #self.getraenk.einpacken() 
        #self.getraenk.etikettieren()
        return self.getraenk

    #Definition der Factory Method 
    def createGetraenk(self):
        raise NotImplementedError
#Concrete Creator
class RandomGetraenkeFactory (IGetraenkCreator):    
    def createGetraenk(self):
            randomseite=random.randint(1,2)
            randomgetraenk=random.randint(1,3)
            randomgroesse=random.randint(1,3)
            if randomgroesse==1:
                if randomseite==1:
                    if randomgetraenk==1:
                        bier=Bier(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), bier_klein)
                        sprite_list.append(bier)
                        return Bier(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), bier_klein)
                    if randomgetraenk==2:
                        cola= Cola(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), cola_klein)
                        sprite_list.append(cola)
                        return Cola(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), cola_klein)
                    if randomgetraenk==3:
                        radler= Radler(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), radler_klein)
                        sprite_list.append(radler)
                        return Radler(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), radler_klein)          
                if randomseite==2:
                    if randomgetraenk==1:
                        bier=Bier(WIDTH-50, random.randint(20, HEIGHT-50), random.randint(3,7)* -1, random.randint(3, 7)* -1, bier_klein)
                        sprite_list.append(bier)
                        return Bier(WIDTH-50, random.randint(20, HEIGHT-50), random.randint(3,7)* -1, random.randint(3, 7)* -1, bier_klein)
                    if randomgetraenk==2:
                        cola= Cola(WIDTH-50, random.randint(20, HEIGHT-50), random.randint(3,7)* -1, random.randint(3, 7)* -1, cola_klein)
                        sprite_list.append(cola)
                        return Cola(WIDTH-50, random.randint(20, HEIGHT-50), random.randint(3,7)* -1, random.randint(3, 7)* -1, cola_klein)
                    if randomgetraenk==3:
                        radler= Radler(WIDTH-50, random.randint(20, HEIGHT-50), random.randint(3,7)* -1, random.randint(3, 7)* -1, radler_klein)
                        sprite_list.append(radler)
                        return Radler(WIDTH-50, random.randint(20, HEIGHT-50), random.randint(3,7)* -1, random.randint(3, 7)* -1, radler_klein)
            if randomgroesse==2:
                if randomseite==1:
                    if randomgetraenk==1:
                        bier=Bier(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), bier_gross)
                        sprite_list.append(bier)
                        return Bier(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), bier_gross)
                    if randomgetraenk==2:
                        cola= Cola(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), cola_gross)
                        sprite_list.append(cola)
                        return Cola(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), cola_gross)
                    if randomgetraenk==3:
                        radler= Radler(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), radler_gross)
                        sprite_list.append(radler)
                        return Radler(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), radler_gross)          
                if randomseite==2:
                    if randomgetraenk==1:
                        bier=Bier(WIDTH-50, random.randint(20, HEIGHT-50), random.randint(3,7)* -1, random.randint(3, 7)* -1, bier_gross)
                        sprite_list.append(bier)
                        return Bier(WIDTH-50, random.randint(20, HEIGHT-50), random.randint(3,7)* -1, random.randint(3, 7)* -1, bier_gross)
                    if randomgetraenk==2:
                        cola= Cola(WIDTH-50, random.randint(20, HEIGHT-50), random.randint(3,7)* -1, random.randint(3, 7)* -1, cola_gross)
                        sprite_list.append(cola)
                        return Cola(WIDTH-50, random.randint(20, HEIGHT-50), random.randint(3,7)* -1, random.randint(3, 7)* -1, cola_gross)
                    if randomgetraenk==3:
                        radler= Radler(WIDTH-50, random.randint(20, HEIGHT-50), random.randint(3,7)* -1, random.randint(3, 7)* -1, radler_gross)
                        sprite_list.append(radler)
                        return Radler(WIDTH-50, random.randint(20, HEIGHT-50), random.randint(3,7)* -1, random.randint(3, 7)* -1, radler_gross)
            if randomgroesse==3:
                if randomseite==1:
                    if randomgetraenk==1:
                        bier=Bier(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), image_dict["bier"])
                        sprite_list.append(bier)
                        return Bier(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), image_dict["bier"])
                    if randomgetraenk==2:
                        cola= Cola(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), image_dict["cola"])
                        sprite_list.append(cola)
                        return Cola(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), image_dict["cola"])
                    if randomgetraenk==3:
                        radler= Radler(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), image_dict["radler"])
                        sprite_list.append(radler)
                        return Radler(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), image_dict["radler"])          
                if randomseite==2:
                    if randomgetraenk==1:
                        bier=Bier(WIDTH-50, random.randint(20, HEIGHT-50), random.randint(3,7)* -1, random.randint(3, 7)* -1, image_dict["bier"])
                        sprite_list.append(bier)
                        return Bier(WIDTH-50, random.randint(20, HEIGHT-50), random.randint(3,7)* -1, random.randint(3, 7)* -1, image_dict["bier"])
                    if randomgetraenk==2:
                        cola= Cola(WIDTH-50, random.randint(20, HEIGHT-50), random.randint(3,7)* -1, random.randint(3, 7)* -1, image_dict["cola"])
                        sprite_list.append(cola)
                        return Cola(WIDTH-50, random.randint(20, HEIGHT-50), random.randint(3,7)* -1, random.randint(3, 7)* -1, image_dict["cola"])
                    if randomgetraenk==3:
                        radler= Radler(WIDTH-50, random.randint(20, HEIGHT-50), random.randint(3,7)* -1, random.randint(3, 7)* -1, image_dict["radler"])
                        sprite_list.append(radler)
                        return Radler(WIDTH-50, random.randint(20, HEIGHT-50), random.randint(3,7)* -1, random.randint(3, 7)* -1, image_dict["radler"])
#Product
class Getraenk(): 

    def __init__(self, x, y, sx, sy, image):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.image = image
        self.getraenk_rect = image.get_rect()
    
    def update(self):
        # Bewegung
        self.x = self.x + self.sx
        self.y = self.y #self.y + self.sy# -> So nur horizontale bewegung
        self.getraenk_rect.topleft = (self.x, self.y)
        #respawn -> im Gameloop
        #if self.getraenk_rect.right == WIDTH or self.getraenk_rect.left == 0:
            #factory=Client()
            #factory.main()

    def render(self, screen):
        screen.blit(self.image, self.getraenk_rect)


#Concrete Product A
class Bier (Getraenk): 
    def starten(self):
        pass

#Concrete Product B
class Radler (Getraenk):
    def starten(self):
        pass

#Concrete Product C
class Cola (Getraenk):
    def starten(self):
        pass

#client Random Sprite Factory
class Client:
    def main(self): 
        random = RandomGetraenkeFactory() 
        randomGetraenkSpawn = random.holeGetraenk() 
        randomGetraenkSpawn.starten()#"RandomFactory startet startet" 
        

#Random Factory für X mal starten
#for i in range(1, 7):
#    factory=Client()
#    factory.main()
      




running = True
start_ticks=pygame.time.get_ticks() #starter tic
while running:
    # Game Loop
    clock.tick(FPS)
    

    seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
    #print(round(seconds,2)) #Auskommentiert, damit sekunden nicht mehr im terminal erscheinen
    if seconds>10: # if more than 10 seconds close the game
        pass

    
    #wiederholter Spawn
    last_spawn_time = pygame.time.get_ticks()
    #if last_spawn_time< 720 or last_spawn_time < 5030 and last_spawn_time > 4970 or  last_spawn_time < 10030 and last_spawn_time > 9970 or  last_spawn_time < 20030 and last_spawn_time > 19970:
    #Spawn nach 1, 10 und 20 Sekunden
    if round(seconds,1)==1 or round(seconds,1)==10 or round(seconds,1)==20 or round(seconds,1)==30:
        #for i in range(1, 10):
        factory=Client()
        factory.main()
        

    # Did the user click the window close button?
    for event in pygame.event.get():
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
            #score_value+=1
            #neuen Sprite erzeugen
            factory=Client()
            factory.main()

    # Rendern
    redrawGameWindow()
    #Sprites Rendern
    for sprite in sprite_list:
        sprite.render(screen)


    #Hand Rendern
    x,y=pygame.mouse.get_pos()

    screen.blit(image_dict["handauf"],(x-80,y-80))
   


    #Prüfen auf Kollision 
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        for sprite in sprite_list:
         if sprite.getraenk_rect.collidepoint(event.pos):  #event.pos = Maus Position beim klick
            print("Treffer")
            score_value +=5
            remainingTriesCount_value -=1
            #pygame.mixer.music.play(0)
            if type(sprite) == Bier:
                flensburger_beer_plop.play()
            elif type(sprite) == Cola: 
                water_sound.play()
            print(sprite)
            sprite_list.remove(sprite)
            if remainingTriesCount_value == 0:
                print("Öffner verbraucht bitte nachladen")        
                

    # Display
    pygame.display.flip()
pygame.quit()


#todo:
#Anzeige anzahl öffner 
#wenn anzahl 0 dann geht nichts mehr nur noch nachladen
#verschiedene sounds bei verschiedenen getränken
