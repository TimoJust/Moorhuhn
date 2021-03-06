from factory import *

def hs_bhf_Laden(fn = "./scoreBahnhof.txt"):
    #Aus Datei lesen
    hs = {}
    try:
        with open(fn,"r") as f:
            for zeile in f:
                name,_,punkte = zeile.partition(":")
                if name and punkte:
                    hs[name]=int(punkte)
    except FileNotFoundError:
        return {}
    return hs

def hs_penny_Laden(fn = "./scorePenny.txt"):
    #Aus Datei lesen
    hspenny = {}
    try:
        with open(fn,"r") as f:
            for zeile in f:
                name,_,punkte = zeile.partition(":")
                if name and punkte:
                    hspenny[name]=int(punkte)
    except FileNotFoundError:
        return {}
    return hspenny

def hs_kneipe_Laden(fn = "./scoreKneipe.txt"):
    #Aus Datei lesen
    hskneipe = {}
    try:
        with open(fn,"r") as f:
            for zeile in f:
                name,_,punkte = zeile.partition(":")
                if name and punkte:
                    hskneipe[name]=int(punkte)
    except FileNotFoundError:
        return {}
    return hskneipe

def hs_bhfEintragen(dictionary, fn = "./scoreBahnhof.txt", top_n=0):
    #Dictionary in Textdatei mit top_n höchsten Werten 
    with open(fn,"w") as f:
        for index,(name,pts) in enumerate(sorted(dictionary.items(), key= lambda x:-x[1])):
            f.write(f"{name}:{pts}\n")
            if top_n and index == top_n-1:
                break
            
def hs_kneipeEintragen(dictionary, fn = "./scoreKneipe.txt", top_n=0):
    #Dictionary in Textdatei mit top_n höchsten Werten 
    with open(fn,"w") as f:
        for index,(name,pts) in enumerate(sorted(dictionary.items(), key= lambda x:+x[1])):
            f.write(f"{name}:{pts}\n")
            if top_n and index == top_n+1:
                break

def hs_pennyEintragen(dictionary, fn = "./scorePenny.txt", top_n=0):
    #Dictionary in Textdatei mit top_n höchsten Werten 
    with open(fn,"w") as f:
        for index,(name,pts) in enumerate(sorted(dictionary.items(), key= lambda x:-x[1])):
            f.write(f"{name}:{pts}\n")
            if top_n and index == top_n-1:
                break

def highscore_bhfHinzufügen(name,score):
    b[name]=score

def highscore_kneipeHinzufügen(name,score):
    k[name]=score

def highscore_pennyHinzufügen(name,score):
    p[name]=score

def highscore_bhfAnzeigen():
    bb = hs_bhf_Laden()
    draw_text(str(bb))
    time.sleep(3)

def highscore_pennyAnzeigen():
    pp = hs_penny_Laden()
    draw_text(str(pp))
    time.sleep(3)

def highscore_kneipeAnzeigen():
    kk = hs_kneipe_Laden()
    draw_text(str(kk))
    time.sleep(3)


b = hs_bhf_Laden()
bb = hs_bhf_Laden()
p = hs_penny_Laden()
pp = hs_penny_Laden()
k = hs_kneipe_Laden()
kk = hs_kneipe_Laden()


#test=highscore_pennyAnzeigen()
#draw_text(str(test[1][0]))
#highscore_kneipeHinzufügen("Mo",32)
#hs_kneipeEintragen(k, top_n=3)
#highscore_kneipeAnzeigen()
#highscore_bhfHinzufügen("Sven",25)
#hs_bhfEintragen(k, top_n=3)
#highscore_bhfAnzeigen()
#highscore_pennyHinzufügen("Sven",25)
#hs_pennyEintragen(k, top_n=3)
#highscore_pennyAnzeigen()