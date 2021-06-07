import pygame
# Settings
pygame.display.set_caption("Dionysos - Mo(o)r(e)alk - Genug getrunken, ab jetzt wird gesoffen!")
WIDTH = 1280# 1250 # 
HEIGHT = 720#938#
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
textX=290
textY=HEIGHT-50
timeX=WIDTH-70
timeY=HEIGHT-50

