from factory import *
import operator

player="Malia"
scoreplayer=1000

def hs_Eintragen(dictionary, fn = "./high.txt", top_n=0):
    #Dictionary in Textdatei mit top_n höchsten Werten 
    with open(fn,"w") as f:
        for index,(name,pts) in enumerate(sorted(dictionary.items(), key= lambda x:-x[1])):
            f.write(f"{name}:{pts}\n")
            if top_n and index == top_n-1:
                break

def hs_Laden(fn = "./high.txt"):
    #Aus Datei lesen
    highscore_Dict = {}
    try:
        with open(fn,"r") as f:
            for zeile in f:
                name,_,punkte = zeile.partition(":")
                if name and punkte:
                    highscore_Dict[name]=int(punkte)
    except FileNotFoundError:
        return {}
    return highscore_Dict

def highscore_Hinzufügen():
    highscore_Dict[player] = scoreplayer

def highscore_Sortieren():
    sortierter_Highscore = sorted(hs_Laden.highscore_Dict, key=hs_Laden.highscore_Dict.get, reverse=True)

#sortierter_Highscore = sorted(highscore_Dict, key=highscore_Dict.get, reverse=True)
#for r in sortierter_Highscore:
#    print(r, highscore_Dict[r])


#draw_text('1. '+str(sortierter_Highscore[0])+': '+str(highscore_Dict[sortierter_Highscore[0]])+' Punkte\n\n2. '+str(sortierter_Highscore[1])+': '+str(highscore_Dict[sortierter_Highscore[1]])+' Punkte\n\n3. '+str(sortierter_Highscore[2])+': '+str(highscore_Dict[sortierter_Highscore[2]])+' Punkte\n\n\n\n\n\nDeine Punkte '+player+': '+str(scoreplayer)+'')
#time.sleep(5) 


k = hs_Laden()
k[player]=scoreplayer
hs_Eintragen(player, top_n=3)