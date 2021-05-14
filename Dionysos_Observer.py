

"""Observer Design Pattern
"""

from abc import ABCMeta, abstractstaticmethod

class IObserver(metaclass=ABCMeta):
    @staticmethod
    @abstractstaticmethod

    def update(self, postAchivment: str):
        """ Interface Method 
        von  Sven
        Quelle: Krauss observer.py  """
        raise NotImplementedError



class AktuellerSpieler(IObserver):
    def __init__(self,name):
        self.name = name
        
    
    def update(self, postAchivment: str):
        print(self.name)
        # wer gerade beobachtet sven und ben 
        print(postAchivment)


class Datenbank():
    def __init__(self):
        self._listeSpieler = []
        self.latestAchivment = ""

    def register(self, observer: IObserver):
         self._listeSpieler.append(observer)

    def unregister(self, observer: IObserver):
        self._listeSpieler.remove(observer)

    def _notify(self):
        for observer in self._listeSpieler:
            observer.update(self.latestAchivment) 


class AchivmentDatenbank(Datenbank):
    def erzieltEinAchivment(self, postAchivment):
        self.observer = postAchivment
        self._notify()


achivmentDatenbank= AchivmentDatenbank()

spielerSven= AktuellerSpieler("Sven")
spielerBen= AktuellerSpieler("Ben")

achivmentDatenbank.register(spielerSven)
achivmentDatenbank.register(spielerBen)

achivmentDatenbank.latestAchivment = "Hans hat 100 Punkte"

achivmentDatenbank._notify()