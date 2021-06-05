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
    #scoreboard_score=font.render(str(score_value),True,WEISS)
    #screen.blit(scoreboard_score,[textX, textY])
    screen.blit(image_dict["score"], [timeX-110, timeY])
    scoreboard_time=font.render(str(time_value),True,WEISS)
    screen.blit(scoreboard_time,[timeX-50, timeY+32])

def redrawGameWindow():    
    screen.blit(bg,(0,0))
    scoreboard()
time_value=30
counter=0
running = True
while running:
    # Game Loop
    clock.tick(FPS)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT: 
            time_value -= 1   
            if counter==0:
                for _ in range(1, 7):
                    Client(BahnnhofFactory())
                counter=5
            counter-=1
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
            #Neues Getränk Spawnen
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
        screen.blit(hand[1],(x-20,y-20))
        for sprite in sprite_list:
         if sprite.getraenk_rect.collidepoint(event.pos):  #event.pos = Maus Position beim klick
            print("Treffer")
            if type(sprite)==Bierflasche:
                time_value+=1
            if type(sprite)==Limo:
                time_value-=3
            sprite_list.remove(sprite)
    # Display
    pygame.display.flip()
pygame.quit()
