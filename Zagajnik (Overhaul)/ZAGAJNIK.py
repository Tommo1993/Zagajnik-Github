import time
import random
from data.locdesc import *
#from data.locdefs import *
#from data.enemydefs import *
#from data.enemylist import *
#from data.itemdefs import *
#from data.leveldefs import *
#from data.statdefs import PlayerStats
#from data.classdefs import ClassDefs

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
    return item.gold

def SzukanieMiejscaNaPrzedmiot(item, KoniecQuesta):
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
def ClassChoice(player,item,StartInput):		
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
        item.itemslotchest = [1,"Stary skórzany napierśnik","Jeszcze się trzyma...","armor","armorchest",0,0,0,0,0,0,0,0,0,0,0,0,0.1,0.1,0.05,0]
        item.itemslotlegs = [1,"Dziurawe włókniane spodnie","Więcej dziur niż nitek.","armor","armorlegs",0,0,0,0,0,0,0,0,0,0,0,0,0,0.05,0,0]
        item.itemslotfoot = [1,"Buty bez podeszwy","ochroniają podbicie stopy przed podmuchem wiatru!","armor","armorfoot",0,0,0,0,0,0,0,0,0,0,0,0,0.05,0.05,0.5,0]
        item.itemslotweapon1 = [1,"Drewniana pałka","W zasadzie grubszy kij.","weapon","mace",0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,3]
        item.inventoryslot1 = [1,2,"Bochenek Chleba","Czerstwy, ale da się zjeść.","consumable","food",4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        item.inventoryslot2 = [1,1,"Bukłak wody","Mmm... bardzo błotnista i prosto z bagna.","consumable","food",0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
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
    return player, item

#####GRACZ#####

#####WYDARZENIA#####
def EventHandler(LocMoveset,item,player,ActionInput,Loc7Moveset):
    if LocMoveset[5] == 1:
        print("Między kamyczkami na dnie widzisz mieniącą się złotą monetę")
        print("Czy chciałbyś ją podnieść? (Tak/Nie)")
        while ActionInput != "tak" or ActionInput != "nie":
            ActionInput = input().lower()
            if ActionInput == "tak":
                item.gold+=1
                print("Podniosłeś złotą monetę")
                print("Dodano: +1 Korona")
                ActionInput = ""
                LocMoveset[5] = 0
                Loc5Moveset[5] = 0
                return LocMoveset, item, player, ActionInput, MovementAction, Loc5Moveset
            if ActionInput == "nie":
                print("Postanawaiasz zostawić monetę w spokoju.")
                break
    if LocMoveset[5] == 2:
        while ActionInput != "tak" or ActionInput != "nie":
            ActionInput = input().lower()
            if ActionInput in MovementNorth:
                return LocMoveset, item, player, ActionInput, MovementAction, Loc5Moveset
            if ActionInput == "tak":
                print("...Mmmm... Cóż za soczysty zapach...")
                time.sleep(3)
                print("Giniesz krótko po tym gdy próbowałeś pocałować ogra.")
                print("Nawet taki zwierzoczłowiek ma jakieś podstawy moralne...")
                time.sleep(3)
                player.HP = 0
                LocMoveset[5] = 0
                return LocMoveset, item, player, ActionInput, MovementAction, Loc5Moveset
            if ActionInput == "nie":
                print('Dobry wybór Kmiotku.')
                print("Możesz spokojnie odejść...")
                LocMoveset[5] = 0
                break
    if LocMoveset[5] == 3:
        while ActionInput != "tak" or ActionInput != "nie":
            ActionInput = input().lower()
            if ActionInput in MovementEast:
                return LocMoveset, item, player, ActionInput, MovementAction, Loc5Moveset
            if ActionInput == "tak":
                print('...Powoli wsadzasz palec w żar...')
                time.sleep(2)
                print('Dziwnym przypadkiem po chwilowym bólu tracisz czucie w palcu...')
                time.sleep(2)
                print('Totalnie przypadkowo twój palec zostaje w ognisku.')
                time.sleep(2)
                strata = random.randint(1,3)
                player.HP -= strata
                print("Straciłeś",strata,"HP!")
                LocMoveset[5] = 0
                return LocMoveset, item, player, ActionInput, MovementAction, Loc5Moveset
            if ActionInput == "nie":
                print('Dobry wybór Kmiotku.')
                print("Możesz spokojnie odejść...")
                LocMoveset[5] = 0
                break
#####WYDARZENIA#####

#####GŁÓWNY MODUŁ#####
akcja=['North','South','East','West','n','s','w','e','Zjedz','Użyj','Opis','Atakuj','Zagadaj']
MovementAction=['north','n','south','s','east','e','west','w']
MovementNorth=['north','n']
MovementSouth=['south','s']
MovementEast=['east','e']
MovementWest=['west','w']
OtherAction=['zjedz','użyj','opis','atakuj','zagadaj', 'ubierz', 'dobądź', 'zdejmij', 'schowaj', 'ekwipunek', 'weź']
ItemAction=['zjedz','użyj','opis','ubierz','dobądź','zdejmij','schowaj','ekwipunek']
DebugAction=['debug','additem']
LocMoveset=[0,0,0,0,0,0]
Loc1Moveset=[2,0,0,0,0,0] #W kolejności North(0)/South(1)/East(2)/West(3)/Wróg w Lokacji(4)/Wydarzenie(5)
Loc2Moveset=[3,0,0,0,0,0]
Loc3Moveset=[0,2,4,9,0,0] #Skrzyżowanie
Loc4Moveset=[5,0,7,3,0,0] #0 = "Tam nie pójdziesz'
Loc5Moveset=[0,4,0,0,0,0] #Strumyk
#Loc6Moveset=[0,0,0,0] #Alternatywna wersja strumyka
Loc7Moveset=[0,8,0,4,0,1]
Loc8Moveset=[7,0,0,0,0,0] #Obóz ogrów w zagajniku
Loc9Moveset=[10,0,3,11,0,0]
Loc10Moveset=[12,9,0,0,0,0]
Loc11Moveset=[0,0,9,0,0,0] #Ognisko w Zagajniku
Loc12Moveset=[14,10,0,0,0,0] #Południowa brama Crosset
#Loc13Moveset=[0,0,0,0] #alternatywna wersja bramy
Loc14Moveset=[19,12,16,15,0,0] #skrzyzowanie crosset
Loc15Moveset=[20,0,14,0,0,0] #ulica pszenna crosset
Loc16Moveset=[17,0,21,14,0,0] #ulica targowa crosset
Loc17Moveset=[0,16,0,0,0,0] #zaułek
#Loc18Moveset=[0,0,0,0] #alternatywny zaułek
Loc19Moveset=[0,14,0,0,0,0] #wieża straznicza crosset
Loc20Moveset=[0,15,0,0,0,0] #piekarnia crosset
Loc21Moveset=[0,0,0,16,0,0] #kuźnia crosset


def ActInput(ActionInput):
    ActionInput = input().lower()
    return ActionInput
    
def LocMovesetCheck(Lokacja):
    if Lokacja == 1:
        LocMoveset=Loc1Moveset
    if Lokacja == 2:
        LocMoveset=Loc2Moveset
    if Lokacja == 3:
        LocMoveset=Loc3Moveset
    if Lokacja == 4:
        LocMoveset=Loc4Moveset
    if Lokacja == 5:
        LocMoveset=Loc5Moveset
    if Lokacja == 6:
        LocMoveset=Loc6Moveset
    if Lokacja == 7:
        LocMoveset=Loc7Moveset
    if Lokacja == 8:
        LocMoveset=Loc8Moveset
    if Lokacja == 9:
        LocMoveset=Loc9Moveset
    if Lokacja == 10:
        LocMoveset=Loc10Moveset
    if Lokacja == 11:
        LocMoveset=Loc11Moveset
    if Lokacja == 12:
        LocMoveset=Loc12Moveset
    if Lokacja == 13:
        LocMoveset=Loc13Moveset
    if Lokacja == 14:
        LocMoveset=Loc14Moveset
    if Lokacja == 15:
        LocMoveset=Loc15Moveset
    if Lokacja == 16:
        LocMoveset=Loc16Moveset
    if Lokacja == 17:
        LocMoveset=Loc17Moveset
    if Lokacja == 18:
        LocMoveset=Loc18Moveset
    if Lokacja == 19:
        LocMoveset=Loc19Moveset
    if Lokacja == 20:
        LocMoveset=Loc20Moveset
    if Lokacja == 21:
        LocMoveset=Loc21Moveset
    return LocMoveset
    

def ActionCheck(ActionInput,Lokacja,LocMoveset): #nie testowane, powiedzmy że działa
    #print(MovementAction)
    if ActionInput in MovementAction:
        if ActionInput in MovementNorth:
            #print(LocMoveset)
            #print(ActionInput)
            if LocMoveset[0] != 0:
                Lokacja=LocMoveset[0]
                #print(Lokacja)
                #return ActionInput, Lokacja, LocMoveset 
            if LocMoveset[0] == 0:
                print("Tam nie pójdziesz")
                #return ActionInput, Lokacja, LocMoveset
        if ActionInput in MovementSouth:
            if LocMoveset[1] != 0:
                Lokacja=LocMoveset[1]
            if LocMoveset[1] == 0:
                print("Tam nie pójdziesz")
        if ActionInput in MovementEast:
            if LocMoveset[2] != 0:
                Lokacja=LocMoveset[2]
            if LocMoveset[2] == 0:
                print("Tam nie pójdziesz")
        if ActionInput in MovementWest:
            if LocMoveset[3] != 0:
                Lokacja=LocMoveset[3]
            if LocMoveset[3] == 0:
                print("Tam nie pójdziesz")
    if ActionInput in OtherAction:
        if ActionInput in ItemAction:
            print("przeniesione")
    if ActionInput in DebugAction:
        if ActionInput == 'debug':
            print("Jakieś dane tu się będą pokazywać")
     #NIŻEJ ZMIENIŁEM or NA and   
    if (ActionInput not in MovementAction) and (ActionInput not in OtherAction) and (ActionInput not in DebugAction) and (ActionInput != "questy"):
        print("???")
    return ActionInput, Lokacja, LocMoveset

#def LocDescCheck(Lokacja):
def LocDescCheck(Lokacja, DaneWszystkichQuestów):
    if Lokacja == 1:
        loc1()
    if Lokacja == 2:
        loc2()
    if Lokacja == 3:
        loc3()
    if Lokacja == 4:
        loc4()
    if Lokacja == 5:
        loc5()
    if Lokacja == 6:
        loc6()
    if Lokacja == 7:
        loc7()
    if Lokacja == 8:
        loc8()
    if Lokacja == 9:
        loc9()
    if Lokacja == 10:
        loc10()
    if Lokacja == 11:
        loc11()
    if Lokacja == 12 and DaneWszystkichQuestów[1][0] == 0:
        DaneWszystkichQuestów[1][0] = 1
        loc13()
        print()
        print('Otrzymano zadanie: Miejscowy Bohater')
        print()
    if Lokacja == 12 and DaneWszystkichQuestów[1][0] == 1 or DaneWszystkichQuestów[1][0] == 3:
        loc12()
    #if Lokacja == 13:
        #loc13()
    if Lokacja == 14:
        loc14()
    if Lokacja == 15:
        loc15()
    if Lokacja == 16:
        loc16()
    if Lokacja == 17:
        loc17()
    if Lokacja == 18:
        loc18()
    if Lokacja == 19:
        loc19()
    if Lokacja == 20:
        loc20()
    if Lokacja == 21:
        loc21()
    return None #nic nie zwraca, tylko generuje opis 
#####GŁÓWNY MODUŁ#####
    
clear = "\n" * 100
def clear():
    print(clear)

ActionInput = ""
player = PlayerStats(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)

#Staty = PlayerStats("edgy", 100, 20, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
#Staty.PlayerName()
#print(Staty.StatDisplay())
start = 0
if start == 0:
    print("###############################################################")
    print()
    print("               Mikołaj, Tomek i Gruby prezentują...")
    time.sleep(1)
    print()
    print("                            ZAGAJNIK")
    print()
    time.sleep(1)
    print("###############################################################")
    print()
    print("Nowa Gra   -   Kontynuuj   -   Wczytaj   -   Opcje   -   Wyjdź")
    print()
    print()
while start == 0:
    StartInput = input().lower()
    if StartInput == "nowa gra":
        Lokacja = 1
        start = 1
        xyz = 1
        xxx = ["zbrojny","1","zwiadowca","2","łotr","3"]
        while xyz == 1:
            print("Wybierz swoją klasę...")
            print("Zbrojny (1), zwiadowca (2), łotr (3)...")
            StartInput = input().lower()
            ClassChoice(player,item,StartInput)
            if StartInput in xxx:
                xyz = 0
    if StartInput == "kontynuuj":
        print("Czy na pewno chcesz kontunuować swoje cierpienie?")
    if StartInput == "wczytaj":
        print("Jak zrobisz zapisywanie to pogadamy!")
    if StartInput == "opcje":
        print("Masz dwie opcje: gułag albo śmierć!")
    if StartInput == "wyjdź":
        break
    print()
    

Lokacja = 1
DaneWszystkichQuestów=Questy()
#print(DaneWszystkichQuestów)
#print()
while Lokacja != 0 and start == 1: #lokacja 0 to GAME OVER
    #LocDescCheck(Lokacja)
    LocDescCheck(Lokacja,DaneWszystkichQuestów)
    LocMoveset=LocMovesetCheck(Lokacja)
    if LocMoveset[4] != 0 or LocMoveset[5] != 0:
        EventHandler(LocMoveset,item,player,ActionInput,MovementAction,Loc7Moveset)
        if player.HP <= 0:
            Lokacja = 0
        if ActionInput not in MovementAction:
            ActionInput = input().lower()
    if LocMoveset[5] == 0 and LocMoveset[4] == 0:
        ActionInput = input().lower()
    
    #to zmieniłem i TO JEST KLUCZOWE:
    (ActionInput,Lokacja,LocMoveset)=ActionCheck(ActionInput,Lokacja,LocMoveset)
    
    
    if ActionInput == 'questy':
        if DaneWszystkichQuestów[1][0] == 1:
            print()
            print('Nazwa: {}'.format(DaneWszystkichQuestów[1][1]))
            print('Opis: {}'.format(DaneWszystkichQuestów[1][2]))
            print('Zleceniodawca: {}'.format(DaneWszystkichQuestów[1][3]))
        print()
        if DaneWszystkichQuestów[1][0] == 0 or DaneWszystkichQuestów[1][0] == 3:
            print('Nie masz żadnych zadań!')
            print()
            
            
            
       
        
            
        

    

    
