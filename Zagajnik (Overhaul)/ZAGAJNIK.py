import time
import random
from time import sleep
##### EKWIPUNEK ######
# WSZYSTKIE ITEMY BĘDĄ OPISANE W FORMIE SłOWNIKÓW : ITEM = {"name": nazwa_przedmiotu, "type": typ_przedmiotu, "doIhave": True/False (kolejne statystyki)}
from data.itemdefs import items
from data.inventory import inventory

#####STATYSTYKI GRACZA#####
class PlayerStats:
    def __init__(self, name, HP, MP, MaxHP, MaxMP, XP, level, str, dex, int, end, luck, basedamage, statpoints, spentstatpoints, pclass, subclass, combatstate, pointsspentstr, pointsspentdex, pointsspentint, pointsspentend, pointsspentluck, armorhead, armortorso, armorarms, armorlegs, eqaddedstr, eqaddeddex, eqaddedint, eqaddedend, eqaddedluck, basestr, basedex, baseint, baseend, baseluck):
        self.name = name
        self.HP = HP
        self.MP = MP
        self.MaxHP = MaxHP
        self.MaxMP = MaxMP
        self.XP = XP
        self.level = level
        self.str = str
        self.dex = dex
        self.int = int
        self.end = end
        self.luck = luck
        self.basedamage = basedamage
        self.statpoints = statpoints
        self.spentstatpoints = spentstatpoints
        self.pclass = pclass
        self.subclass = subclass
        self.combatstate = combatstate
        self.pointsspentstr = pointsspentstr
        self.pointsspentdex = pointsspentdex
        self.pointsspentint = pointsspentint
        self.pointsspentend = pointsspentend
        self.pointsspentluck = pointsspentluck
        self.armorhead = armorhead #zależne od ekwipunku
        self.armortorso = armortorso #
        self.armorarms = armorarms #
        self.armorlegs = armorlegs #
        self.eqaddedstr = eqaddedstr # 
        self.eqaddeddex = eqaddeddex #
        self.eqaddedint = eqaddedint #
        self.eqaddedend = eqaddedend #
        self.eqaddedluck = eqaddedluck #
        self.basestr = basestr
        self.basedex = basedex
        self.baseint = baseint
        self.baseend = baseend
        self.baseluck = baseluck
    
    def classchoice(self): #wybór startowej klasy, przedmioty mogą być dodane za pomocą tego (prawdopodobnie)
        print("Wybierz swoją początkową klasę.")
        print("Masz do wyboru zbrojnego, zwiadowcę i adepta magii.")
        print("(1/2/3)")
        while True:
            qwe = str(input())
            if qwe == "1":
                self.pclass = 1
                self.subclass = 1
                self.HP = 20 #maxhp się zwiększa wraz z siłą i wytrzymałością, podobnie jak mana; 4 (str) * 1 + 3 (end) * 2 = dodane maxhp
                self.MaxHP = 10 #
                self.MP = 5
                self.MaxMP = 0
                self.basestr = 4
                self.baseend = 3
                self.baseint = 1
                self.basedex = 3
                self.baseluck = 1
                print("Wybrałeś zbrojnego.")
                break
            if qwe == "2":
                self.pclass = 2
                self.subclass = 1
                self.HP = 15
                self.MaxHP = 10
                self.MP = 10
                self.MaxMP = 0
                self.basestr = 3
                self.baseend = 1
                self.baseint = 3
                self.basedex = 4
                self.baseluck = 2
                print("Wybrałeś zwiadowcę.")
                break
            if qwe == "3":
                self.pclass = 3
                self.subclass = 1
                self.HP = 10
                self.MaxHP = 6
                self.MP = 15
                self.MaxMP = 0
                self.basestr = 2
                self.baseend = 1
                self.baseint = 6
                self.basedex = 3
                self.baseluck = 1
                print("Wybrałeś adepta magii.")
                break
        return self
    def calcstats(self): #oblicza statystyki, by wszystko się zgadzało
        self.str = self.pointsspentstr + self.eqaddedstr + self.basestr
        self.dex = self.pointsspentdex + self.eqaddeddex + self.basedex
        self.int = self.pointsspentint + self.eqaddedint + self.baseint
        self.end = self.pointsspentend + self.eqaddedend + self.baseend
        self.luck = self.pointsspentluck + self.eqaddedluck + self.baseluck
        return self
        
    def calcmaxhp(self):
        self.MaxHP = 10+(1*self.str)+(2*self.end)
        if self.HP > self.MaxHP:
            self.HP = self.MaxHP
        if self.MaxHP < 0:
            print("Ta wiadomość nie powinna się pokazywać. Coś jest nie tak z twoim maksymalnym poziomem życia...")
            self.MaxHP = 1
            print("Ustawiono maksymalne życie na: 1")
        return self
    def calcmaxmp(self):
        self.MaxMP = 0+(1*self.dex)+(2*self.int)
        if self.MP > self.MaxMP:
            self.MP = self.MaxMP
        if self.MaxMP < 0:
            print("Ta wiadomość nie powinna się pokazywać. Coś jest nie tak z twoim maksymalnym poziomem many...")
            self.MaxMP = 0
            print("Ustawiono maksymalną manę na: 0")
        return self
    def calcdamage(self):
        self.basedamage = 1+(1*self.dex)+(2*self.str)
        if self.basedamage < 0:
            print("Ta wiadomość nie powinna się pokazywać. Coś jest nie tak z twoimi obrażeniami podstawowymi...")
            self.MaxMP = 1
            print("Ustawiono podstawowe obrażenia na: 1")
        return self
    def calclevel(self):
        if self.XP < 0:
            print("Ta wiadomość nie powinna się pokazywać. Coś jest nie tak z twoim poziomem...")
        if self.XP == 0:
            self.level = 0
            self.statpoints = 0
        if self.XP > 0 and self.XP <= 99:
            self.level = 1
            self.statpoints = 1 - self.spentstatpoints
        if self.XP >= 100 and self.XP <= 219:
            self.level = 2
            self.statpoints = 2 - self.spentstatpoints
        if self.XP >= 220 and self.XP <= 349:
            self.level = 3
            self.statpoints = 3 - self.spentstatpoints
        if self.XP >= 350 and self.XP <= 499:
            self.level = 4
            self.statpoints = 4 - self.spentstatpoints
        if self.XP >= 500 and self.XP <= 750:
            self.level = 5
            self.statpoints = 5 - self.spentstatpoints
        return self
    def displaystats(self):
        print(player.name, "nazwa gracza")
        print(player.HP, "hp")
        print(player.MP, "mp")
        print(player.MaxHP, "maxhp")
        print(player.MaxMP, "maxmp")
        print(player.XP, "xp")
        print(player.level, "lvl")
        print(player.str, "str")
        print(player.dex, "dex")
        print(player.int, "int")
        print(player.end, "end")
        print(player.luck, "luck")
        print(player.basedamage, "basedmg")
        print(player.statpoints, "statp")
        print(player.spentstatpoints, "spentstatp")
        print(player.pclass, "pclass")
        print(player.subclass, "subclass")
        print(player.combatstate, "combatstate")


#####STATYSTYKI GRACZA#####
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

player = PlayerStats("",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
player.name = str(input("Powiedz jak się nazywasz podróżniku.")) #możecie to dać pod komentarzem jak przeszkadza
player.classchoice() #to też możecie dać pod komentarzem
while True:
    player.calcstats()
    player.calcmaxhp()
    player.calcmaxmp()
    player.calcdamage()
    player.calclevel()
    ActionInput = input("[{} HP] [{} MP] [{} XP] [{} LVL] {}".format(player.HP,player.MP,player.XP,player.level,"\n")).lower()
    #zmieniłem inputa, powinien działać tak samo
    if x == "stats":
        player.displaystats()
    if x == "addxp":
        player.XP += 50
        print("dodano 50 xp")
    if x == "lvlup" and player.statpoints <= 0:
        print("nie masz wystarczająco punktów")
    if x == "lvlup" and player.statpoints > 0:
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



                      
            

        
            
        

    

    
