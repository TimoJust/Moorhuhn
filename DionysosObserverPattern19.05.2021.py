"""
Observer Pattern für Dionysos, dient der Übergabe 
von Achivments und Punkten.
Autor: Sven Radzabov
"""
# xxx Nur zum Testen der Ausgabe auskommentieren xxx
import ctypes  
from pygame.constants import JOYAXISMOTION

""" Die Klasse Achivment() speichert die Namen und Punkte der Spieler """

class Achievment():
    def __init__(self, spielerName: str, punkte: int, achievmentText: str):
        self._spielerName = spielerName
        self._punkte = punkte
        self.achievmentText = achievmentText
    
    def textausgaben(self):
        return self._achievmentText
    
    def punkteausgeben(self):
        return self._punkte

""" Das Interfafe IObserver() übergibt die methode update() an die Klasse Achivment """

class IObserver():
    def update(self, newAchivment: Achievment):
        raise NotImplementedError

""""
Klasse Display() implementiert Interface IOserver().
Sie dient der Übergabe von Punkten und Achivments an das 
Display vom Spiel
"""

class Display(IObserver):
    def __init__(self):
        """ Der Punktestand beginnt mit 0 Punkten"""
        self._pukteAnzeige = 0 
    
    def update(self, newAchivment: Achievment):
        self._pukteAnzeige = newAchivment.punkteausgeben()
        print("Display Punkteanzahl =", self._pukteAnzeige)
        displayText = "Der Spieler hat " + str(self._pukteAnzeige) + "Punkte."
        # Nur zum Testen auskommentieren 
        ctypes.windll.user32.MessageBoxW(0, displayText , "Meine Punkte-Anzeige", 1)


""" Klasse AktuellerSpieler(IObserver) dient dazu den Observer 
also aktuellen Spieler darüber zu informieren das ein neuen Spieler
ein Achivment erreicht hat 

Die Klasse implementiert die Methode update() von IObserver

"""

class AktuellerSpieler(IObserver):
    def __init__(self, name):
        self.name = name
        print("Es wurde ein neuer Spieler erstellt: ", self.name)
    
    def update(self, newAchievment: Achievment):
        print("Observer", self.name, "wird informiert: ")
        """ Hier wird der aktuelle Obeserver informiert """

"""
Die Klasse Datenbank sogrt für die Registrierung / Löschung 
und Benachrichtigung der Observer.

"""

class Datenbank(): 
    def __init__(self):
        self._listeDerSpieler = []
    
    def register(self, observer: IObserver):
         self._listeDerSpieler.append(observer)

    def unregister(self, observer: IObserver):
        self._listeDerSpieler.remove(observer)
    
    def _notify(self, achievement: Achievment):
        print("Die Datenbank informiert die Observer über das neueste Achievment")
        for observer in self._listeDerSpieler:
            observer.update(achievement)


""" 
Die Klasse Achivmentdatenbak legt ein Dictionary mit Spieler und Punktestand an.
Zudem enthält die Klasse verschiedene Achivments, die ausgegeben werden können. 
"""

class AchievmentDatenbank(Datenbank):
    def __init__(self):
        super().__init__()
        """ Dictionary = { "spielerName" : Punktestand } """
        self._punkteStandSpieler = {}

    """ erzieltesAchievment() ruft die notify() aus der Datenbank auf und informiert 
    die Observer über das neueste Achievment """

    def erzieltesAchievment(self):
        self._notify()
    
    def addSpieler(self, observer: IObserver, name: str):
        self.register(observer)
        self._punkteStandSpieler[name] = 0

    def treffer(self, spielerName: str, flugObjekt: str, punkte: int):
        self._punkteStandSpieler[spielerName] = self._punkteStandSpieler[spielerName] + punkte
    

        """ Verschiedene Achievments """
        achievmentText = ""
        if punkte == 10 :
            achievmentText = "Trunkenbold"
            print(achievmentText)
        
        if punkte ==25:
            achievmentText = "Schluckspecht"
            print(achievmentText)
        
        if punkte ==50:
            achievmentText = "Schnapsdrossel"
            print(achievmentText)
        
        if punkte ==100:
            achievmentText = "Saufbruder"
            print(achievmentText)

        newAchievment = Achievment(spielerName, punkte, achievmentText)
        print("Datenbank wurde informiert, dass der Spieler ", spielerName, " ", punkte, " Punkte bekommen hat.")
        self._notify(newAchievment)



"""
Nachfolgend angelegte Spieler und  Registrierte Spieler zum Testen 
Beim Mergen auskommentieren.

"""
achchivmentdatenbank = AchievmentDatenbank()

spielerSven = AktuellerSpieler("Sven")
spielerMalte= AktuellerSpieler("Malte")

achchivmentdatenbank.addSpieler(spielerSven, spielerSven.name)
achchivmentdatenbank.addSpieler(spielerMalte, spielerMalte.name)

myDisplay = Display()
achchivmentdatenbank.register(myDisplay)

achchivmentdatenbank.treffer(spielerSven.name, "Bier", 51)
       
    # TEST TEST
    