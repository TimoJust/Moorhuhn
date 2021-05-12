import pygame
from settings import *
from sprites import *
from factory import *

# Initialisierung
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mein Spiel")
clock = pygame.time.Clock()


# Sprites
factory = Factory()
sprite_list = factory.getSprites()

# Game Loop
running = True
bewegung = True

while running:
    # Das ist noch nicht gut -> State Pattern
    # FPS
    clock.tick(FPS)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            factory.generateSpriteFromMouse(x, y)
            sprite_list = factory.getSprites()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bewegung = not bewegung

    # Update
    if bewegung:
        for sprite in sprite_list:
            sprite.update()

    # Rendern
    #screen.fill(WEISS)
    
    #10.05.2021 Malte Background Image Anfang
    screen.blit(factory.background_image, (0,0))
    #10.05.2021 Malte Background Image Ende
    for sprite in sprite_list:
        sprite.render(screen)

    # Display
    pygame.display.flip()
    

pygame.quit()
