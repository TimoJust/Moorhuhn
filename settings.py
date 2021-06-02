import pygame
# Settings
WIDTH = 1280
HEIGHT = 720
FPS = 60
WEISS = (255, 255, 255)
SCHWARZ = (0, 0, 0)
BLAU = (0, 0, 255)
ROT = (255, 0, 0)
SLATEGRAY_3 = (159,182,205)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
position = (0,0)
pygame.font.init()
#Score 
score_value=0
time_value=90
font =pygame.font.SysFont(None, 50)
textX=50
textY=50
timeX=WIDTH-50
timeY=50

