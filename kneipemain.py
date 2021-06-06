import pygame
import os
import random
import time
from factory import *
from settings import*

# Initialisierung
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dionysos")
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)
pygame.mouse.set_visible(False)

health_bar_width=1


def Leberwert(surface,x,y,value,maxvalue):
    xx=0
    for hp in range(value):
        pygame.draw.rect(surface, WEISS, (x+xx,y,100,32), 0)
        xx+= int(max(min(value / float(maxvalue) * health_bar_width, health_bar_width), 0))
    



#Scorboard Funktion 
def scoreboard():
    scoreboard_score=font.render(str(score_value),True,WEISS)
    screen.blit(scoreboard_score,[textX, textY])
    scoreboard_time=font.render(str(time_value),True,WEISS)
    screen.blit(scoreboard_time,[timeX, timeY])

def redrawGameWindow():    
    screen.blit(bg,(0,0))
    scoreboard()
    Leberwert(screen,0,HEIGHT-50,score_value,1)
    #pygame.draw.rect(screen, WEISS, (20,HEIGHT-200,100,32), 0)

frame=0
frame_b=0
score_value=1100
counter=0
time_value=0
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
            if score_value==0:
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
pygame.quit()
