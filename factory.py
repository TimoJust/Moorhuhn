import pygame
import os
import random
import time
from settings import *

#SpriteListe
sprite_list = [] 


# Hier Grafiken einbinden
game_folder = os.path.dirname(__file__)
image_dict = {}
hand = ['','']
hand[0] = pygame.image.load("handauf1.png")
hand[1] = pygame.image.load("handzu1.png")
#handListe = [pygame.image.load(os.path.join(game_folder, "handauf.png")),pygame.image.load(os.path.join(game_folder, "handzu.png"))]
image_dict["bier"] = pygame.image.load(os.path.join(game_folder, "biercartoon.png"))
image_dict["jaegermeister"] = pygame.image.load(os.path.join(game_folder, "jaegermeister.png"))
image_dict["wasserflasche"]= pygame.image.load(os.path.join(game_folder, "wasserflasche.png"))
image_dict["bierdose"]= pygame.image.load(os.path.join(game_folder, "bierdose.png"))
image_dict["limo"]= pygame.image.load(os.path.join(game_folder, "limo.png"))
image_dict["cafe"]= pygame.image.load(os.path.join(game_folder, "cafe.png"))
image_dict["bierflasche"]= pygame.image.load(os.path.join(game_folder, "bierflasche.png"))
image_dict["handauf"]= pygame.image.load(os.path.join(game_folder, "hand2.png"))
image_dict["score"]= pygame.image.load(os.path.join(game_folder, "score.png"))

bg=pygame.image.load("hintergrund2.jpg")
#skalierung der Bilder
bier = image_dict["bier"]
bier_klein = pygame.transform.scale(bier, (75,75))
bier_gross = pygame.transform.scale(bier, (100,100))
wasserflasche = image_dict["wasserflasche"]
wasserflasche_klein = pygame.transform.scale(wasserflasche, (75,75))
wasserflasche_gross = pygame.transform.scale(wasserflasche, (100,100))
bierdose = image_dict["bierdose"]
bierdose_klein = pygame.transform.scale(bierdose, (75,75))
bierdose_gross = pygame.transform.scale(bierdose, (100,100))
jaegermeister_klein = image_dict["jaegermeister"]
jaegermeister_klein= pygame.transform.scale(jaegermeister_klein, (50,50))
bierflasche_klein = image_dict["bierflasche"]
bierflasche_klein= pygame.transform.scale(bierflasche_klein, (90,90))
cafe_klein = image_dict["cafe"]
cafe_klein= pygame.transform.scale(cafe_klein, (100,100))




skalierung      = 0 
skalierungswert = 1




#Product
class Getraenk:
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
        self.y = self.y#self.y + self.sy# -> So nur horizontale bewegung
        self.getraenk_rect.center = (self.x, self.y)


    def render(self, screen):
        screen.blit(self.image, self.getraenk_rect)

    def starten(self):
        raise NotImplementedError
                

#Product A
class Bierdose(Getraenk):
    def starten(self):
        print("Bierdose Startet")
#Product B
class Wasserflasche(Getraenk):
    def starten(self):
        print("Wasserflasche Startet")
#Product C
class Bier(Getraenk):
    def starten(self):
        print("Bierflasche Startet")
#Product D
class Cafe(Getraenk):
    def starten(self):
        print("Cafe Startet")
#Product E
class Jaegermeister(Getraenk):
    def starten(self):
        print("Jaegermeister Startet")
#Product F
class Bierflasche(Getraenk):
    def starten(self):
        print("Bierflasche Startet")
#Product G
class Limo(Getraenk):
    def starten(self):
        print("Limo Startet")

# Creator
class IGetraenkFactory:
    def makeGetraenk(self): 
        raise NotImplementedError

# Concrete Creator A
#Level Kneipe Factory -> Randomgrößen  /  Randomseite  / 2Getränke  /  Verteilung  1/5_Wasserflaschen 4/5_Bierdose
class PennyFactory(IGetraenkFactory):
    def makeGetraenk(self): 
        randomseite=random.randint(1,2)
        randomgetraenk=random.randint(1,5)
        randomgroesse=random.randint(1,3)
        if randomgroesse==1:
            if randomseite==1:
                if randomgetraenk==1 or randomgetraenk==3 or randomgetraenk==4 or randomgetraenk==5:
                    bierdose=Bierdose(0, random.randint(50, HEIGHT-100), random.randint(3,7), random.randint(3, 7), bierdose_klein)
                    sprite_list.append(bierdose)
                    return Bierdose(0, random.randint(50, HEIGHT-100), random.randint(3,7), random.randint(3, 7), bierdose_klein)
                if randomgetraenk==2:
                    wasserflasche= Wasserflasche(0, random.randint(50, HEIGHT-100), random.randint(3,7), random.randint(3, 7), wasserflasche_klein)
                    sprite_list.append(wasserflasche)
                    return Wasserflasche(0, random.randint(50, HEIGHT-100), random.randint(3,7), random.randint(3, 7), wasserflasche_klein)       
            if randomseite==2:
                if randomgetraenk==1 or randomgetraenk==3 or randomgetraenk==4 or randomgetraenk==5:
                    bierdose=Bierdose(WIDTH-50, random.randint(50, HEIGHT-100), random.randint(3,7)* -1, random.randint(3, 7)* -1, bierdose_klein)
                    sprite_list.append(bierdose)
                    return Bierdose(WIDTH-50, random.randint(50, HEIGHT-100), random.randint(3,7)* -1, random.randint(3, 7)* -1, bierdose_klein)
                if randomgetraenk==2:
                    wasserflasche= Wasserflasche(WIDTH-50, random.randint(50, HEIGHT-100), random.randint(3,7)* -1, random.randint(3, 7)* -1, wasserflasche_klein)
                    sprite_list.append(wasserflasche)
                    return Wasserflasche(WIDTH-50, random.randint(50, HEIGHT-100), random.randint(3,7)* -1, random.randint(3, 7)* -1, wasserflasche_klein)
        if randomgroesse==2: 
            if randomseite==1:
                if randomgetraenk==1 or randomgetraenk==3 or randomgetraenk==4 or randomgetraenk==5:
                    bierdose=Bierdose(0, random.randint(50, HEIGHT-100), random.randint(3,7), random.randint(3, 7), bierdose_gross)
                    sprite_list.append(bierdose)
                    return Bierdose(0, random.randint(50, HEIGHT-100), random.randint(3,7), random.randint(3, 7), bierdose_gross)
                if randomgetraenk==2:
                    wasserflasche= Wasserflasche(0, random.randint(50, HEIGHT-100), random.randint(3,7), random.randint(3, 7), wasserflasche_gross)
                    sprite_list.append(wasserflasche)
                    return Wasserflasche(0, random.randint(50, HEIGHT-100), random.randint(3,7), random.randint(3, 7), wasserflasche_gross)       
            if randomseite==2:
                if randomgetraenk==1 or randomgetraenk==3 or randomgetraenk==4 or randomgetraenk==5:
                    bierdose=Bierdose(WIDTH-50, random.randint(50, HEIGHT-100), random.randint(3,7)* -1, random.randint(3, 7)* -1, bierdose_gross)
                    sprite_list.append(bierdose)
                    return Bierdose(WIDTH-50, random.randint(50, HEIGHT-100), random.randint(3,7)* -1, random.randint(3, 7)* -1, bierdose_gross)
                if randomgetraenk==2:
                    wasserflasche= Wasserflasche(WIDTH-50, random.randint(50, HEIGHT-100), random.randint(3,7)* -1, random.randint(3, 7)* -1, wasserflasche_gross)
                    sprite_list.append(wasserflasche)
                    return Wasserflasche(WIDTH-50, random.randint(50, HEIGHT-100), random.randint(3,7)* -1, random.randint(3, 7)* -1, wasserflasche_gross)   
        if randomgroesse==3:
            if randomseite==1:
                if randomgetraenk==1 or randomgetraenk==3 or randomgetraenk==4 or randomgetraenk==5:
                    bierdose=Bierdose(0, random.randint(50, HEIGHT-100), random.randint(3,7), random.randint(3, 7), image_dict["bierdose"])
                    sprite_list.append(bierdose)
                    return Bierdose(0, random.randint(50, HEIGHT-100), random.randint(3,7), random.randint(3, 7), image_dict["bierdose"])
                if randomgetraenk==2:
                    wasserflasche= Wasserflasche(0, random.randint(50, HEIGHT-100), random.randint(3,7), random.randint(3, 7), image_dict["wasserflasche"])
                    sprite_list.append(wasserflasche)
                    return Wasserflasche(0, random.randint(50, HEIGHT-100), random.randint(3,7), random.randint(3, 7), image_dict["wasserflasche"])       
            if randomseite==2:
                if randomgetraenk==1 or randomgetraenk==3 or randomgetraenk==4 or randomgetraenk==5:
                    bierdose=Bierdose(WIDTH-50, random.randint(50, HEIGHT-100), random.randint(3,7)* -1, random.randint(3, 7)* -1, image_dict["bierdose"])
                    sprite_list.append(bierdose)
                    return Bierdose(WIDTH-50, random.randint(50, HEIGHT-100), random.randint(3,7)* -1, random.randint(3, 7)* -1, image_dict["bierdose"])
                if randomgetraenk==2:
                    wasserflasche= Wasserflasche(WIDTH-50, random.randint(50, HEIGHT-100), random.randint(3,7)* -1, random.randint(3, 7)* -1, image_dict["wasserflasche"])
                    sprite_list.append(wasserflasche)
                    return Wasserflasche(WIDTH-50, random.randint(50, HEIGHT-100), random.randint(3,7)* -1, random.randint(3, 7)* -1, image_dict["wasserflasche"])

# Concrete Creator B
#Level Kneipe Factory -> Randomseite  / 3Getränke  /  Verteilung  1/5_Jägermeister 1/5_Cafe 3/5_Bier
class KneipeFactory(IGetraenkFactory):
    def makeGetraenk(self): 
        randomseite=random.randint(1,2)
        randomgetraenk=random.randint(1,5)
        if randomseite==1:
                if randomgetraenk==1 or randomgetraenk==3 or randomgetraenk==4:
                    bierflasche=Bierflasche(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), bier_klein)
                    sprite_list.append(bierflasche)
                    return Bierflasche(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), bier_klein)
                if randomgetraenk==2:
                    cafe= Cafe(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), cafe_klein)
                    sprite_list.append(cafe)
                    return Cafe(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), cafe_klein) 
                if randomgetraenk==5:
                    jaegermeister= Jaegermeister(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), jaegermeister_klein)
                    sprite_list.append(jaegermeister)
                    return Jaegermeister(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), jaegermeister_klein)      
        if randomseite==2:
                if randomgetraenk==1 or randomgetraenk==3 or randomgetraenk==4:
                    bierflasche=Bierflasche(WIDTH-50, random.randint(20, HEIGHT-50), random.randint(3,7)* -1, random.randint(3, 7)* -1, bier_klein)
                    sprite_list.append(bierflasche)
                    return Bierflasche(WIDTH-50, random.randint(20, HEIGHT-50), random.randint(3,7)* -1, random.randint(3, 7)* -1, bier_klein)
                if randomgetraenk==2:
                    cafe= Cafe(WIDTH-50, random.randint(20, HEIGHT-50), random.randint(3,7)* -1, random.randint(3, 7)* -1, cafe_klein)
                    sprite_list.append(cafe)
                    return Cafe(WIDTH-50, random.randint(20, HEIGHT-50), random.randint(3,7)* -1, random.randint(3, 7)* -1, cafe_klein) 
                if randomgetraenk==5:
                    jaegermeister= Jaegermeister(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), jaegermeister_klein)
                    sprite_list.append(jaegermeister)
                    return Jaegermeister(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), jaegermeister_klein)

# Concrete Creator C
#Level Bahnhof Factory -> Randomseite  /  2Getränke  /  Verteilung 1/5_Limo 4/5_Bierflasche
class BahnnhofFactory(IGetraenkFactory):
    def makeGetraenk(self): 
        randomseite=random.randint(1,2)
        randomgetraenk=random.randint(1,5)
        if randomseite==1:
                if randomgetraenk==1 or randomgetraenk==3 or randomgetraenk==4 or randomgetraenk==5:
                    bierflasche=Bierflasche(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), image_dict["bierflasche"])
                    sprite_list.append(bierflasche)
                    return Bierflasche(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), image_dict["bierflasche"])
                if randomgetraenk==2:
                    limo = Limo(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), image_dict["limo"])
                    sprite_list.append(limo)
                    return Limo(0, random.randint(20, HEIGHT-50), random.randint(3,7), random.randint(3, 7), image_dict["limo"])       
        if randomseite==2:
                if randomgetraenk==1 or randomgetraenk==3 or randomgetraenk==4 or randomgetraenk==5:
                    bierflasche=Bierflasche(WIDTH-50, random.randint(20, HEIGHT-50), random.randint(3,7)* -1, random.randint(3, 7)* -1, image_dict["bierflasche"])
                    sprite_list.append(bierflasche)
                    return Bierflasche(WIDTH-50, random.randint(20, HEIGHT-50), random.randint(3,7)* -1, random.randint(3, 7)* -1, image_dict["bierflasche"])
                if randomgetraenk==2:
                    limo= Limo(WIDTH-50, random.randint(20, HEIGHT-50), random.randint(3,7)* -1, random.randint(3, 7)* -1, image_dict["limo"])
                    sprite_list.append(limo)
                    return Limo(WIDTH-50, random.randint(20, HEIGHT-50), random.randint(3,7)* -1, random.randint(3, 7)* -1, image_dict["limo"])
 
#Client    
class Client:
    def __init__(self, factory):
        self.factory = factory
        self.factory.makeGetraenk()
        print(factory)


