from settings import *

class IDisplay_Hintergrund_Behavior:
    def display(self):
        raise NotImplementedError
class Penny(IDisplay_Hintergrund_Behavior):
    def display(self):
        penny = pygame.image.load("penny.jpg")        
        screen.blit(penny,position)
class Kneipe(IDisplay_Hintergrund_Behavior):
    def display(self):
        kneipe = pygame.image.load("kneipe.jpg")
        screen.blit(kneipe,position)
class Bahnhof(IDisplay_Hintergrund_Behavior):
    def display(self):
        bahnhof = pygame.image.load("bahnhof.jpg")
        screen.blit(bahnhof,position)
class BildHintergrund:
    position = (0,0)
    def __init__(self, dp: IDisplay_Hintergrund_Behavior):
        self.auswählen = dp
    def hintergrund_anzeigen(self):
        self.auswählen.display(self)

penny = BildHintergrund(Penny)
kneipe = BildHintergrund(Kneipe)
hauptbahnhof = BildHintergrund(Bahnhof)


