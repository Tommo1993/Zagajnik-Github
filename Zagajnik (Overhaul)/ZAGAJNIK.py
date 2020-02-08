import time
import random
from time import sleep
##### EKWIPUNEK ######
# WSZYSTKIE ITEMY BĘDĄ OPISANE W FORMIE SłOWNIKÓW : ITEM = {"name": nazwa_przedmiotu, "type": typ_przedmiotu, "doIhave": True/False (kolejne statystyki)}
from data.itemdefs import items
from data.inventory import inventory

#####SYSTEM QUESTÓW#####
def Questy():
        
    DaneQuesta=[0,"","","","",0,0,0,0] #Slot 0- Aktywność questa Slot 1- Nazwa Slot 2- Opis Slot 3- Zleceniodawca Slot 4- Nagroda przedmiot Slot 5- ilość exp Slot 6- nagroda pieniądze 7- ID questa 8- status
    DaneQuesta1=[0,"Miejscowy Bohater","Zostało mi powierzone bardzo trudne zadanie - odnaleźć łyżeczkę dżemu.","Staruszek z Crosset","",100,5,1,0]
    DaneWszystkichQuestów=[]
    DaneWszystkichQuestów.append(DaneQuesta)
    DaneWszystkichQuestów.append(DaneQuesta1)
    #print(DaneWszystkichQuestów)
    return DaneWszystkichQuestów

def SprawdzanieStatusu(DaneWszystkichQuestów, ActionInput, SzukanieMiejscaNaPrzedmiot, KoniecQuesta):
    while DaneWszystkichQuestów[1][0] == 1 and DaneWszystkichQuestów[1][7] >0:
        if DaneWszystkichQuestów[1][8] == 0 and DaneWszystkichQuestów[1][7] == 1 and ActionInput == "quests":
            print('''Miejscowy Bohater - Odnajdź łyżeczkę dżemu.
            Nagroda - 5 Koron, 100exp
            Zleceniodawca - Staruszek z Crosset''')
        if DaneWszystkichQuestów[1][8] == 1 and DaneWszystkichQuestów[1][7] == 1 and ActionInput == "quests":
            print('''Miejscowy Bohater - Wykonane.
            Nagroda - 5 Koron, 100exp
            Zleceniodawca - Staruszek z Crosset''')
        if DaneWszystkichQuestów[1][8] == 1 and DaneWszystkichQuestów[1][7] == 1:
            print('''Zadanie "Miejscowy Bohater" zostało ukończone.
            Wróć do zleceniodawcy po nagrodę.''')
            if DaneWszystkichQuestów[1][8] == 1 and Lokacja == 12:
                print('''Dziękuje Ci! Kto jest małą łyżeczką, no kto!
            Żebym nie wyszedł na dusigrosza o to mała nagroda.''')
                print('Otrzymano: 5 Koron')
                if DaneWszystkichQuestów[1][4] == 0:
                    KoniecQuesta(player, Questy)
                    DaneQuesta1[0] == 3
                if DaneWszystkichQuestów[1][4] != 0:
                    SzukanieMiejscaNaPrzedmiot(item, KoniecQuesta)
                    KoniecQuesta(player, Questy)
                    DaneWszystkichQuestów[1][0] == 3
    
def PrintQuest(Questy):
    print()
    print(DaneQuesta[1])
    print(DaneQuesta[2])
    print(DaneQuesta[3])
    print(DaneQuesta[4])
    print(DaneQuesta[5])
    print(DaneQuesta[6])
    print()

def KoniecQuesta(player, Questy):
    player.EXP += DaneQuesta[5]
    item.gold += DaneQuesta[6]
    OtrzymanyPRZEDMIOT = DaneQuesta[4]
    return player.EXP

def SzukanieMiejscaNaPrzedmiot(KoniecQuesta):
    SprawdzenieMiejsca = []
    
    if item.inventoryslot1[0] == 0:
        item.inventoryslot1 == OtrzymanyPRZEDMIOT
    if item.inventoryslot1[0] == 1:
        if SprawdzenieMiejsca in locals():
            del SprawdzenieMiejsca
            SprawdzenieMiejsca=[]
        SprawdzenieMiejsca.append(1)
        return SprawdzenieMiejsca
        
    if item.inventoryslot2[0] == 0:
        item.inventoryslot2 == OtrzymanyPRZEDMIOT      
    if SprawdzenieMiejsca[0] == 1:
        if item.inventoryslot2[0] == 1:
            if SprawdzenieMiejsca in locals():
                del SprawdzenieMiejsca
                SprawdzenieMiejsca=[]
            SprawdzenieMiejsca.append(2)
            return SprawdzenieMiejsca
            
    if item.inventoryslot3[0] == 0:
        item.inventoryslot3 == OtrzymanyPRZEDMIOT            
    if SprawdzenieMiejsca[0] == 2:
        if item.inventoryslot3[0] == 1:
            if SprawdzenieMiejsca in locals():
                del SprawdzenieMiejsca
                SprawdzenieMiejsca=[]
            SprawdzenieMiejsca.append(3)
            return SprawdzenieMiejsca
            
    if item.inventoryslot4[0] == 0:
        item.inventoryslot4 == OtrzymanyPRZEDMIOT
    if SprawdzenieMiejsca[0] == 3:        
        if item.inventoryslot4[0] == 1:
            if SprawdzenieMiejsca in locals():
                del SprawdzenieMiejsca
                SprawdzenieMiejsca=[]
            SprawdzenieMiejsca.append(4)
            return SprawdzenieMiejsca
    
    if item.inventoryslot5[0] == 0:
        item.inventoryslot5 == OtrzymanyPRZEDMIOT
    if item.inventoryslot5[0] == 1:
        if SprawdzenieMiejsca in locals():
            del SprawdzenieMiejsca
            SprawdzenieMiejsca=[]
        SprawdzenieMiejsca.append(5)
        return SprawdzenieMiejsca
        
    if item.inventoryslot6[0] == 0:
        item.inventoryslot6 == OtrzymanyPRZEDMIOT
    if item.inventoryslot6[0] == 1:
        if SprawdzenieMiejsca in locals():
            del SprawdzenieMiejsca
            SprawdzenieMiejsca=[]
        SprawdzenieMiejsca.append(6)
        return SprawdzenieMiejsca
        
    if item.inventoryslot7[0] == 0:
        item.inventoryslot7 == OtrzymanyPRZEDMIOT
    if item.inventoryslot7[0] == 1:
        if SprawdzenieMiejsca in locals():
            del SprawdzenieMiejsca
            SprawdzenieMiejsca=[]
        SprawdzenieMiejsca.append(7)
        return SprawdzenieMiejsca
    
    if item.inventoryslot8[0] == 0:
        item.inventoryslot8 == OtrzymanyPRZEDMIOT
    if item.inventoryslot8[0] == 1:
        if SprawdzenieMiejsca in locals():
            del SprawdzenieMiejsca
            SprawdzenieMiejsca=[]
        SprawdzenieMiejsca.append(8)
        return SprawdzenieMiejsca
    
    if item.inventoryslot10[0] == 0:
        item.inventoryslot10 == OtrzymanyPRZEDMIOT
    if item.inventoryslot10[0] == 1:
        print('Brak miejsca w ekwipunku!')
        #PrzedmiotNaGape1 = 1
        #while PrzedmiotNaGape1 == 1 and Lokacja == LokacjaZleceniodawcy:
        #   SzukanieMiejscaNaPrzedmiot(item, KoniecQuesta)
#####SYSTEM QUESTÓW#####

#####GRACZ#####
class PlayerStats:
    def __init__(player, name, HP, MP, MaxHP, MaxMP, MaxHPnocalc, MaxMPnocalc, EXP, level, str, dex, int, end, luck, basedamage, weapondamage, statpoint, pclass, subclass):
        player.name = name
        player.HP = HP
        player.MP = MP
        player.MaxHP = MaxHP
        player.MaxMP = MaxMP
        player.MaxHPnocalc = MaxHPnocalc
        player.MaxMPnocalc = MaxMPnocalc
        player.EXP = EXP
        player.level = level
        player.str = str
        player.dex = dex
        player.int = int
        player.end = end
        player.luck = luck
        player.basedamage = basedamage
        player.weapondamage = weapondamage
        player.statpoint = statpoint
        player.pclass = pclass
        player.subclass = subclass
def ClassChoice(player,StartInput):		
    if StartInput == "1" or StartInput == "zbrojny":
        print("Twoja klasa to zbrojny.")
        player.MaxHP == 20
        player.HP == 20
        player.MaxMP == 5
        player.MP == 5
        player.str = 3
        player.dex = 2
        player.int = 1
        player.end = 2
        player.luck = 1
        player.pclass = 1
    if StartInput == "2" or StartInput == "zwiadowca":
        rint("Twoja klasa to zwiadowca.")
        player.MaxHP == 15
        player.HP == 15
        player.MaxMP == 10
        player.MP == 5
        player.pclass = 2
    if StartInput == "3" or StartInput == "łotr":
        print("Twoja klasa to łotr.")
        player.MaxHP == 10
        player.HP == 10
        player.MaxMP == 15
        player.MP == 15
        player.pclass = 3
    return player

#####GRACZ#####


#####GŁÓWNY MODUŁ#####
akcja=['Zjedz','Użyj','Opis','Atakuj','Zagadaj']
OtherAction=['zjedz','użyj','opis','atakuj','zagadaj', 'ubierz', 'dobądź', 'zdejmij', 'schowaj', 'ekwipunek', 'weź']
ItemAction=['zjedz','użyj','opis','ubierz','dobądź','zdejmij','schowaj','ekwipunek']
DebugAction=['debug']
InformacjeLokacji = [[1,0,0,0],[0,0]]
def ActInput(ActionInput):
    ActionInput = input().lower()
    return ActionInput
helmet = "puste"
chestplate = "puste"
legs = "puste"
gloves = "puste"
item1 = "puste"
item2 = "puste"
item3 = "puste"
item4 = "puste"
item5 = "puste"
ekwipunek = [helmet, chestplate, legs, gloves, item1, item2, item3, item4, item5]

    

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
player = PlayerStats(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)

###########################################################################
###########################################################################
###########################################################################
###########################################################################

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


while True:
    ActionInput = str(input())
    items()
    itemlist = items()
    inventory(ekwipunek, ActionInput, itemlist)
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



                      
            

        
            
        

    

    
