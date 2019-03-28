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
akcja=['North','South','East','West','n','s','w','e','Zjedz','Użyj','Opis','Atakuj','Zagadaj']
MovementAction=['north','n','south','s','east','e','west','w']
MovementNorth=['north','n']
MovementSouth=['south','s']
MovementEast=['east','e']
MovementWest=['west','w']
OtherAction=['zjedz','użyj','opis','atakuj','zagadaj', 'ubierz', 'dobądź', 'zdejmij', 'schowaj', 'ekwipunek']
LocMoveset=[0,0,0,0]
Loc1Moveset=[2,0,0,0] #W kolejności North(0)/South(1)/East(2)/West(3)
Loc2Moveset=[3,0,0,0]
Loc3Moveset=[0,2,4,9] #Skrzyżowanie
Loc4Moveset=[5,0,7,3] #0 = "Tam nie pójdziesz'
Loc5Moveset=[0,4,0,0] #Strumyk
#Loc6Moveset=[0,0,0,0] #Alternatywna wersja strumyka
Loc7Moveset=[0,8,0,4]
Loc8Moveset=[7,0,0,0] #Obóz ogrów w zagajniku
Loc9Moveset=[10,0,3,11]
Loc10Moveset=[12,9,0,0]
Loc11Moveset=[0,0,9,0] #Ognisko w Zagajniku
Loc12Moveset=[14,10,0,0] #Południowa brama Crosset
#Loc13Moveset=[0,0,0,0] #alternatywna wersja bramy
Loc14Moveset=[19,12,16,15] #skrzyzowanie crosset
Loc15Moveset=[20,0,14,0] #ulica pszenna crosset
Loc16Moveset=[17,0,21,14] #ulica targowa crosset
Loc17Moveset=[0,16,0,0] #zaułek
#Loc18Moveset=[0,0,0,0] #alternatywny zaułek
Loc19Moveset=[0,14,0,0] #wieża straznicza crosset
Loc20Moveset=[0,15,0,0] #piekarnia crosset
Loc21Moveset=[0,0,0,16] #kuźnia crosset


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
#    if ActionInput in OtherAction:
     #NIŻEJ ZMIENIŁEM or NA and   
    if (ActionInput not in MovementAction) and (ActionInput not in OtherAction):
        print("???")
    return ActionInput, Lokacja, LocMoveset

def LocDescCheck(Lokacja):
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
    if Lokacja == 12:
        loc12()
    if Lokacja == 13:
        loc13()
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
    


ActionInput = ""
start = 1
Lokacja = 1
while Lokacja != 0: #lokacja 0 to GAME OVER
    
    LocDescCheck(Lokacja)
    LocMoveset=LocMovesetCheck(Lokacja)
    ActionInput = input().lower()
    #to zmieniłem i TO JEST KLUCZOWE:
    (ActionInput, Lokacja, LocMoveset)=ActionCheck(ActionInput,Lokacja,LocMoveset)
    

    
