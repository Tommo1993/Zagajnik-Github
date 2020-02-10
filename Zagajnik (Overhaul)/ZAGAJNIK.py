import time
import random
from time import sleep
from data.player import *
##### EKWIPUNEK ######
# WSZYSTKIE ITEMY BĘDĄ OPISANE W FORMIE SłOWNIKÓW : ITEM = {"name": nazwa_przedmiotu, "type": typ_przedmiotu, "doIhave": True/False (kolejne statystyki)}
from data.itemdefs import items
from data.inventory import inventory
from data.skrypt_wykazu_itemow import wykaz_itemow
wykaz_itemow()
itemlist = items()
#####SYSTEM QUESTÓW#####
#####SYSTEM QUESTÓW#####
#####GŁÓWNY MODUŁ#####
akcja=['Zjedz','Użyj','Opis','Atakuj','Zagadaj']
OtherAction=['zjedz','użyj','opis','atakuj','zagadaj', 'ubierz', 'dobądź', 'zdejmij', 'schowaj', 'ekwipunek', 'weź']
ItemAction=['zjedz','użyj','opis','ubierz','dobądź','zdejmij','schowaj','ekwipunek']
DebugAction=['debug']
InformacjeLokacji = [[1,0,0,0],[0,0],[]]
def ActInput(ActionInput):
    ActionInput = input().lower()
    return ActionInput
itemlist = items()
helmet = itemlist["puste"]
chestplate = itemlist["puste"]
legs = itemlist["puste"]
gloves = itemlist["puste"]
item1 = "puste"
item2 = "puste"
item3 = "puste"
item4 = "puste"
item5 = "puste"
amulet = itemlist["brak_amuletu"]
weapon = itemlist["brak broni"]
ekwipunek = [helmet, chestplate, legs, gloves, item1, item2, item3, item4, item5, amulet]

    

def ActionCheck(ActionInput,Lokacja,LocMoveset):
    if ActionInput in OtherAction:
        if ActionInput in ItemAction:
            print("przeniesione")
    if ActionInput in DebugAction:
        if ActionInput == 'debug':
            print("Jakieś dane tu się będą pokazywać") 
    if (ActionInput not in OtherAction) and (ActionInput not in DebugAction) and (ActionInput != "questy"):
        print('???')
    return ActionInput, Lokacja

clear = "\n" * 100
def clear():
    print(clear)

ActionInput = ""

def TekstJeden():
    TamNiePójdziesz = 'Brak możliwości ruchu.   '
    for i in TamNiePójdziesz:
        print (i, end='')
        sleep(0.01)

def Lokacja1():
    DescLok1 = 'To jest Lokacja nr. 1 gry Zagajnik.'
    for i in DescLok1:
        print (i, end='')
        sleep(0.01)
        
def Lokacja2():
    DescLok2 = 'To jest Lokacja nr. 2 gry Zagajnik.'
    for i in DescLok2:
        print (i, end='')
        sleep(0.01)
    
YW = ['W','w']
YS = ['S','s']
XA = ['A','a']
XD = ['D','d']

player = PlayerStats("",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100.0,100.0)
player.name = str(input("Powiedz jak się nazywasz podróżniku.")) #możecie to dać pod komentarzem jak przeszkadza
player.classchoice() #to też możecie dać pod komentarzem

while True:

    #if InformacjeLokacji[2] != []:
        #print('Na ziemi leży:' CoNaZiemi)

    player.eqaddedstr = int(ekwipunek[0]["dodawana_siła"]+ekwipunek[1]["dodawana_siła"]+ekwipunek[2]["dodawana_siła"]+ekwipunek[3]["dodawana_siła"]+ekwipunek[9]["dodawana_siła"])
    player.eqaddeddex = int(ekwipunek[0]["odejmowana_zręczność"]+ekwipunek[1]["odejmowana_zręczność"]+ekwipunek[2]["odejmowana_zręczność"]+ekwipunek[3]["odejmowana_zręczność"]+ekwipunek[9]["dodawana_zręczność"])
    player.eqaddedint = int(ekwipunek[0]["dodawana_inteligencja"]+ekwipunek[1]["dodawana_inteligencja"]+ekwipunek[2]["dodawana_inteligencja"]+ekwipunek[3]["dodawana_inteligencja"]+ekwipunek[9]["dodawana_inteligencja"])
    player.eqaddedend = int(ekwipunek[0]["dodawana_wytrzymałość"]+ekwipunek[1]["dodawana_wytrzymałość"]+ekwipunek[2]["dodawana_wytrzymałość"]+ekwipunek[3]["dodawana_wytrzymałość"]+ekwipunek[9]["dodawana_wytrzymałość"])
    player.eqaddedluck = int(ekwipunek[0]["dodawane_szczęście"]+ekwipunek[1]["dodawane_szczęście"]+ekwipunek[2]["dodawane_szczęście"]+ekwipunek[3]["dodawane_szczęście"]+ekwipunek[9]["dodawane_szczęście"])
    player.armortorso = (int(ekwipunek[1]["ochrona"]) / 2) + int(ekwipunek[3]["ochrona"])
    player.armorhead = int(ekwipunek[0]["ochrona"])
    player.armorlegs = int(ekwipunek[2]["ochrona"])
    player.calcstats()
    player.calcmaxhp()
    player.calcmaxmp()
    player.hpmpscaling()
    player.calcdamage()
    player.calclevel()
    player.prevhpscaling()
    print() #TEMP FIX
    ActionInput = input("[{} HP] [{} MP] [{} XP] [{} LVL] {}".format(player.HP,player.MP,player.XP,player.level,"\n")).lower()
    #zmieniłem inputa, powinien działać tak samo
    if ActionInput == "stats":
        player.displaystats()
    if ActionInput == "addxp":
        player.XP += 50
        print("dodano 50 xp")
    if ActionInput == "lvlup" and player.statpoints <= 0:
        print("nie masz wystarczająco punktów")
    if ActionInput == "lvlup" and player.statpoints > 0:
        y = input("wybierz, którą statystykę chcesz ulepszyć (str/dex/int/end/luck)")
        if y == "str":
            player.pointsspentstr += 1
            player.spentstatpoints += 1
            player.calclevel()
        if y == "dex":
            player.pointsspentdex += 1
            player.spentstatpoints += 1
            player.calclevel()
        if y == "int":
            player.pointsspentint += 1
            player.spentstatpoints += 1
            player.calclevel()
        if y == "end":
            player.pointsspentend += 1
            player.spentstatpoints += 1
            player.calclevel()
        if y == "luck":
            player.pointsspentluck += 1
            player.spentstatpoints += 1
            player.calclevel()
        if y not in ("str","dex","int","end","luck"):
            print("zła odpowiedź")                         #kod co do statystyk gracza tu się kończy            
    items()
    itemlist = items()
    inventory(ekwipunek, ActionInput, itemlist, player)
    if InformacjeLokacji[0][0] == 1 and ActionInput in YW:
        InformacjeLokacji[1][1] = InformacjeLokacji[1][1]+1
    if InformacjeLokacji[0][0] == 0 and ActionInput in YW:
        TekstJeden()
        
    if InformacjeLokacji[0][1] == 1 and ActionInput in YS:
        InformacjeLokacji[1][1] = InformacjeLokacji[1][1]-1
    if InformacjeLokacji[0][1] == 0 and ActionInput in YS:
        TekstJeden()

    if InformacjeLokacji[0][2] == 1 and ActionInput in XA:
        InformacjeLokacji[1][0] = InformacjeLokacji[1][0]+1
    if InformacjeLokacji[0][2] == 0 and ActionInput in XA:
        TekstJeden()
        
    if InformacjeLokacji[0][3] == 1 and ActionInput in XD:
        InformacjeLokacji[1][0] = InformacjeLokacji[1][0]-1
    if InformacjeLokacji[0][3] == 0 and ActionInput in XD:
        TekstJeden()

    if InformacjeLokacji[1][0] == 0 and InformacjeLokacji[1][1] == 0:
        InformacjeLokacji[0][0] = 1
        InformacjeLokacji[0][1] = 0
        InformacjeLokacji[0][2] = 0
        InformacjeLokacji[0][3] = 0
        Lokacja1()
    if InformacjeLokacji[1][0] == 0 and InformacjeLokacji[1][1] == 1:
        InformacjeLokacji[0][0] = 0
        InformacjeLokacji[0][1] = 1
        InformacjeLokacji[0][2] = 0
        InformacjeLokacji[0][3] = 0
        Lokacja2()



                      
            

        
            
        

    

    
