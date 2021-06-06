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
pygame.display.set_caption("Mooralk")
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)
pygame.mouse.set_visible(False)


#Scorboard Funktion 
def scoreboard():
    screen.blit(image_dict["score"], [timeX-110, timeY])
    screen.blit(image_dict["score"], [textX+30, textY-30])
    scoreboard_score=font.render(str(score_value),True,WEISS)
    screen.blit(scoreboard_score,[textX+100, textY+5])
    scoreboard_time=font.render(str(time_value),True,WEISS)
    screen.blit(scoreboard_time,[timeX-50, timeY+32])
    

def redrawGameWindow():    
    screen.blit(bg,(0,0))
    scoreboard()

frame=0
frame_b=0

running = True
while running:
    # Game Loop
    clock.tick(FPS)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT: 
            time_value -= 1           
            #Factory nach x sek starten
            if time_value ==89 or time_value ==80 or time_value ==70 or time_value ==60 or time_value ==50 or time_value ==40 or time_value ==30 or time_value ==20 or time_value ==10: 
                #X Factory für _ mal starten
                for _ in range(1, 7):
                    Client(PennyFactory())
            if time_value==0:
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
         if sprite.getraenk_rect.collidepoint(event.pos):  #event.pos = Maus Position beim klick
            print("Treffer")
            
            
            if type(sprite)==Bierdose or type(sprite)==Bierflasche or type(sprite)==Bier:
                score_value+=20
            if type(sprite)==Limo or type(sprite)==Cafe or type(sprite)==Wasserflasche:
                score_value-=20

            sprite_list.remove(sprite)
        frame = 0
    # Display
    pygame.display.flip()
pygame.quit()
