import time
import random
from time import sleep
from data.player import *
##### EKWIPUNEK ######
# WSZYSTKIE ITEMY BĘDĄ OPISANE W FORMIE SłOWNIKÓW : ITEM = {"name": nazwa_przedmiotu, "type": typ_przedmiotu, "doIhave": True/False (kolejne statystyki)}
from data.itemdefs import items
from data.inventory import inventory
from data.skrypt_wykazu_itemow import wykaz_itemow
from data.entity import EntityStats

wykaz_itemow()
itemlist = items()
#####SYSTEM QUESTÓW##### parametryVendora[1][0] 0 nie jest kluczem
#####SYSTEM QUESTÓW#####
#####GŁÓWNY MODUŁ#####

def LosowanieEnemy(InformacjeLokacji):
    print(InformacjeLokacji)
    if InformacjeLokacji[2][0] == 1:

        entity = entitylist[random.choice(["szkielet", "minotaur", "wilk"])]
        fight = 1
        return entity, fight

    
TekstyKowalCrosset = ['Tekst1','Tekst2','Tekst3']
def ParametryVendora1():
    Asortyment = {"zniszczona przeszywanica": itemlist["zniszczona przeszywanica"]["cena"], "naszyjnik z kości": itemlist["naszyjnik z kości"]["cena"], "zardzewiały miecz": itemlist["zardzewiały miecz"]["cena"]}
    ParametryVendora = [Asortyment, "Kowal Bożydar"]
    return ParametryVendora
NPCvendors = {'kowal bożydar': ParametryVendora1}
def WystępowanieNPC(itemlist, ParametryVendora, InformacjeLokacji, ekwipunek, ActionInput):
    if InformacjeLokacji[1][0] == 0 and InformacjeLokacji[1][1] == 0: # jeżeli npc ma występować jeszcze gdzieś, to piszemy "or" i kolejne koordynaty
        ParametryVendora = ParametryVendora1()
        print('W lokacji znajduje się:', ParametryVendora[1])
        if ActionInput.lower()[0:7] == "zagadaj":
            key = str(ActionInput.lower()[8:len(ActionInput.lower())])
            if key in NPCvendors.keys():
                answer = input(random.choice(TekstyKowalCrosset))
                if answer.lower() == "kup":
                    answer1 = input("Co byś chciał kupić kmiotku?\n")
                    key = answer1
                    if key in itemlist.keys():
                        if key.lower() in ParametryVendora[0].keys():
                            if "puste" in ekwipunek[4:9] and ekwipunek[10] >= ParametryVendora[0][key]:
                                for free_space in range(4, 9):
                                    if ekwipunek[free_space] == "puste":
                                        ekwipunek[free_space] = itemlist[key]
                                        ekwipunek[10] = ekwipunek[10] - itemlist[key]["cena"]
                                        print("Zakupino", itemlist[key]["name"].title(), "!")
                                        return ekwipunek
                            elif "puste" not in ekwipunek[4:9] and ekwipunek[10] >= ParametryVendora[0][key]:
                                print("Nie masz miejsca na przedmiot, który chcesz zakupić!")
                                return ekwipunek
                            elif "puste" in ekwipunek[4:9] and ekwipunek[10] < ParametryVendora[0][key]:
                                print("Nie stać cię na ten przedmiot kmiotku!")
                                return ekwipunek
                            elif "puste" not in ekwipunek[4:9] and ekwipunek[10] < ParametryVendora[0][key]:
                                print("Nie stać cię na ten przedmiot, ani nie masz na niego miejsca w ekwipunku, kmiotku!")
                                return ekwipunek
                        else:
                            print("Sprzedawca nie ma przedmiotu, który chcesz kupić!")
                            return ekwipunek
                    else:
                        print("Wybrany przedmiot nie istnieje!")
                        return ekwipunek




                elif answer.lower()[0:8] == "sprzedaj":
                    answer1 = input("Co byś chciał sprzedać, kmiotku?\n")
                    key = answer1.lower()
                    if key in itemlist.keys():
                            if itemlist[key] in ekwipunek[4:9]:
                                for item_position in range(4, 9):
                                    if ekwipunek[item_position] == itemlist[key]:
                                        ekwipunek[item_position] = "puste"
                                        ekwipunek[10] = ekwipunek[10] + itemlist[key]["cena"]
                                        print("Sprzedano", key.title(),"!")
                                        return ekwipunek
                                    else:
                                        continue

                            elif itemlist[key] in ekwipunek[0:4] or itemlist[key] == ekwipunek[9]:
                                print("Najpierw zdejmij przedmiot, który chcesz sprzedać!")
                            else:
                                print("Nie masz przedmiotu, który chcesz sprzedać!")

                    else:
                        print("Przedmiot, który chcesz sprzedać, nie istnieje!")




                else:
                    return None
            else:
                print('Nie ma tu nikogo takiego.')
fight = 0
def EnemyAttack(player,entity):
    enemyhitdirection = random.randint(1,4)
    if enemyhitdirection == 1:
        entitydmgvalue = entity.damage*2+random.randint(-5,5)-player.armorhead
        if entitydmgvalue > 0:
            print("Przeciwnik trafił cię w głowę i zadał {} obrażeń!".format(entitydmgvalue))
            player.HP -= entitydmgvalue
        if entitydmgvalue <= 0:
            print("Przeciwnik trafił cię w głowę, ale nie zadał żadnych obrażeń.")
    elif enemyhitdirection == 2:
        entitydmgvalue = entity.damage+random.randint(-5,5)-player.armortorso
        if entitydmgvalue > 0:
            print("Przeciwnik trafił cię w tors i zadał {} obrażeń!".format(entitydmgvalue))
            player.HP -= entitydmgvalue
        if entitydmgvalue <= 0:
            print("Przeciwnik trafił cię w tors, ale nie zadał żadnych obrażeń.")
    elif enemyhitdirection == 3:
        entitydmgvalue = entity.damage+random.randint(-5,5)-player.armorarms
        if entitydmgvalue > 0:
            print("Przeciwnik trafił cię w rękę i zadał {} obrażeń!".format(entitydmgvalue))
            player.HP -= entitydmgvalue
        if entitydmgvalue <= 0:
            print("Przeciwnik trafił cię w rękę, ale nie zadał żadnych obrażeń.")
    elif enemyhitdirection == 4:
        entitydmgvalue = entity.damage+random.randint(-5,5)-player.armorlegs
        if entitydmgvalue > 0:
            print("Przeciwnik trafił cię w nogę i zadał {} obrażeń!".format(entitydmgvalue))
            player.HP -= entitydmgvalue
        if entitydmgvalue <= 0:
            print("Przeciwnik trafił cię w nogę, ale nie zadał żadnych obrażeń.")
    return player, entity
    
def SystemWalki(player,entity,fight):
    while fight == 1:
        print("Na twojej drodze stoi {}, twój wróg posiada {} HP.".format(entity.entityname,entity.hp))
        print("Wybierz co chciałbyś zrobić.")
        print("Zaatakuj (Z), Atak Specjalny (X), Użyj Przedmiotów (C), Uciekaj (V)")
        PlayerChoice = input("[{}/{} HP] [{}/{} MP] [{} XP] [{} LVL] {}".format(player.HP,player.MaxHP,player.MP,player.MaxMP,player.XP,player.level,"\n")).lower()
        if PlayerChoice == "z" or PlayerChoice == "zaatakuj":
            playerdmgvalue = player.basedamage+random.randint(-5,5)-entity.armor
            playerdmgvalue = int(playerdmgvalue)
            if playerdmgvalue <= 0:
                print("Trafiłeś wroga, ale nie zadałeś mu żadnych obrażeń.")
            else:
                print("Trafiłeś wroga i zadałeś mu {} obrażeń.".format(playerdmgvalue))
                entity.hp -= playerdmgvalue
                if entity.hp <= 0:
                    result = 1
                    fight = 0
            if entity.hp > 0:
                EnemyAttack(player,entity)
            if player.HP <= 0:
                result = 2
                break
        elif PlayerChoice == "x" or PlayerChoice == "atak specjalny":
            if player.pclass == 1 and player.subclass == 1:
                print("Atak specjalny:")
                print("Silne uderzenie [1 MP] (Z)")
                print("Bitewny szał [5 MP] (X)")
                PlayerChoice = input("[{}/{} HP] [{}/{} MP] [{} XP] [{} LVL] {}".format(player.HP,player.MaxHP,player.MP,player.MaxMP,player.XP,player.level,"\n")).lower()
                if PlayerChoice == "z" and player.MP > 0:
                    player.MP -= 1
                    playerdmgvalue = player.basedamage*2-4+random.randint(-8,8)-entity.armor
                    playerdmgvalue = int(playerdmgvalue)
                    if playerdmgvalue <= 0:
                        print("Trafiłeś wroga, ale nie zadałeś mu żadnych obrażeń.")
                    else:
                        print("Trafiłeś wroga i zadałeś mu {} obrażeń.".format(playerdmgvalue))
                        entity.hp -= playerdmgvalue
                        if entity.hp <= 0:
                            result = 1
                            fight = 0
                    if entity.hp > 0:
                        EnemyAttack(player,entity)
                elif PlayerChoice == "z" and player.MP <= 0:
                    print("Nie masz wystarczająco many na ten atak.")
                elif PlayerChoice == "x" and player.MP > 0:
                    player.MP -= 5
                    playerdmgvalue = player.basedamage*2+random.randint(-10,10)-entity.armor*0.5
                    playerdmgvalue = int(playerdmgvalue)
                    if playerdmgvalue <= 0:
                        print("Trafiłeś wroga, ale nie zadałeś mu żadnych obrażeń.")
                    else:
                        print("Trafiłeś wroga i zadałeś mu {} obrażeń.".format(playerdmgvalue))
                        recoveredhp = int(playerdmgvalue/4)
                        print("Twój atak odnowił ci {} HP.".format(recoveredhp))
                        player.HP += recoveredhp
                        entity.hp -= playerdmgvalue
                        if entity.hp <= 0:
                            result = 1
                            fight = 0
                    print("Twój wróg nie zdążył zareagować na twoją dziką szarżę i nie zaatakował.")
                elif PlayerChoice == "x" and player.MP <= 0:
                    print("Nie masz wystarczająco many na ten atak.")
                else:
                    print("Nie posiadasz takiej możliwości ataku.")
            elif player.pclass == 2 and player.subclass == 1:
                print("Jeszcze nie zrobione.")
            elif player.pclass == 3 and player.subclass == 1:
                print("Jeszcze nie zrobione.")
        elif PlayerChoice == "c" or PlayerChoice == "użyj przedmiotów":
            print("Nie ma takiej opcji.")
        elif PlayerChoice == "v" or PlayerChoice == "uciekaj": 
            speedvalue = player.dex*2+player.int*0.5+player.str+player.end*2.5
            if speedvalue > entity.hp*3:
                print("Udało ci się uciec od wroga.")
                fight = 0
                result = 1
                break
            if speedvalue <= entity.hp*3:
                print("Nie byłeś wystarczająco szybki by uciec od wroga.")
        elif PlayerChoice == "gtfo":
            print("Udało ci się uciec od wroga.")
            fight = 0
            result = 2
            break
        elif PlayerChoice.lower() not in ('z','x','c','v','zaatakuj','atak specjalny','użyj przedmiotów','uciekaj','gtfo',):
            print("Coś źle wpisałeś.")
    if result == 2:
        print("Nie udało ci się pokonać wroga.")
        return player,entity,fight
    if result == 1:
        print("Pokonałeś swojego przeciwnika.")
        print("Otrzymałeś {} XP!".format(entity.xpreward))
        player.XP += entity.xpreward
        return player,entity,fight
def szkielet():
    entity = EntityStats("Szkielet", 10,10,10,[],5,2)
    return entity
def troll():
    entity = EntityStats("Troll", 10, 5, 6, [], 2, 5)
    return entity
def potezny_troll():
    entity = EntityStats("Potężny troll", 15,6,8,[],3,10)
    return entity
def gryf(): #### NAZWA DO ZMIANY, ZALEŻY OD PISARZY
    entity = EntityStats("Gryf", 20,5,6,[],9,0)
    return entity
def wilk():
    entity = EntityStats("Wilk", 10, 10, 10, [], 5, 2)
    return entity
def wilk_alfa():
    entity = EntityStats("Wilk Alfa", 15, 15, 5, [],10,3)
    return entity
def bagienny_potwor():
    entity = EntityStats("Bagienny potwór", 15,10,5,[],20,5)
    return entity
def minotaur():
    entity = EntityStats("Minotaur", 100, 50, 200, [], 20, 10)
    return entity
def wiesniak_w_kartonie():
    entity = EntityStats("Wieśniak w kartonie",5,2,2,[],5,1)
    return entity
def bandyta():
    entity = EntityStats("Bandyta", 5,3,4,[],6,3)
    return entity
entitylist = {"wilk":wilk(), "szkielet": szkielet(), "minotaur": minotaur(), "troll": troll(), "potężny troll": potezny_troll(),
              "gryf": gryf(), "wilk alfa": wilk_alfa(), "bagienny potwór": bagienny_potwor(), "wieśniak w kartonie": wiesniak_w_kartonie(),
              "bandyta": bandyta()}



akcja=['Zjedz','Użyj','Opis','Atakuj','Zagadaj']
OtherAction=['zjedz','użyj','opis','atakuj','zagadaj', 'ubierz', 'dobądź', 'zdejmij', 'schowaj', 'ekwipunek', 'weź']
ItemAction=['zjedz','użyj','opis','ubierz','dobądź','zdejmij','schowaj','ekwipunek']
DebugAction=['debug']
InformacjeLokacji = [[1,0,0,0],[0,0],[0,0]]
def ActInput(ActionInput):
    ActionInput = input().lower()
    return ActionInput
itemlist = items()
helmet = itemlist["pikelhauba"]
chestplate = itemlist["zbroja płytowa"]
legs = itemlist["nagolenniki"]
gloves = itemlist["skórzane rękawice"]
item1 = itemlist["jabłko"]
item2 = itemlist["eliksir życia"]
item3 = itemlist["potężny eliksir życia"]
item4 = "puste"
item5 = "puste"
amulet = itemlist["naszyjnik z kości"]
weapon = itemlist["brak broni"]
money = 50
ekwipunek = [helmet, chestplate, legs, gloves, item1, item2, item3, item4, item5, amulet, money, weapon]

    

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
entity = EntityStats("",0,0,0,[],0,0)
player = PlayerStats("",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100.0,100.0)
player.name = str(input("Powiedz jak się nazywasz podróżniku.")) #możecie to dać pod komentarzem jak przeszkadza
player.classchoice() #to też możecie dać pod komentarzem
ParametryVendora = [{0}, [0]] #lista1 = asortyment , lista2 = nazwa
while True:
    player.eqaddedstr = int(ekwipunek[0]["dodawana_siła"]+ekwipunek[1]["dodawana_siła"]+ekwipunek[2]["dodawana_siła"]+ekwipunek[3]["dodawana_siła"]+ekwipunek[9]["dodawana_siła"]+ekwipunek[11]["dodawana_siła"])
    player.eqaddeddex = int(ekwipunek[0]["odejmowana_zręczność"]+ekwipunek[1]["odejmowana_zręczność"]+ekwipunek[2]["odejmowana_zręczność"]+ekwipunek[3]["odejmowana_zręczność"]+ekwipunek[9]["dodawana_zręczność"])
    player.eqaddedint = int(ekwipunek[0]["dodawana_inteligencja"]+ekwipunek[1]["dodawana_inteligencja"]+ekwipunek[2]["dodawana_inteligencja"]+ekwipunek[3]["dodawana_inteligencja"]+ekwipunek[9]["dodawana_inteligencja"]+ekwipunek[11]["dodawana_inteligencja"])
    player.eqaddedend = int(ekwipunek[0]["dodawana_wytrzymałość"]+ekwipunek[1]["dodawana_wytrzymałość"]+ekwipunek[2]["dodawana_wytrzymałość"]+ekwipunek[3]["dodawana_wytrzymałość"]+ekwipunek[9]["dodawana_wytrzymałość"])
    player.eqaddedluck = int(ekwipunek[0]["dodawane_szczęście"]+ekwipunek[1]["dodawane_szczęście"]+ekwipunek[2]["dodawane_szczęście"]+ekwipunek[3]["dodawane_szczęście"]+ekwipunek[9]["dodawane_szczęście"]+ekwipunek[11]["dodawane_szczęście"])
    player.armortorso = (int(ekwipunek[1]["ochrona"]) / 2) + int(ekwipunek[3]["ochrona"])
    player.armorhead = int(ekwipunek[0]["ochrona"])
    player.armorlegs = int(ekwipunek[2]["ochrona"])
    player.calcstats()
    player.calcmaxhp()
    player.calcmaxmp()
    player.hpmpscaling()
    player.calcdamage()
    player.calclevel()
    items()
    itemlist = items()
    inventory(ekwipunek, ActionInput, itemlist, player)
    player.prevhpscaling()
    if player.HP > player.MaxHP:
        player.HP = player.MaxHP
    if player.MP > player.MaxMP:
        player.MP = player.MaxMP
    print() 
    ActionInput = input("[{}/{} HP] [{}/{} MP] [{} XP] [{} LVL] {}".format(player.HP,player.MaxHP,player.MP,player.MaxMP,player.XP,player.level,"\n")).lower()
    if ActionInput == "walcz" and entity.entityname != "":
        if entity.hp <= 0:
            print("Przeciwnik już jest martwy.")
            fight = 0
        if entity.hp > 0:
            fight = 1
            SystemWalki(player, entity, fight)
            player.prevhpscaling()
            player.hpmpscaling()
            if player.HP <= 0:
                print("Umarłeś.")
                break
    if ActionInput == "walcz" and entity.entityname == "":
        print("W tej lokacji nie ma żadnego przeciwnika.")
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

    if (InformacjeLokacji[1][0] == 0) and (InformacjeLokacji[1][1] == 0):
        WystępowanieNPC(itemlist, ParametryVendora, InformacjeLokacji, ekwipunek, ActionInput)
        entity = entitylist[random.choice(["szkielet", "wilk", "minotaur"])]
        InformacjeLokacji[0][0] = 1
        InformacjeLokacji[0][1] = 0
        InformacjeLokacji[0][2] = 0
        InformacjeLokacji[0][3] = 0
        InformacjeLokacji[2][0] = 1
        Lokacja1()
        
    if InformacjeLokacji[1][0] == 0 and InformacjeLokacji[1][1] == 1:
        WystępowanieNPC(itemlist, ParametryVendora, InformacjeLokacji, ekwipunek, ActionInput)
        LosowanieEnemy(InformacjeLokacji)
        InformacjeLokacji[0][0] = 0
        InformacjeLokacji[0][1] = 1
        InformacjeLokacji[0][2] = 0
        InformacjeLokacji[0][3] = 0
        InformacjeLokacji[2][0] = 0
        Lokacja2()
input()
