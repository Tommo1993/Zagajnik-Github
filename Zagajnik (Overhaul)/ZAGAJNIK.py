import time
import random
from time import sleep
##### EKWIPUNEK ######
# WSZYSTKIE ITEMY BĘDĄ OPISANE W FORMIE SłOWNIKÓW : ITEM = {"name": nazwa_przedmiotu, "type": typ_przedmiotu, "doIhave": True/False (kolejne statystyki)}
from data.itemdefs import items
from data.inventory import inventory
from data.skrypt_wykazu_itemow import wykaz_itemow
wykaz_itemow()
itemlist = items()
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
                self.HP = 20  #maxhp się zwiększa wraz z siłą i wytrzymałością, podobnie jak mana; 4 (str) * 1 + 3 (end) * 2 = dodane maxhp
                self.MaxHP = 10  #
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
            self.MaxHP = 1
            print("Życie poniżej zera; ustawiono na 0.")
        return self
    def calcmaxmp(self):
        self.MaxMP = 0+(1*self.dex)+(2*self.int)
        if self.MP > self.MaxMP:
            self.MP = self.MaxMP
        if self.MP < 0:
            self.MP = 0
        if self.MaxMP < 0:
            self.MaxMP = 0
            print("Mana poniżej zera; ustawiono na 0.")
        return self
    def calcdamage(self):
        self.basedamage = 1+(1*self.dex)+(2*self.str)
        if self.basedamage < 0:
            self.MaxMP = 1
            print("Obrażenia poniżej zera; ustawiono na 0.")
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

player = PlayerStats("",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
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
    player.calcdamage()
    player.calclevel()
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



                      
            

        
            
        

    

    
