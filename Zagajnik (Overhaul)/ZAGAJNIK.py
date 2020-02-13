import time
import random
from time import sleep
from data.player import *
##### EKWIPUNEK ######
# WSZYSTKIE ITEMY BĘDĄ OPISANE W FORMIE SłOWNIKÓW : ITEM = {"name": nazwa_przedmiotu, "type": typ_przedmiotu, "doIhave": True/False (kolejne statystyki)}
from data.itemdefs import items
from data.inventory import inventory
from data.skrypt_wykazu_itemow import wykaz_itemow
from data.entity import *

wykaz_itemow()
itemlist = items()
#####SYSTEM QUESTÓW##### parametryVendora[1][0] 0 nie jest kluczem
#####SYSTEM QUESTÓW#####
#####GŁÓWNY MODUŁ#####

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
def SystemWalki(player,entity,fight):
    while fight == 1:
        print("Na twojej drodze stoi {}, twój wróg posiada {} HP.".format(entity.entityname,entity.hp))
        print("Wybierz co chciałbyś zrobić.")
        print("Zaatakuj (Z), Atak Specjalny (X), Użyj Przedmiotów (C), Uciekaj (V)")
        PlayerChoice = input("[{} HP] [{} MP] [{} XP] [{} LVL] {}".format(player.HP,player.MP,player.XP,player.level,"\n")).lower()
        if PlayerChoice == "z" or PlayerChoice == "zaatakuj":
            playerdmgvalue = player.basedamage+random.randint(-5,5)-entity.armor
            if playerdmgvalue <= 0:
                print("Trafiłeś wroga, ale nie zadałeś mu żadnych obrażeń.")
            else:
                print("Trafiłeś wroga i zadałeś mu {} obrażeń.".format(playerdmgvalue))
                entity.hp -= playerdmgvalue
                if entity.hp <= 0:
                    result = 1
                    fight = 0
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
            if player.HP <= 0:
                result = 2
                break
        elif PlayerChoice == "x" or PlayerChoice == "atak specjalny":
            print("Jeszcze tego nie ma.")
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
        elif PlayerChoice not in ('z','x','c','v','zaatakuj','atak specjalny','użyj przedmiotów','uciekaj','gtfo'):
            print("Coś źle wpisałeś.")
    if result == 2:
        print("Nie udało ci się pokonać wroga.")
        return player,entity,fight
    if result == 1:
        print("Pokonałeś swojego przeciwnika.")
        print("Otrzymałeś {} XP!".format(entity.xpreward))
        player.XP += entity.xpreward
        return player,entity,fight

entity = EntityStats("kukła treningowa",20,5,10,0,2,2)
def szkielet(entity):
    entity.hp = 5
    entity.armor = 0
    entity.damage = 3
    entity.entityname = "Szkielet"
    #entity.loottable = [itemlist["jabłko"], itemlist["naszyjnik z kości"]]
    entity.mp = 5
    entity.xpreward = 20
def troll(entity):
    entity.hp = 20
    entity.armor = 5
    entity.damage = 10
    entity.entityname = "Troll"
    #entity.loottable = [itemlist["eliksir many"]]
    entity.mp = 20
    entity.xpreward = 50
def potezny_troll(entity):
    entity.hp = 40
    entity.armor = 25
    entity.damage = 15
    entity.entityname = "Potęzny troll"
    #entity.loottable = [itemlist["potężny eliksir many"]]
    entity.mp = 20
    entity.xpreward = 70
def gryf(entity): #### NAZWA DO ZMIANY, ZALEŻY OD PISARZY
    entity.hp = 30
    entity.armor = 0
    entity.damage = 20
    entity.entityname = "Gryf"
    #entity.loottable = [itemlist["Potężny eliksir życia"]] #### PLUS TA SKORUPKA OPISANA W FABULE, TRZEBA COŚ WYMYŚLIć
    entity.mp = 30
    entity.xpreward = 40
def wilk(entity):
    entity.hp = 10
    entity.armor = 0
    entity.damage = 8
    entity.entityname = "Wilk"
    #entity.loottable = [itemlist["mięso z wilka"]] #### PLUS OPISANA W FABULE SKÓRA
    entity.mp = 30
    entity.xpreward = 40
def wilk_alfa(entity):
    entity.hp = 30
    entity.armor = 5
    entity.damage = 12
    entity.entityname = "Wilk Alfa"
    #entity.loottable = [itemlist["mięso z wilka"], itemlist["skóra wilka"]]
    entity.mp = 35
    entity.xpreward = 60
def bagienny_potwor(entity):
    entity.hp = 60
    entity.armor = 15
    entity.damage = 15
    entity.entityname = "Potwór z bagien"
    #entity.loottable = [itemlist["Potężny eliksir życia"], itemlist["Potęzny eliksir many"], itemlist["królicza łapka"]]
    entity.mp = 40
    entity.xpreward = 150
def minotaur(entity):
    entity.hp = 200
    entity.armor = 30
    entity.damage = 25
    entity.entityname = "Potężny Minotaur"
    #entity.loottable = []  #### KLUCZ OPISANY W FABULE
    entity.mp = 60
    entity.xpreward = 300
def wiesniak_w_kartonie(entity):
    entity.hp = 15
    entity.armor = 6
    entity.damage = 10
    entity.entityname = "Wieśniak w kartonie"
    #entity.loottable = [itemlist["zniszczona przeszywanica"], itemlist["skórzane spodnie"]] #### PLUS JAKAŚ BROń
    entity.mp = 10
    entity.xpreward = 15
def bandyta(entity):
    entity.hp = 20
    entity.armor = 10
    entity.damage = 15
    entity.entityname = "Bandyta"
    #entity.loottable = [itemlist["Potężny eliksir życia"]]  #### PLUS TA SKORUPKA OPISANA W FABULE, TRZEBA COŚ WYMYŚLIć
    entity.mp = 20
    entity.xpreward = 30
#entitylist = {"szkielet": szkielet(entity), "troll": troll(entity), "potężny troll": potezny_troll(entity), "gryf": gryf(entity), "wilk": wilk(entity),
#              "wilk alfa": wilk_alfa(entity), "bagienny potwór": bagienny_potwor(entity), "minotaur": minotaur(entity), "wieśniak w kartonie":
#                  wiesniak_w_kartonie(entity), "bandyta": bandyta(entity)}    
akcja=['Zjedz','Użyj','Opis','Atakuj','Zagadaj']
OtherAction=['zjedz','użyj','opis','atakuj','zagadaj', 'ubierz', 'dobądź', 'zdejmij', 'schowaj', 'ekwipunek', 'weź']
ItemAction=['zjedz','użyj','opis','ubierz','dobądź','zdejmij','schowaj','ekwipunek']
DebugAction=['debug']
InformacjeLokacji = [[1,0,0,0],[0,0]]
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
money = 10
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
    player.prevhpscaling()
    print() #TEMP FIX
    ActionInput = input("[{} HP] [{} MP] [{} XP] [{} LVL] {}".format(player.HP,player.MP,player.XP,player.level,"\n")).lower()
    if ActionInput == "walcz":
        fight = 1
        SystemWalki(player,entity,fight)
        player.prevhpscaling()
        player.hpmpscaling()
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

    if (InformacjeLokacji[1][0] == 0) and (InformacjeLokacji[1][1] == 0):
        WystępowanieNPC(itemlist, ParametryVendora, InformacjeLokacji, ekwipunek, ActionInput)
        InformacjeLokacji[0][0] = 1
        InformacjeLokacji[0][1] = 0
        InformacjeLokacji[0][2] = 0
        InformacjeLokacji[0][3] = 0
        Lokacja1()
        
    if InformacjeLokacji[1][0] == 0 and InformacjeLokacji[1][1] == 1:
        WystępowanieNPC(itemlist, ParametryVendora, InformacjeLokacji, ekwipunek, ActionInput)
        InformacjeLokacji[0][0] = 0
        InformacjeLokacji[0][1] = 1
        InformacjeLokacji[0][2] = 0
        InformacjeLokacji[0][3] = 0
        Lokacja2()
        



                


                      
            

        
            
        

    

    
