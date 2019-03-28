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
#####EKWIPUNEK#####
class Inventory:
    def __init__(item, gold, X, itemslotactive1, itemslotactive2, itemslotactive3, itemslotactive4, itemslotactive5, itemslotactive6, itemslotweapon1, itemslotweapon2, itemslothead, itemslotchest, itemslotarms, itemslothands, itemslotlegs, itemslotfoot, itemslotacc1, itemslotacc2, itemslotacc3, inventoryslot1, inventoryslot2, inventoryslot3, inventoryslot4, inventoryslot5, inventoryslot6, inventoryslot7, inventoryslot8, inventoryslot9, inventoryslot10, assignmentinvslot):
        item.gold=0
        item.X=0
        item.itemslotactive1=itemslotactive1
        item.itemslotactive2=itemslotactive2
        item.itemslotactive3=itemslotactive3
        item.itemslotactive4=itemslotactive4
        item.itemslotactive5=itemslotactive5
        item.itemslotactive6=itemslotactive6 
        item.itemslotweapon1=itemslotweapon1
        item.itemslotweapon2=itemslotweapon2
        item.itemslothead=itemslothead
        item.itemslotchest=itemslotchest
        item.itemslotarms=itemslotarms
        item.itemslothands=itemslothands
        item.itemslotlegs=itemslotlegs
        item.itemslotfoot=itemslotfoot
        item.itemslotacc1=itemslotacc1
        item.itemslotacc2=itemslotacc2
        item.itemslotacc3=itemslotacc3
        item.inventoryslot1=inventoryslot1
        item.inventoryslot2=inventoryslot2 
        item.inventoryslot3=inventoryslot3 
        item.inventoryslot4=inventoryslot4 
        item.inventoryslot5=inventoryslot5 
        item.inventoryslot6=inventoryslot6 
        item.inventoryslot7=inventoryslot7
        item.inventoryslot8=inventoryslot8
        item.inventoryslot9=inventoryslot9
        item.inventoryslot10=inventoryslot10
        item.assignmentinvslot=assignmentinvslot
def defineinventory(item):
    item.itemslotactive1=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0] #sloty ekwipunku (indeksy):
    item.itemslotactive2=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0] #slot 0 = czy jakiś przedmiot tam jest,
    item.itemslotactive3=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0] #slot 1 = nazwa, slot 2 = opis, slot 3 = typ, slot 4 = podtyp,
    item.itemslotactive4=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0] #slot 5 = +hp, slot 6 = +mp, slot 7 = maxhp, slot 8 = maxmp,
    item.itemslotactive5=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0] #slot 9 = +exp, slot 10 = str, slot 11 = dex, slot 12 = int
    item.itemslotactive6=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0] #slot 13 = end, slot 14 = luck, slot 15 = weapon dmg, slot 16 = ID
    item.itemslotweapon1=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
    item.itemslotweapon2=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
    item.itemslothead=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
    item.itemslotchest=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
    item.itemslotarms=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
    item.itemslothands=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
    item.itemslotlegs=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
    item.itemslotfoot=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
    item.itemslotacc1=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
    item.itemslotacc2=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
    item.itemslotacc3=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
    item.inventoryslot1=[0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0] #sloty ekwipunku (indeksy):
    item.inventoryslot2=[0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0] #slot 0 = czy jakiś przedmiot tam jest, slot 1 = ilość,
    item.inventoryslot3=[0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0] #slot 2 = nazwa, slot 3 = opis, slot 4 = typ, slot 5 = podtyp,
    item.inventoryslot4=[0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0] #slot 6 = +hp, slot 7 = +mp, slot 8 = maxhp, slot 9 = maxmp,
    item.inventoryslot5=[0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0] #slot 10 = +exp, slot 11 = str, slot 12 = dex, slot 13 = int
    item.inventoryslot6=[0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0] #slot 14 = end, slot 15 = luck, slot 16 = weapon dmg, slot 17 = ID
    item.inventoryslot7=[0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
    item.inventoryslot8=[0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
    item.inventoryslot9=[0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
    item.inventoryslot10=[0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
    item.assignmentinvslot=[0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
    return item
def itemuse(lookforinv,ActionInput):
    if ActionInput == 'zjedz':
        print("Co chciałbyś zjeść?")
        ActionInput = input().lower()
        lookforinv="food"
        return ActionInput, lookforinv
    if ActionInput == 'użyj':
        print("Co chciałbyś użyć?")
        ActionInput = input().lower()
        lookforinv="consumable"
        return ActionInput, lookforinv
    if ActionInput == 'opis':
        print("O którym przedmiocie chcesz wiedzieć więcej?")
        ActionInput = input().lower()
        lookforinv="desc"
        return ActionInput, lookforinv
    if ActionInput == 'ubierz':
        print("Co chciałbyś ubrać na siebię?")
        ActionInput = input().lower()
        lookforinv="armor"
        return ActionInput, lookforinv
    if ActionInput == 'dobądź':
        print("Jaką broń chciałbyś dobyć?")
        ActionInput = input().lower()
        lookforinv="weapon"
        return ActionInput, lookforinv
    if ActionInput == 'zdejmij':
        print("Co chciałbyś zdjąć z siebie?")
        ActionInput = input().lower()
        lookforinv="armoroff"
        return ActionInput, lookforinv
    if ActionInput == 'schowaj':
        print("Jaką broń chciałbyś schować?")
        ActionInput = input().lower()
        lookforinv="weaponoff"
        return ActionInput, lookforinv
    if ActionInput == 'upuść':
        print("Jaki przedmiot chciałbyś upuścić? Tej akcji nie można cofnąć! (Wybierz przedmiot nie używany przez ciebię)")
        ActionInput = input().lower()
        return ActionInput
    if ActionInput == 'ekwipunek':
        lookforinvtype(ActionInput)
        
def lookforinventory(lookforinv,ActionInput,item): #do zrobienia
    if lookforinv == "food":
        if (item.inventoryslot1[4] == lookforinv) and (item.inventoryslot1[2] == ActionInput):
            if item.inventoryslot1[0] == 1:
                player.HP+=item.inventoryslot1[6]
                player.MP+=item.inventoryslot1[7]
                if item.inventoryslot1[1] > 1:
                    item.inventoryslot1[1]-=1
                if item.inventoryslot1[1] == 1:
                    item.inventoryslot1[0] = 0
        if (item.inventoryslot2[4] == lookforinv) and (item.inventoryslot2[2] == ActionInput):
            if item.inventoryslot2[0] == 1:
                player.HP+=item.inventoryslot2[6]
                player.MP+=item.inventoryslot2[7]
                if item.inventoryslot2[1] > 1:
                    item.inventoryslot2[1]-=1
                if item.inventoryslot2[1] == 1:
                    item.inventoryslot2[0] = 0
        if (item.inventoryslot3[4] == lookforinv) and (item.inventoryslot3[2] == ActionInput):
            if item.inventoryslot3[0] == 1:
                player.HP+=item.inventoryslot3[6]
                player.MP+=item.inventoryslot3[7]
                if item.inventoryslot3[1] > 1:
                    item.inventoryslot3[1]-=1
                if item.inventoryslot3[1] == 1:
                    item.inventoryslot3[0] = 0
        if (item.inventoryslot4[4] == lookforinv) and (item.inventoryslot4[2] == ActionInput):
            if item.inventoryslot4[0] == 1:
                player.HP+=item.inventoryslot4[6]
                player.MP+=item.inventoryslot4[7]
                if item.inventoryslot4[1] > 1:
                    item.inventoryslot4[1]-=1
                if item.inventoryslot4[1] == 1:
                    item.inventoryslot4[0] = 0
        if (item.inventoryslot5[4] == lookforinv) and (item.inventoryslot5[2] == ActionInput):
            if item.inventoryslot5[0] == 1:
                player.HP+=item.inventoryslot5[6]
                player.MP+=item.inventoryslot5[7]
                if item.inventoryslot5[1] > 1:
                    item.inventoryslot5[1]-=1
                if item.inventoryslot5[1] == 1:
                    item.inventoryslot5[0] = 0
        if (item.inventoryslot6[4] == lookforinv) and (item.inventoryslot6[2] == ActionInput):
            if item.inventoryslot6[0] == 1:
                player.HP+=item.inventoryslot6[6]
                player.MP+=item.inventoryslot6[7]
                if item.inventoryslot6[1] > 1:
                    item.inventoryslot6[1]-=1
                if item.inventoryslot6[1] == 1:
                    item.inventoryslot6[0] = 0
        if (item.inventoryslot7[4] == lookforinv) and (item.inventoryslot7[2] == ActionInput):
            if item.inventoryslot7[0] == 1:
                player.HP+=item.inventoryslot7[6]
                player.MP+=item.inventoryslot7[7]
                if item.inventoryslot7[1] > 1:
                    item.inventoryslot7[1]-=1
                if item.inventoryslot7[1] == 1:
                    item.inventoryslot7[0] = 0
        if (item.inventoryslot8[4] == lookforinv) and (item.inventoryslot8[2] == ActionInput):
            if item.inventoryslot8[0] == 1:
                player.HP+=item.inventoryslot8[6]
                player.MP+=item.inventoryslot8[7]
                if item.inventoryslot8[1] > 1:
                    item.inventoryslot8[1]-=1
                if item.inventoryslot8[1] == 1:
                    item.inventoryslot8[0] = 0
        if (item.inventoryslot9[4] == lookforinv) and (item.inventoryslot9[2] == ActionInput):
            if item.inventoryslot9[0] == 1:
                player.HP+=item.inventoryslot9[6]
                player.MP+=item.inventoryslot9[7]
                if item.inventoryslot9[1] > 1:
                    item.inventoryslot9[1]-=1
                if item.inventoryslot9[1] == 1:
                    item.inventoryslot9[0] = 0
        if (item.inventoryslot10[4] == lookforinv) and (item.inventoryslot10[2] == ActionInput):
            if item.inventoryslot10[0] == 1:
                player.HP+=item.inventoryslot10[6]
                player.MP+=item.inventoryslot10[7]
                if item.inventoryslot10[1] > 1:
                    item.inventoryslot10[1]-=1
                if item.inventoryslot10[1] == 1:
                    item.inventoryslot10[0] = 0
        
    if lookforinv == "consumable":
        print()
        
    if lookforinv == "armor": #do zrobienia
        if (item.inventoryslot1[4] == lookforinv) and (item.inventoryslot1[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot1
            if item.inventoryslot1[5] == 'armorhead':
                item.itemslothead[0] = item.assignmentinvslot[0]
                item.itemslothead[1] = item.assignmentinvslot[2]
                item.itemslothead[2] = item.assignmentinvslot[3]
                item.itemslothead[3] = item.assignmentinvslot[4]
                item.itemslothead[4] = item.assignmentinvslot[5]
                item.itemslothead[5] = item.assignmentinvslot[6]
                item.itemslothead[6] = item.assignmentinvslot[7]
                item.itemslothead[7] = item.assignmentinvslot[8]
                item.itemslothead[8] = item.assignmentinvslot[9]
                item.itemslothead[9] = item.assignmentinvslot[10]
                item.itemslothead[10] = item.assignmentinvslot[11]
                item.itemslothead[11] = item.assignmentinvslot[12]
                item.itemslothead[12] = item.assignmentinvslot[13]
                item.itemslothead[13] = item.assignmentinvslot[14]
                item.itemslothead[14] = item.assignmentinvslot[15]
                item.itemslothead[15] = item.assignmentinvslot[16]
                item.itemslothead[16] = item.assignmentinvslot[17]
            if item.inventoryslot1[5] == 'armorchest':
                item.itemslotchest[0] = item.assignmentinvslot[0]
                item.itemslotchest[1] = item.assignmentinvslot[2]
                item.itemslotchest[2] = item.assignmentinvslot[3]
                item.itemslotchest[3] = item.assignmentinvslot[4]
                item.itemslotchest[4] = item.assignmentinvslot[5]
                item.itemslotchest[5] = item.assignmentinvslot[6]
                item.itemslotchest[6] = item.assignmentinvslot[7]
                item.itemslotchest[7] = item.assignmentinvslot[8]
                item.itemslotchest[8] = item.assignmentinvslot[9]
                item.itemslotchest[9] = item.assignmentinvslot[10]
                item.itemslotchest[10] = item.assignmentinvslot[11]
                item.itemslotchest[11] = item.assignmentinvslot[12]
                item.itemslotchest[12] = item.assignmentinvslot[13]
                item.itemslotchest[13] = item.assignmentinvslot[14]
                item.itemslotchest[14] = item.assignmentinvslot[15]
                item.itemslotchest[15] = item.assignmentinvslot[16]
                item.itemslotchest[16] = item.assignmentinvslot[17]
            if item.inventoryslot1[5] == 'armorarms':
                item.itemslotarms[0] = item.assignmentinvslot[0]
                item.itemslotarms[1] = item.assignmentinvslot[2]
                item.itemslotarms[2] = item.assignmentinvslot[3]
                item.itemslotarms[3] = item.assignmentinvslot[4]
                item.itemslotarms[4] = item.assignmentinvslot[5]
                item.itemslotarms[5] = item.assignmentinvslot[6]
                item.itemslotarms[6] = item.assignmentinvslot[7]
                item.itemslotarms[7] = item.assignmentinvslot[8]
                item.itemslotarms[8] = item.assignmentinvslot[9]
                item.itemslotarms[9] = item.assignmentinvslot[10]
                item.itemslotarms[10] = item.assignmentinvslot[11]
                item.itemslotarms[11] = item.assignmentinvslot[12]
                item.itemslotarms[12] = item.assignmentinvslot[13]
                item.itemslotarms[13] = item.assignmentinvslot[14]
                item.itemslotarms[14] = item.assignmentinvslot[15]
                item.itemslotarms[15] = item.assignmentinvslot[16]
                item.itemslotarms[16] = item.assignmentinvslot[17]    
            if item.inventoryslot1[5] == 'armorhands':
                item.itemslothands[0] = item.assignmentinvslot[0]
                item.itemslothands[1] = item.assignmentinvslot[2]
                item.itemslothands[2] = item.assignmentinvslot[3]
                item.itemslothands[3] = item.assignmentinvslot[4]
                item.itemslothands[4] = item.assignmentinvslot[5]
                item.itemslothands[5] = item.assignmentinvslot[6]
                item.itemslothands[6] = item.assignmentinvslot[7]
                item.itemslothands[7] = item.assignmentinvslot[8]
                item.itemslothands[8] = item.assignmentinvslot[9]
                item.itemslothands[9] = item.assignmentinvslot[10]
                item.itemslothands[10] = item.assignmentinvslot[11]
                item.itemslothands[11] = item.assignmentinvslot[12]
                item.itemslothands[12] = item.assignmentinvslot[13]
                item.itemslothands[13] = item.assignmentinvslot[14]
                item.itemslothands[14] = item.assignmentinvslot[15]
                item.itemslothands[15] = item.assignmentinvslot[16]
                item.itemslothands[16] = item.assignmentinvslot[17]   
            if item.inventoryslot1[5] == 'armorlegs':
                item.itemslotlegs[0] = item.assignmentinvslot[0]
                item.itemslotlegs[1] = item.assignmentinvslot[2]
                item.itemslotlegs[2] = item.assignmentinvslot[3]
                item.itemslotlegs[3] = item.assignmentinvslot[4]
                item.itemslotlegs[4] = item.assignmentinvslot[5]
                item.itemslotlegs[5] = item.assignmentinvslot[6]
                item.itemslotlegs[6] = item.assignmentinvslot[7]
                item.itemslotlegs[7] = item.assignmentinvslot[8]
                item.itemslotlegs[8] = item.assignmentinvslot[9]
                item.itemslotlegs[9] = item.assignmentinvslot[10]
                item.itemslotlegs[10] = item.assignmentinvslot[11]
                item.itemslotlegs[11] = item.assignmentinvslot[12]
                item.itemslotlegs[12] = item.assignmentinvslot[13]
                item.itemslotlegs[13] = item.assignmentinvslot[14]
                item.itemslotlegs[14] = item.assignmentinvslot[15]
                item.itemslotlegs[15] = item.assignmentinvslot[16]
                item.itemslotlegs[16] = item.assignmentinvslot[17]    
            if item.inventoryslot1[5] == 'armorfoot':
                item.itemslotfoot[0] = item.assignmentinvslot[0]
                item.itemslotfoot[1] = item.assignmentinvslot[2]
                item.itemslotfoot[2] = item.assignmentinvslot[3]
                item.itemslotfoot[3] = item.assignmentinvslot[4]
                item.itemslotfoot[4] = item.assignmentinvslot[5]
                item.itemslotfoot[5] = item.assignmentinvslot[6]
                item.itemslotfoot[6] = item.assignmentinvslot[7]
                item.itemslotfoot[7] = item.assignmentinvslot[8]
                item.itemslotfoot[8] = item.assignmentinvslot[9]
                item.itemslotfoot[9] = item.assignmentinvslot[10]
                item.itemslotfoot[10] = item.assignmentinvslot[11]
                item.itemslotfoot[11] = item.assignmentinvslot[12]
                item.itemslotfoot[12] = item.assignmentinvslot[13]
                item.itemslotfoot[13] = item.assignmentinvslot[14]
                item.itemslotfoot[14] = item.assignmentinvslot[15]
                item.itemslotfoot[15] = item.assignmentinvslot[16]
                item.itemslotfoot[16] = item.assignmentinvslot[17]    
            if item.inventoryslot1[5] == 'armoracc':
                if item.itemslotacc1[0] == 0:    
                    item.itemslotacc1[0] = item.assignmentinvslot[0]
                    item.itemslotacc1[1] = item.assignmentinvslot[2]
                    item.itemslotacc1[2] = item.assignmentinvslot[3]
                    item.itemslotacc1[3] = item.assignmentinvslot[4]
                    item.itemslotacc1[4] = item.assignmentinvslot[5]
                    item.itemslotacc1[5] = item.assignmentinvslot[6]
                    item.itemslotacc1[6] = item.assignmentinvslot[7]
                    item.itemslotacc1[7] = item.assignmentinvslot[8]
                    item.itemslotacc1[8] = item.assignmentinvslot[9]
                    item.itemslotacc1[9] = item.assignmentinvslot[10]
                    item.itemslotacc1[10] = item.assignmentinvslot[11]
                    item.itemslotacc1[11] = item.assignmentinvslot[12]
                    item.itemslotacc1[12] = item.assignmentinvslot[13]
                    item.itemslotacc1[13] = item.assignmentinvslot[14]
                    item.itemslotacc1[14] = item.assignmentinvslot[15]
                    item.itemslotacc1[15] = item.assignmentinvslot[16]
                    item.itemslotacc1[16] = item.assignmentinvslot[17] 
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] == 0):
                    item.itemslotacc2[0] = item.assignmentinvslot[0]
                    item.itemslotacc2[1] = item.assignmentinvslot[2]
                    item.itemslotacc2[2] = item.assignmentinvslot[3]
                    item.itemslotacc2[3] = item.assignmentinvslot[4]
                    item.itemslotacc2[4] = item.assignmentinvslot[5]
                    item.itemslotacc2[5] = item.assignmentinvslot[6]
                    item.itemslotacc2[6] = item.assignmentinvslot[7]
                    item.itemslotacc2[7] = item.assignmentinvslot[8]
                    item.itemslotacc2[8] = item.assignmentinvslot[9]
                    item.itemslotacc2[9] = item.assignmentinvslot[10]
                    item.itemslotacc2[10] = item.assignmentinvslot[11]
                    item.itemslotacc2[11] = item.assignmentinvslot[12]
                    item.itemslotacc2[12] = item.assignmentinvslot[13]
                    item.itemslotacc2[13] = item.assignmentinvslot[14]
                    item.itemslotacc2[14] = item.assignmentinvslot[15]
                    item.itemslotacc2[15] = item.assignmentinvslot[16]
                    item.itemslotacc2[16] = item.assignmentinvslot[17]  
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] == 0):
                    item.itemslotacc3[0] = item.assignmentinvslot[0]
                    item.itemslotacc3[1] = item.assignmentinvslot[2]
                    item.itemslotacc3[2] = item.assignmentinvslot[3]
                    item.itemslotacc3[3] = item.assignmentinvslot[4]
                    item.itemslotacc3[4] = item.assignmentinvslot[5]
                    item.itemslotacc3[5] = item.assignmentinvslot[6]
                    item.itemslotacc3[6] = item.assignmentinvslot[7]
                    item.itemslotacc3[7] = item.assignmentinvslot[8]
                    item.itemslotacc3[8] = item.assignmentinvslot[9]
                    item.itemslotacc3[9] = item.assignmentinvslot[10]
                    item.itemslotacc3[10] = item.assignmentinvslot[11]
                    item.itemslotacc3[11] = item.assignmentinvslot[12]
                    item.itemslotacc3[12] = item.assignmentinvslot[13]
                    item.itemslotacc3[13] = item.assignmentinvslot[14]
                    item.itemslotacc3[14] = item.assignmentinvslot[15]
                    item.itemslotacc3[15] = item.assignmentinvslot[16]
                    item.itemslotacc3[16] = item.assignmentinvslot[17]               
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na akcesoria są w użyciu')
            if item.inventoryslot1[5] == 'armoractive': 
                if (item.itemslotactive1[0] == 0):
                    item.itemslotactive1[0] = item.assignmentinvslot[0]
                    item.itemslotactive1[1] = item.assignmentinvslot[2]
                    item.itemslotactive1[2] = item.assignmentinvslot[3]
                    item.itemslotactive1[3] = item.assignmentinvslot[4]
                    item.itemslotactive1[4] = item.assignmentinvslot[5]
                    item.itemslotactive1[5] = item.assignmentinvslot[6]
                    item.itemslotactive1[6] = item.assignmentinvslot[7]
                    item.itemslotactive1[7] = item.assignmentinvslot[8]
                    item.itemslotactive1[8] = item.assignmentinvslot[9]
                    item.itemslotactive1[9] = item.assignmentinvslot[10]
                    item.itemslotactive1[10] = item.assignmentinvslot[11]
                    item.itemslotactive1[11] = item.assignmentinvslot[12]
                    item.itemslotactive1[12] = item.assignmentinvslot[13]
                    item.itemslotactive1[13] = item.assignmentinvslot[14]
                    item.itemslotactive1[14] = item.assignmentinvslot[15]
                    item.itemslotactive1[15] = item.assignmentinvslot[16]
                    item.itemslotactive1[16] = item.assignmentinvslot[17]           
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] == 0):
                    item.itemslotactive2[0] = item.assignmentinvslot[0]
                    item.itemslotactive2[1] = item.assignmentinvslot[2]
                    item.itemslotactive2[2] = item.assignmentinvslot[3]
                    item.itemslotactive2[3] = item.assignmentinvslot[4]
                    item.itemslotactive2[4] = item.assignmentinvslot[5]
                    item.itemslotactive2[5] = item.assignmentinvslot[6]
                    item.itemslotactive2[6] = item.assignmentinvslot[7]
                    item.itemslotactive2[7] = item.assignmentinvslot[8]
                    item.itemslotactive2[8] = item.assignmentinvslot[9]
                    item.itemslotactive2[9] = item.assignmentinvslot[10]
                    item.itemslotactive2[10] = item.assignmentinvslot[11]
                    item.itemslotactive2[11] = item.assignmentinvslot[12]
                    item.itemslotactive2[12] = item.assignmentinvslot[13]
                    item.itemslotactive2[13] = item.assignmentinvslot[14]
                    item.itemslotactive2[14] = item.assignmentinvslot[15]
                    item.itemslotactive2[15] = item.assignmentinvslot[16]
                    item.itemslotactive2[16] = item.assignmentinvslot[17]                
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] == 0):
                    item.itemslotactive3[0] = item.assignmentinvslot[0]
                    item.itemslotactive3[1] = item.assignmentinvslot[2]
                    item.itemslotactive3[2] = item.assignmentinvslot[3]
                    item.itemslotactive3[3] = item.assignmentinvslot[4]
                    item.itemslotactive3[4] = item.assignmentinvslot[5]
                    item.itemslotactive3[5] = item.assignmentinvslot[6]
                    item.itemslotactive3[6] = item.assignmentinvslot[7]
                    item.itemslotactive3[7] = item.assignmentinvslot[8]
                    item.itemslotactive3[8] = item.assignmentinvslot[9]
                    item.itemslotactive3[9] = item.assignmentinvslot[10]
                    item.itemslotactive3[10] = item.assignmentinvslot[11]
                    item.itemslotactive3[11] = item.assignmentinvslot[12]
                    item.itemslotactive3[12] = item.assignmentinvslot[13]
                    item.itemslotactive3[13] = item.assignmentinvslot[14]
                    item.itemslotactive3[14] = item.assignmentinvslot[15]
                    item.itemslotactive3[15] = item.assignmentinvslot[16]
                    item.itemslotactive3[16] = item.assignmentinvslot[17]                 
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] == 0):
                    item.itemslotactive4[0] = item.assignmentinvslot[0]
                    item.itemslotactive4[1] = item.assignmentinvslot[2]
                    item.itemslotactive4[2] = item.assignmentinvslot[3]
                    item.itemslotactive4[3] = item.assignmentinvslot[4]
                    item.itemslotactive4[4] = item.assignmentinvslot[5]
                    item.itemslotactive4[5] = item.assignmentinvslot[6]
                    item.itemslotactive4[6] = item.assignmentinvslot[7]
                    item.itemslotactive4[7] = item.assignmentinvslot[8]
                    item.itemslotactive4[8] = item.assignmentinvslot[9]
                    item.itemslotactive4[9] = item.assignmentinvslot[10]
                    item.itemslotactive4[10] = item.assignmentinvslot[11]
                    item.itemslotactive4[11] = item.assignmentinvslot[12]
                    item.itemslotactive4[12] = item.assignmentinvslot[13]
                    item.itemslotactive4[13] = item.assignmentinvslot[14]
                    item.itemslotactive4[14] = item.assignmentinvslot[15]
                    item.itemslotactive4[15] = item.assignmentinvslot[16]
                    item.itemslotactive4[16] = item.assignmentinvslot[17]    
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] == 0):
                    item.itemslotactive5[0] = item.assignmentinvslot[0]
                    item.itemslotactive5[1] = item.assignmentinvslot[2]
                    item.itemslotactive5[2] = item.assignmentinvslot[3]
                    item.itemslotactive5[3] = item.assignmentinvslot[4]
                    item.itemslotactive5[4] = item.assignmentinvslot[5]
                    item.itemslotactive5[5] = item.assignmentinvslot[6]
                    item.itemslotactive5[6] = item.assignmentinvslot[7]
                    item.itemslotactive5[7] = item.assignmentinvslot[8]
                    item.itemslotactive5[8] = item.assignmentinvslot[9]
                    item.itemslotactive5[9] = item.assignmentinvslot[10]
                    item.itemslotactive5[10] = item.assignmentinvslot[11]
                    item.itemslotactive5[11] = item.assignmentinvslot[12]
                    item.itemslotactive5[12] = item.assignmentinvslot[13]
                    item.itemslotactive5[13] = item.assignmentinvslot[14]
                    item.itemslotactive5[14] = item.assignmentinvslot[15]
                    item.itemslotactive5[15] = item.assignmentinvslot[16]
                    item.itemslotactive5[16] = item.assignmentinvslot[17]     
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] == 0):
                    item.itemslotactive6[0] = item.assignmentinvslot[0]
                    item.itemslotactive6[1] = item.assignmentinvslot[2]
                    item.itemslotactive6[2] = item.assignmentinvslot[3]
                    item.itemslotactive6[3] = item.assignmentinvslot[4]
                    item.itemslotactive6[4] = item.assignmentinvslot[5]
                    item.itemslotactive6[5] = item.assignmentinvslot[6]
                    item.itemslotactive6[6] = item.assignmentinvslot[7]
                    item.itemslotactive6[7] = item.assignmentinvslot[8]
                    item.itemslotactive6[8] = item.assignmentinvslot[9]
                    item.itemslotactive6[9] = item.assignmentinvslot[10]
                    item.itemslotactive6[10] = item.assignmentinvslot[11]
                    item.itemslotactive6[11] = item.assignmentinvslot[12]
                    item.itemslotactive6[12] = item.assignmentinvslot[13]
                    item.itemslotactive6[13] = item.assignmentinvslot[14]
                    item.itemslotactive6[14] = item.assignmentinvslot[15]
                    item.itemslotactive6[15] = item.assignmentinvslot[16]
                    item.itemslotactive6[16] = item.assignmentinvslot[17]                   
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na przedmioty aktywne są w użyciu')
        if (item.inventoryslot2[4] == lookforinv) and (item.inventoryslot2[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot2
            if item.inventoryslot2[5] == 'armorhead':
                item.itemslothead[0] = item.assignmentinvslot[0]
                item.itemslothead[1] = item.assignmentinvslot[2]
                item.itemslothead[2] = item.assignmentinvslot[3]
                item.itemslothead[3] = item.assignmentinvslot[4]
                item.itemslothead[4] = item.assignmentinvslot[5]
                item.itemslothead[5] = item.assignmentinvslot[6]
                item.itemslothead[6] = item.assignmentinvslot[7]
                item.itemslothead[7] = item.assignmentinvslot[8]
                item.itemslothead[8] = item.assignmentinvslot[9]
                item.itemslothead[9] = item.assignmentinvslot[10]
                item.itemslothead[10] = item.assignmentinvslot[11]
                item.itemslothead[11] = item.assignmentinvslot[12]
                item.itemslothead[12] = item.assignmentinvslot[13]
                item.itemslothead[13] = item.assignmentinvslot[14]
                item.itemslothead[14] = item.assignmentinvslot[15]
                item.itemslothead[15] = item.assignmentinvslot[16]
                item.itemslothead[16] = item.assignmentinvslot[17]
            if item.inventoryslot2[5] == 'armorchest':
                item.itemslotchest[0] = item.assignmentinvslot[0]
                item.itemslotchest[1] = item.assignmentinvslot[2]
                item.itemslotchest[2] = item.assignmentinvslot[3]
                item.itemslotchest[3] = item.assignmentinvslot[4]
                item.itemslotchest[4] = item.assignmentinvslot[5]
                item.itemslotchest[5] = item.assignmentinvslot[6]
                item.itemslotchest[6] = item.assignmentinvslot[7]
                item.itemslotchest[7] = item.assignmentinvslot[8]
                item.itemslotchest[8] = item.assignmentinvslot[9]
                item.itemslotchest[9] = item.assignmentinvslot[10]
                item.itemslotchest[10] = item.assignmentinvslot[11]
                item.itemslotchest[11] = item.assignmentinvslot[12]
                item.itemslotchest[12] = item.assignmentinvslot[13]
                item.itemslotchest[13] = item.assignmentinvslot[14]
                item.itemslotchest[14] = item.assignmentinvslot[15]
                item.itemslotchest[15] = item.assignmentinvslot[16]
                item.itemslotchest[16] = item.assignmentinvslot[17]
            if item.inventoryslot2[5] == 'armorarms':
                item.itemslotarms[0] = item.assignmentinvslot[0]
                item.itemslotarms[1] = item.assignmentinvslot[2]
                item.itemslotarms[2] = item.assignmentinvslot[3]
                item.itemslotarms[3] = item.assignmentinvslot[4]
                item.itemslotarms[4] = item.assignmentinvslot[5]
                item.itemslotarms[5] = item.assignmentinvslot[6]
                item.itemslotarms[6] = item.assignmentinvslot[7]
                item.itemslotarms[7] = item.assignmentinvslot[8]
                item.itemslotarms[8] = item.assignmentinvslot[9]
                item.itemslotarms[9] = item.assignmentinvslot[10]
                item.itemslotarms[10] = item.assignmentinvslot[11]
                item.itemslotarms[11] = item.assignmentinvslot[12]
                item.itemslotarms[12] = item.assignmentinvslot[13]
                item.itemslotarms[13] = item.assignmentinvslot[14]
                item.itemslotarms[14] = item.assignmentinvslot[15]
                item.itemslotarms[15] = item.assignmentinvslot[16]
                item.itemslotarms[16] = item.assignmentinvslot[17]    
            if item.inventoryslot2[5] == 'armorhands':
                item.itemslothands[0] = item.assignmentinvslot[0]
                item.itemslothands[1] = item.assignmentinvslot[2]
                item.itemslothands[2] = item.assignmentinvslot[3]
                item.itemslothands[3] = item.assignmentinvslot[4]
                item.itemslothands[4] = item.assignmentinvslot[5]
                item.itemslothands[5] = item.assignmentinvslot[6]
                item.itemslothands[6] = item.assignmentinvslot[7]
                item.itemslothands[7] = item.assignmentinvslot[8]
                item.itemslothands[8] = item.assignmentinvslot[9]
                item.itemslothands[9] = item.assignmentinvslot[10]
                item.itemslothands[10] = item.assignmentinvslot[11]
                item.itemslothands[11] = item.assignmentinvslot[12]
                item.itemslothands[12] = item.assignmentinvslot[13]
                item.itemslothands[13] = item.assignmentinvslot[14]
                item.itemslothands[14] = item.assignmentinvslot[15]
                item.itemslothands[15] = item.assignmentinvslot[16]
                item.itemslothands[16] = item.assignmentinvslot[17]   
            if item.inventoryslot2[5] == 'armorlegs':
                item.itemslotlegs[0] = item.assignmentinvslot[0]
                item.itemslotlegs[1] = item.assignmentinvslot[2]
                item.itemslotlegs[2] = item.assignmentinvslot[3]
                item.itemslotlegs[3] = item.assignmentinvslot[4]
                item.itemslotlegs[4] = item.assignmentinvslot[5]
                item.itemslotlegs[5] = item.assignmentinvslot[6]
                item.itemslotlegs[6] = item.assignmentinvslot[7]
                item.itemslotlegs[7] = item.assignmentinvslot[8]
                item.itemslotlegs[8] = item.assignmentinvslot[9]
                item.itemslotlegs[9] = item.assignmentinvslot[10]
                item.itemslotlegs[10] = item.assignmentinvslot[11]
                item.itemslotlegs[11] = item.assignmentinvslot[12]
                item.itemslotlegs[12] = item.assignmentinvslot[13]
                item.itemslotlegs[13] = item.assignmentinvslot[14]
                item.itemslotlegs[14] = item.assignmentinvslot[15]
                item.itemslotlegs[15] = item.assignmentinvslot[16]
                item.itemslotlegs[16] = item.assignmentinvslot[17]    
            if item.inventoryslot2[5] == 'armorfoot':
                item.itemslotfoot[0] = item.assignmentinvslot[0]
                item.itemslotfoot[1] = item.assignmentinvslot[2]
                item.itemslotfoot[2] = item.assignmentinvslot[3]
                item.itemslotfoot[3] = item.assignmentinvslot[4]
                item.itemslotfoot[4] = item.assignmentinvslot[5]
                item.itemslotfoot[5] = item.assignmentinvslot[6]
                item.itemslotfoot[6] = item.assignmentinvslot[7]
                item.itemslotfoot[7] = item.assignmentinvslot[8]
                item.itemslotfoot[8] = item.assignmentinvslot[9]
                item.itemslotfoot[9] = item.assignmentinvslot[10]
                item.itemslotfoot[10] = item.assignmentinvslot[11]
                item.itemslotfoot[11] = item.assignmentinvslot[12]
                item.itemslotfoot[12] = item.assignmentinvslot[13]
                item.itemslotfoot[13] = item.assignmentinvslot[14]
                item.itemslotfoot[14] = item.assignmentinvslot[15]
                item.itemslotfoot[15] = item.assignmentinvslot[16]
                item.itemslotfoot[16] = item.assignmentinvslot[17]    
            if item.inventoryslot2[5] == 'armoracc':
                if item.itemslotacc1[0] == 0:    
                    item.itemslotacc1[0] = item.assignmentinvslot[0]
                    item.itemslotacc1[1] = item.assignmentinvslot[2]
                    item.itemslotacc1[2] = item.assignmentinvslot[3]
                    item.itemslotacc1[3] = item.assignmentinvslot[4]
                    item.itemslotacc1[4] = item.assignmentinvslot[5]
                    item.itemslotacc1[5] = item.assignmentinvslot[6]
                    item.itemslotacc1[6] = item.assignmentinvslot[7]
                    item.itemslotacc1[7] = item.assignmentinvslot[8]
                    item.itemslotacc1[8] = item.assignmentinvslot[9]
                    item.itemslotacc1[9] = item.assignmentinvslot[10]
                    item.itemslotacc1[10] = item.assignmentinvslot[11]
                    item.itemslotacc1[11] = item.assignmentinvslot[12]
                    item.itemslotacc1[12] = item.assignmentinvslot[13]
                    item.itemslotacc1[13] = item.assignmentinvslot[14]
                    item.itemslotacc1[14] = item.assignmentinvslot[15]
                    item.itemslotacc1[15] = item.assignmentinvslot[16]
                    item.itemslotacc1[16] = item.assignmentinvslot[17] 
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] == 0):
                    item.itemslotacc2[0] = item.assignmentinvslot[0]
                    item.itemslotacc2[1] = item.assignmentinvslot[2]
                    item.itemslotacc2[2] = item.assignmentinvslot[3]
                    item.itemslotacc2[3] = item.assignmentinvslot[4]
                    item.itemslotacc2[4] = item.assignmentinvslot[5]
                    item.itemslotacc2[5] = item.assignmentinvslot[6]
                    item.itemslotacc2[6] = item.assignmentinvslot[7]
                    item.itemslotacc2[7] = item.assignmentinvslot[8]
                    item.itemslotacc2[8] = item.assignmentinvslot[9]
                    item.itemslotacc2[9] = item.assignmentinvslot[10]
                    item.itemslotacc2[10] = item.assignmentinvslot[11]
                    item.itemslotacc2[11] = item.assignmentinvslot[12]
                    item.itemslotacc2[12] = item.assignmentinvslot[13]
                    item.itemslotacc2[13] = item.assignmentinvslot[14]
                    item.itemslotacc2[14] = item.assignmentinvslot[15]
                    item.itemslotacc2[15] = item.assignmentinvslot[16]
                    item.itemslotacc2[16] = item.assignmentinvslot[17]  
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] == 0):
                    item.itemslotacc3[0] = item.assignmentinvslot[0]
                    item.itemslotacc3[1] = item.assignmentinvslot[2]
                    item.itemslotacc3[2] = item.assignmentinvslot[3]
                    item.itemslotacc3[3] = item.assignmentinvslot[4]
                    item.itemslotacc3[4] = item.assignmentinvslot[5]
                    item.itemslotacc3[5] = item.assignmentinvslot[6]
                    item.itemslotacc3[6] = item.assignmentinvslot[7]
                    item.itemslotacc3[7] = item.assignmentinvslot[8]
                    item.itemslotacc3[8] = item.assignmentinvslot[9]
                    item.itemslotacc3[9] = item.assignmentinvslot[10]
                    item.itemslotacc3[10] = item.assignmentinvslot[11]
                    item.itemslotacc3[11] = item.assignmentinvslot[12]
                    item.itemslotacc3[12] = item.assignmentinvslot[13]
                    item.itemslotacc3[13] = item.assignmentinvslot[14]
                    item.itemslotacc3[14] = item.assignmentinvslot[15]
                    item.itemslotacc3[15] = item.assignmentinvslot[16]
                    item.itemslotacc3[16] = item.assignmentinvslot[17]               
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na akcesoria są w użyciu')
            if item.inventoryslot2[5] == 'armoractive': 
                if (item.itemslotactive1[0] == 0):
                    item.itemslotactive1[0] = item.assignmentinvslot[0]
                    item.itemslotactive1[1] = item.assignmentinvslot[2]
                    item.itemslotactive1[2] = item.assignmentinvslot[3]
                    item.itemslotactive1[3] = item.assignmentinvslot[4]
                    item.itemslotactive1[4] = item.assignmentinvslot[5]
                    item.itemslotactive1[5] = item.assignmentinvslot[6]
                    item.itemslotactive1[6] = item.assignmentinvslot[7]
                    item.itemslotactive1[7] = item.assignmentinvslot[8]
                    item.itemslotactive1[8] = item.assignmentinvslot[9]
                    item.itemslotactive1[9] = item.assignmentinvslot[10]
                    item.itemslotactive1[10] = item.assignmentinvslot[11]
                    item.itemslotactive1[11] = item.assignmentinvslot[12]
                    item.itemslotactive1[12] = item.assignmentinvslot[13]
                    item.itemslotactive1[13] = item.assignmentinvslot[14]
                    item.itemslotactive1[14] = item.assignmentinvslot[15]
                    item.itemslotactive1[15] = item.assignmentinvslot[16]
                    item.itemslotactive1[16] = item.assignmentinvslot[17]           
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] == 0):
                    item.itemslotactive2[0] = item.assignmentinvslot[0]
                    item.itemslotactive2[1] = item.assignmentinvslot[2]
                    item.itemslotactive2[2] = item.assignmentinvslot[3]
                    item.itemslotactive2[3] = item.assignmentinvslot[4]
                    item.itemslotactive2[4] = item.assignmentinvslot[5]
                    item.itemslotactive2[5] = item.assignmentinvslot[6]
                    item.itemslotactive2[6] = item.assignmentinvslot[7]
                    item.itemslotactive2[7] = item.assignmentinvslot[8]
                    item.itemslotactive2[8] = item.assignmentinvslot[9]
                    item.itemslotactive2[9] = item.assignmentinvslot[10]
                    item.itemslotactive2[10] = item.assignmentinvslot[11]
                    item.itemslotactive2[11] = item.assignmentinvslot[12]
                    item.itemslotactive2[12] = item.assignmentinvslot[13]
                    item.itemslotactive2[13] = item.assignmentinvslot[14]
                    item.itemslotactive2[14] = item.assignmentinvslot[15]
                    item.itemslotactive2[15] = item.assignmentinvslot[16]
                    item.itemslotactive2[16] = item.assignmentinvslot[17]                
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] == 0):
                    item.itemslotactive3[0] = item.assignmentinvslot[0]
                    item.itemslotactive3[1] = item.assignmentinvslot[2]
                    item.itemslotactive3[2] = item.assignmentinvslot[3]
                    item.itemslotactive3[3] = item.assignmentinvslot[4]
                    item.itemslotactive3[4] = item.assignmentinvslot[5]
                    item.itemslotactive3[5] = item.assignmentinvslot[6]
                    item.itemslotactive3[6] = item.assignmentinvslot[7]
                    item.itemslotactive3[7] = item.assignmentinvslot[8]
                    item.itemslotactive3[8] = item.assignmentinvslot[9]
                    item.itemslotactive3[9] = item.assignmentinvslot[10]
                    item.itemslotactive3[10] = item.assignmentinvslot[11]
                    item.itemslotactive3[11] = item.assignmentinvslot[12]
                    item.itemslotactive3[12] = item.assignmentinvslot[13]
                    item.itemslotactive3[13] = item.assignmentinvslot[14]
                    item.itemslotactive3[14] = item.assignmentinvslot[15]
                    item.itemslotactive3[15] = item.assignmentinvslot[16]
                    item.itemslotactive3[16] = item.assignmentinvslot[17]                 
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] == 0):
                    item.itemslotactive4[0] = item.assignmentinvslot[0]
                    item.itemslotactive4[1] = item.assignmentinvslot[2]
                    item.itemslotactive4[2] = item.assignmentinvslot[3]
                    item.itemslotactive4[3] = item.assignmentinvslot[4]
                    item.itemslotactive4[4] = item.assignmentinvslot[5]
                    item.itemslotactive4[5] = item.assignmentinvslot[6]
                    item.itemslotactive4[6] = item.assignmentinvslot[7]
                    item.itemslotactive4[7] = item.assignmentinvslot[8]
                    item.itemslotactive4[8] = item.assignmentinvslot[9]
                    item.itemslotactive4[9] = item.assignmentinvslot[10]
                    item.itemslotactive4[10] = item.assignmentinvslot[11]
                    item.itemslotactive4[11] = item.assignmentinvslot[12]
                    item.itemslotactive4[12] = item.assignmentinvslot[13]
                    item.itemslotactive4[13] = item.assignmentinvslot[14]
                    item.itemslotactive4[14] = item.assignmentinvslot[15]
                    item.itemslotactive4[15] = item.assignmentinvslot[16]
                    item.itemslotactive4[16] = item.assignmentinvslot[17]    
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] == 0):
                    item.itemslotactive5[0] = item.assignmentinvslot[0]
                    item.itemslotactive5[1] = item.assignmentinvslot[2]
                    item.itemslotactive5[2] = item.assignmentinvslot[3]
                    item.itemslotactive5[3] = item.assignmentinvslot[4]
                    item.itemslotactive5[4] = item.assignmentinvslot[5]
                    item.itemslotactive5[5] = item.assignmentinvslot[6]
                    item.itemslotactive5[6] = item.assignmentinvslot[7]
                    item.itemslotactive5[7] = item.assignmentinvslot[8]
                    item.itemslotactive5[8] = item.assignmentinvslot[9]
                    item.itemslotactive5[9] = item.assignmentinvslot[10]
                    item.itemslotactive5[10] = item.assignmentinvslot[11]
                    item.itemslotactive5[11] = item.assignmentinvslot[12]
                    item.itemslotactive5[12] = item.assignmentinvslot[13]
                    item.itemslotactive5[13] = item.assignmentinvslot[14]
                    item.itemslotactive5[14] = item.assignmentinvslot[15]
                    item.itemslotactive5[15] = item.assignmentinvslot[16]
                    item.itemslotactive5[16] = item.assignmentinvslot[17]     
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] == 0):
                    item.itemslotactive6[0] = item.assignmentinvslot[0]
                    item.itemslotactive6[1] = item.assignmentinvslot[2]
                    item.itemslotactive6[2] = item.assignmentinvslot[3]
                    item.itemslotactive6[3] = item.assignmentinvslot[4]
                    item.itemslotactive6[4] = item.assignmentinvslot[5]
                    item.itemslotactive6[5] = item.assignmentinvslot[6]
                    item.itemslotactive6[6] = item.assignmentinvslot[7]
                    item.itemslotactive6[7] = item.assignmentinvslot[8]
                    item.itemslotactive6[8] = item.assignmentinvslot[9]
                    item.itemslotactive6[9] = item.assignmentinvslot[10]
                    item.itemslotactive6[10] = item.assignmentinvslot[11]
                    item.itemslotactive6[11] = item.assignmentinvslot[12]
                    item.itemslotactive6[12] = item.assignmentinvslot[13]
                    item.itemslotactive6[13] = item.assignmentinvslot[14]
                    item.itemslotactive6[14] = item.assignmentinvslot[15]
                    item.itemslotactive6[15] = item.assignmentinvslot[16]
                    item.itemslotactive6[16] = item.assignmentinvslot[17]                   
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na przedmioty aktywne są w użyciu')
        if (item.inventoryslot3[4] == lookforinv) and (item.inventoryslot3[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot3
            if item.inventoryslot3[5] == 'armorhead':
                item.itemslothead[0] = item.assignmentinvslot[0]
                item.itemslothead[1] = item.assignmentinvslot[2]
                item.itemslothead[2] = item.assignmentinvslot[3]
                item.itemslothead[3] = item.assignmentinvslot[4]
                item.itemslothead[4] = item.assignmentinvslot[5]
                item.itemslothead[5] = item.assignmentinvslot[6]
                item.itemslothead[6] = item.assignmentinvslot[7]
                item.itemslothead[7] = item.assignmentinvslot[8]
                item.itemslothead[8] = item.assignmentinvslot[9]
                item.itemslothead[9] = item.assignmentinvslot[10]
                item.itemslothead[10] = item.assignmentinvslot[11]
                item.itemslothead[11] = item.assignmentinvslot[12]
                item.itemslothead[12] = item.assignmentinvslot[13]
                item.itemslothead[13] = item.assignmentinvslot[14]
                item.itemslothead[14] = item.assignmentinvslot[15]
                item.itemslothead[15] = item.assignmentinvslot[16]
                item.itemslothead[16] = item.assignmentinvslot[17]
            if item.inventoryslot3[5] == 'armorchest':
                item.itemslotchest[0] = item.assignmentinvslot[0]
                item.itemslotchest[1] = item.assignmentinvslot[2]
                item.itemslotchest[2] = item.assignmentinvslot[3]
                item.itemslotchest[3] = item.assignmentinvslot[4]
                item.itemslotchest[4] = item.assignmentinvslot[5]
                item.itemslotchest[5] = item.assignmentinvslot[6]
                item.itemslotchest[6] = item.assignmentinvslot[7]
                item.itemslotchest[7] = item.assignmentinvslot[8]
                item.itemslotchest[8] = item.assignmentinvslot[9]
                item.itemslotchest[9] = item.assignmentinvslot[10]
                item.itemslotchest[10] = item.assignmentinvslot[11]
                item.itemslotchest[11] = item.assignmentinvslot[12]
                item.itemslotchest[12] = item.assignmentinvslot[13]
                item.itemslotchest[13] = item.assignmentinvslot[14]
                item.itemslotchest[14] = item.assignmentinvslot[15]
                item.itemslotchest[15] = item.assignmentinvslot[16]
                item.itemslotchest[16] = item.assignmentinvslot[17]
            if item.inventoryslot3[5] == 'armorarms':
                item.itemslotarms[0] = item.assignmentinvslot[0]
                item.itemslotarms[1] = item.assignmentinvslot[2]
                item.itemslotarms[2] = item.assignmentinvslot[3]
                item.itemslotarms[3] = item.assignmentinvslot[4]
                item.itemslotarms[4] = item.assignmentinvslot[5]
                item.itemslotarms[5] = item.assignmentinvslot[6]
                item.itemslotarms[6] = item.assignmentinvslot[7]
                item.itemslotarms[7] = item.assignmentinvslot[8]
                item.itemslotarms[8] = item.assignmentinvslot[9]
                item.itemslotarms[9] = item.assignmentinvslot[10]
                item.itemslotarms[10] = item.assignmentinvslot[11]
                item.itemslotarms[11] = item.assignmentinvslot[12]
                item.itemslotarms[12] = item.assignmentinvslot[13]
                item.itemslotarms[13] = item.assignmentinvslot[14]
                item.itemslotarms[14] = item.assignmentinvslot[15]
                item.itemslotarms[15] = item.assignmentinvslot[16]
                item.itemslotarms[16] = item.assignmentinvslot[17]    
            if item.inventoryslot3[5] == 'armorhands':
                item.itemslothands[0] = item.assignmentinvslot[0]
                item.itemslothands[1] = item.assignmentinvslot[2]
                item.itemslothands[2] = item.assignmentinvslot[3]
                item.itemslothands[3] = item.assignmentinvslot[4]
                item.itemslothands[4] = item.assignmentinvslot[5]
                item.itemslothands[5] = item.assignmentinvslot[6]
                item.itemslothands[6] = item.assignmentinvslot[7]
                item.itemslothands[7] = item.assignmentinvslot[8]
                item.itemslothands[8] = item.assignmentinvslot[9]
                item.itemslothands[9] = item.assignmentinvslot[10]
                item.itemslothands[10] = item.assignmentinvslot[11]
                item.itemslothands[11] = item.assignmentinvslot[12]
                item.itemslothands[12] = item.assignmentinvslot[13]
                item.itemslothands[13] = item.assignmentinvslot[14]
                item.itemslothands[14] = item.assignmentinvslot[15]
                item.itemslothands[15] = item.assignmentinvslot[16]
                item.itemslothands[16] = item.assignmentinvslot[17]   
            if item.inventoryslot3[5] == 'armorlegs':
                item.itemslotlegs[0] = item.assignmentinvslot[0]
                item.itemslotlegs[1] = item.assignmentinvslot[2]
                item.itemslotlegs[2] = item.assignmentinvslot[3]
                item.itemslotlegs[3] = item.assignmentinvslot[4]
                item.itemslotlegs[4] = item.assignmentinvslot[5]
                item.itemslotlegs[5] = item.assignmentinvslot[6]
                item.itemslotlegs[6] = item.assignmentinvslot[7]
                item.itemslotlegs[7] = item.assignmentinvslot[8]
                item.itemslotlegs[8] = item.assignmentinvslot[9]
                item.itemslotlegs[9] = item.assignmentinvslot[10]
                item.itemslotlegs[10] = item.assignmentinvslot[11]
                item.itemslotlegs[11] = item.assignmentinvslot[12]
                item.itemslotlegs[12] = item.assignmentinvslot[13]
                item.itemslotlegs[13] = item.assignmentinvslot[14]
                item.itemslotlegs[14] = item.assignmentinvslot[15]
                item.itemslotlegs[15] = item.assignmentinvslot[16]
                item.itemslotlegs[16] = item.assignmentinvslot[17]    
            if item.inventoryslot3[5] == 'armorfoot':
                item.itemslotfoot[0] = item.assignmentinvslot[0]
                item.itemslotfoot[1] = item.assignmentinvslot[2]
                item.itemslotfoot[2] = item.assignmentinvslot[3]
                item.itemslotfoot[3] = item.assignmentinvslot[4]
                item.itemslotfoot[4] = item.assignmentinvslot[5]
                item.itemslotfoot[5] = item.assignmentinvslot[6]
                item.itemslotfoot[6] = item.assignmentinvslot[7]
                item.itemslotfoot[7] = item.assignmentinvslot[8]
                item.itemslotfoot[8] = item.assignmentinvslot[9]
                item.itemslotfoot[9] = item.assignmentinvslot[10]
                item.itemslotfoot[10] = item.assignmentinvslot[11]
                item.itemslotfoot[11] = item.assignmentinvslot[12]
                item.itemslotfoot[12] = item.assignmentinvslot[13]
                item.itemslotfoot[13] = item.assignmentinvslot[14]
                item.itemslotfoot[14] = item.assignmentinvslot[15]
                item.itemslotfoot[15] = item.assignmentinvslot[16]
                item.itemslotfoot[16] = item.assignmentinvslot[17]    
            if item.inventoryslot3[5] == 'armoracc':
                if item.itemslotacc1[0] == 0:    
                    item.itemslotacc1[0] = item.assignmentinvslot[0]
                    item.itemslotacc1[1] = item.assignmentinvslot[2]
                    item.itemslotacc1[2] = item.assignmentinvslot[3]
                    item.itemslotacc1[3] = item.assignmentinvslot[4]
                    item.itemslotacc1[4] = item.assignmentinvslot[5]
                    item.itemslotacc1[5] = item.assignmentinvslot[6]
                    item.itemslotacc1[6] = item.assignmentinvslot[7]
                    item.itemslotacc1[7] = item.assignmentinvslot[8]
                    item.itemslotacc1[8] = item.assignmentinvslot[9]
                    item.itemslotacc1[9] = item.assignmentinvslot[10]
                    item.itemslotacc1[10] = item.assignmentinvslot[11]
                    item.itemslotacc1[11] = item.assignmentinvslot[12]
                    item.itemslotacc1[12] = item.assignmentinvslot[13]
                    item.itemslotacc1[13] = item.assignmentinvslot[14]
                    item.itemslotacc1[14] = item.assignmentinvslot[15]
                    item.itemslotacc1[15] = item.assignmentinvslot[16]
                    item.itemslotacc1[16] = item.assignmentinvslot[17] 
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] == 0):
                    item.itemslotacc2[0] = item.assignmentinvslot[0]
                    item.itemslotacc2[1] = item.assignmentinvslot[2]
                    item.itemslotacc2[2] = item.assignmentinvslot[3]
                    item.itemslotacc2[3] = item.assignmentinvslot[4]
                    item.itemslotacc2[4] = item.assignmentinvslot[5]
                    item.itemslotacc2[5] = item.assignmentinvslot[6]
                    item.itemslotacc2[6] = item.assignmentinvslot[7]
                    item.itemslotacc2[7] = item.assignmentinvslot[8]
                    item.itemslotacc2[8] = item.assignmentinvslot[9]
                    item.itemslotacc2[9] = item.assignmentinvslot[10]
                    item.itemslotacc2[10] = item.assignmentinvslot[11]
                    item.itemslotacc2[11] = item.assignmentinvslot[12]
                    item.itemslotacc2[12] = item.assignmentinvslot[13]
                    item.itemslotacc2[13] = item.assignmentinvslot[14]
                    item.itemslotacc2[14] = item.assignmentinvslot[15]
                    item.itemslotacc2[15] = item.assignmentinvslot[16]
                    item.itemslotacc2[16] = item.assignmentinvslot[17]  
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] == 0):
                    item.itemslotacc3[0] = item.assignmentinvslot[0]
                    item.itemslotacc3[1] = item.assignmentinvslot[2]
                    item.itemslotacc3[2] = item.assignmentinvslot[3]
                    item.itemslotacc3[3] = item.assignmentinvslot[4]
                    item.itemslotacc3[4] = item.assignmentinvslot[5]
                    item.itemslotacc3[5] = item.assignmentinvslot[6]
                    item.itemslotacc3[6] = item.assignmentinvslot[7]
                    item.itemslotacc3[7] = item.assignmentinvslot[8]
                    item.itemslotacc3[8] = item.assignmentinvslot[9]
                    item.itemslotacc3[9] = item.assignmentinvslot[10]
                    item.itemslotacc3[10] = item.assignmentinvslot[11]
                    item.itemslotacc3[11] = item.assignmentinvslot[12]
                    item.itemslotacc3[12] = item.assignmentinvslot[13]
                    item.itemslotacc3[13] = item.assignmentinvslot[14]
                    item.itemslotacc3[14] = item.assignmentinvslot[15]
                    item.itemslotacc3[15] = item.assignmentinvslot[16]
                    item.itemslotacc3[16] = item.assignmentinvslot[17]               
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na akcesoria są w użyciu')
            if item.inventoryslot3[5] == 'armoractive': 
                if (item.itemslotactive1[0] == 0):
                    item.itemslotactive1[0] = item.assignmentinvslot[0]
                    item.itemslotactive1[1] = item.assignmentinvslot[2]
                    item.itemslotactive1[2] = item.assignmentinvslot[3]
                    item.itemslotactive1[3] = item.assignmentinvslot[4]
                    item.itemslotactive1[4] = item.assignmentinvslot[5]
                    item.itemslotactive1[5] = item.assignmentinvslot[6]
                    item.itemslotactive1[6] = item.assignmentinvslot[7]
                    item.itemslotactive1[7] = item.assignmentinvslot[8]
                    item.itemslotactive1[8] = item.assignmentinvslot[9]
                    item.itemslotactive1[9] = item.assignmentinvslot[10]
                    item.itemslotactive1[10] = item.assignmentinvslot[11]
                    item.itemslotactive1[11] = item.assignmentinvslot[12]
                    item.itemslotactive1[12] = item.assignmentinvslot[13]
                    item.itemslotactive1[13] = item.assignmentinvslot[14]
                    item.itemslotactive1[14] = item.assignmentinvslot[15]
                    item.itemslotactive1[15] = item.assignmentinvslot[16]
                    item.itemslotactive1[16] = item.assignmentinvslot[17]           
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] == 0):
                    item.itemslotactive2[0] = item.assignmentinvslot[0]
                    item.itemslotactive2[1] = item.assignmentinvslot[2]
                    item.itemslotactive2[2] = item.assignmentinvslot[3]
                    item.itemslotactive2[3] = item.assignmentinvslot[4]
                    item.itemslotactive2[4] = item.assignmentinvslot[5]
                    item.itemslotactive2[5] = item.assignmentinvslot[6]
                    item.itemslotactive2[6] = item.assignmentinvslot[7]
                    item.itemslotactive2[7] = item.assignmentinvslot[8]
                    item.itemslotactive2[8] = item.assignmentinvslot[9]
                    item.itemslotactive2[9] = item.assignmentinvslot[10]
                    item.itemslotactive2[10] = item.assignmentinvslot[11]
                    item.itemslotactive2[11] = item.assignmentinvslot[12]
                    item.itemslotactive2[12] = item.assignmentinvslot[13]
                    item.itemslotactive2[13] = item.assignmentinvslot[14]
                    item.itemslotactive2[14] = item.assignmentinvslot[15]
                    item.itemslotactive2[15] = item.assignmentinvslot[16]
                    item.itemslotactive2[16] = item.assignmentinvslot[17]                
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] == 0):
                    item.itemslotactive3[0] = item.assignmentinvslot[0]
                    item.itemslotactive3[1] = item.assignmentinvslot[2]
                    item.itemslotactive3[2] = item.assignmentinvslot[3]
                    item.itemslotactive3[3] = item.assignmentinvslot[4]
                    item.itemslotactive3[4] = item.assignmentinvslot[5]
                    item.itemslotactive3[5] = item.assignmentinvslot[6]
                    item.itemslotactive3[6] = item.assignmentinvslot[7]
                    item.itemslotactive3[7] = item.assignmentinvslot[8]
                    item.itemslotactive3[8] = item.assignmentinvslot[9]
                    item.itemslotactive3[9] = item.assignmentinvslot[10]
                    item.itemslotactive3[10] = item.assignmentinvslot[11]
                    item.itemslotactive3[11] = item.assignmentinvslot[12]
                    item.itemslotactive3[12] = item.assignmentinvslot[13]
                    item.itemslotactive3[13] = item.assignmentinvslot[14]
                    item.itemslotactive3[14] = item.assignmentinvslot[15]
                    item.itemslotactive3[15] = item.assignmentinvslot[16]
                    item.itemslotactive3[16] = item.assignmentinvslot[17]                 
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] == 0):
                    item.itemslotactive4[0] = item.assignmentinvslot[0]
                    item.itemslotactive4[1] = item.assignmentinvslot[2]
                    item.itemslotactive4[2] = item.assignmentinvslot[3]
                    item.itemslotactive4[3] = item.assignmentinvslot[4]
                    item.itemslotactive4[4] = item.assignmentinvslot[5]
                    item.itemslotactive4[5] = item.assignmentinvslot[6]
                    item.itemslotactive4[6] = item.assignmentinvslot[7]
                    item.itemslotactive4[7] = item.assignmentinvslot[8]
                    item.itemslotactive4[8] = item.assignmentinvslot[9]
                    item.itemslotactive4[9] = item.assignmentinvslot[10]
                    item.itemslotactive4[10] = item.assignmentinvslot[11]
                    item.itemslotactive4[11] = item.assignmentinvslot[12]
                    item.itemslotactive4[12] = item.assignmentinvslot[13]
                    item.itemslotactive4[13] = item.assignmentinvslot[14]
                    item.itemslotactive4[14] = item.assignmentinvslot[15]
                    item.itemslotactive4[15] = item.assignmentinvslot[16]
                    item.itemslotactive4[16] = item.assignmentinvslot[17]    
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] == 0):
                    item.itemslotactive5[0] = item.assignmentinvslot[0]
                    item.itemslotactive5[1] = item.assignmentinvslot[2]
                    item.itemslotactive5[2] = item.assignmentinvslot[3]
                    item.itemslotactive5[3] = item.assignmentinvslot[4]
                    item.itemslotactive5[4] = item.assignmentinvslot[5]
                    item.itemslotactive5[5] = item.assignmentinvslot[6]
                    item.itemslotactive5[6] = item.assignmentinvslot[7]
                    item.itemslotactive5[7] = item.assignmentinvslot[8]
                    item.itemslotactive5[8] = item.assignmentinvslot[9]
                    item.itemslotactive5[9] = item.assignmentinvslot[10]
                    item.itemslotactive5[10] = item.assignmentinvslot[11]
                    item.itemslotactive5[11] = item.assignmentinvslot[12]
                    item.itemslotactive5[12] = item.assignmentinvslot[13]
                    item.itemslotactive5[13] = item.assignmentinvslot[14]
                    item.itemslotactive5[14] = item.assignmentinvslot[15]
                    item.itemslotactive5[15] = item.assignmentinvslot[16]
                    item.itemslotactive5[16] = item.assignmentinvslot[17]     
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] == 0):
                    item.itemslotactive6[0] = item.assignmentinvslot[0]
                    item.itemslotactive6[1] = item.assignmentinvslot[2]
                    item.itemslotactive6[2] = item.assignmentinvslot[3]
                    item.itemslotactive6[3] = item.assignmentinvslot[4]
                    item.itemslotactive6[4] = item.assignmentinvslot[5]
                    item.itemslotactive6[5] = item.assignmentinvslot[6]
                    item.itemslotactive6[6] = item.assignmentinvslot[7]
                    item.itemslotactive6[7] = item.assignmentinvslot[8]
                    item.itemslotactive6[8] = item.assignmentinvslot[9]
                    item.itemslotactive6[9] = item.assignmentinvslot[10]
                    item.itemslotactive6[10] = item.assignmentinvslot[11]
                    item.itemslotactive6[11] = item.assignmentinvslot[12]
                    item.itemslotactive6[12] = item.assignmentinvslot[13]
                    item.itemslotactive6[13] = item.assignmentinvslot[14]
                    item.itemslotactive6[14] = item.assignmentinvslot[15]
                    item.itemslotactive6[15] = item.assignmentinvslot[16]
                    item.itemslotactive6[16] = item.assignmentinvslot[17]                   
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na przedmioty aktywne są w użyciu')
        if (item.inventoryslot4[4] == lookforinv) and (item.inventoryslot4[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot4
            if item.inventoryslot4[5] == 'armorhead':
                item.itemslothead[0] = item.assignmentinvslot[0]
                item.itemslothead[1] = item.assignmentinvslot[2]
                item.itemslothead[2] = item.assignmentinvslot[3]
                item.itemslothead[3] = item.assignmentinvslot[4]
                item.itemslothead[4] = item.assignmentinvslot[5]
                item.itemslothead[5] = item.assignmentinvslot[6]
                item.itemslothead[6] = item.assignmentinvslot[7]
                item.itemslothead[7] = item.assignmentinvslot[8]
                item.itemslothead[8] = item.assignmentinvslot[9]
                item.itemslothead[9] = item.assignmentinvslot[10]
                item.itemslothead[10] = item.assignmentinvslot[11]
                item.itemslothead[11] = item.assignmentinvslot[12]
                item.itemslothead[12] = item.assignmentinvslot[13]
                item.itemslothead[13] = item.assignmentinvslot[14]
                item.itemslothead[14] = item.assignmentinvslot[15]
                item.itemslothead[15] = item.assignmentinvslot[16]
                item.itemslothead[16] = item.assignmentinvslot[17]
            if item.inventoryslot4[5] == 'armorchest':
                item.itemslotchest[0] = item.assignmentinvslot[0]
                item.itemslotchest[1] = item.assignmentinvslot[2]
                item.itemslotchest[2] = item.assignmentinvslot[3]
                item.itemslotchest[3] = item.assignmentinvslot[4]
                item.itemslotchest[4] = item.assignmentinvslot[5]
                item.itemslotchest[5] = item.assignmentinvslot[6]
                item.itemslotchest[6] = item.assignmentinvslot[7]
                item.itemslotchest[7] = item.assignmentinvslot[8]
                item.itemslotchest[8] = item.assignmentinvslot[9]
                item.itemslotchest[9] = item.assignmentinvslot[10]
                item.itemslotchest[10] = item.assignmentinvslot[11]
                item.itemslotchest[11] = item.assignmentinvslot[12]
                item.itemslotchest[12] = item.assignmentinvslot[13]
                item.itemslotchest[13] = item.assignmentinvslot[14]
                item.itemslotchest[14] = item.assignmentinvslot[15]
                item.itemslotchest[15] = item.assignmentinvslot[16]
                item.itemslotchest[16] = item.assignmentinvslot[17]
            if item.inventoryslot4[5] == 'armorarms':
                item.itemslotarms[0] = item.assignmentinvslot[0]
                item.itemslotarms[1] = item.assignmentinvslot[2]
                item.itemslotarms[2] = item.assignmentinvslot[3]
                item.itemslotarms[3] = item.assignmentinvslot[4]
                item.itemslotarms[4] = item.assignmentinvslot[5]
                item.itemslotarms[5] = item.assignmentinvslot[6]
                item.itemslotarms[6] = item.assignmentinvslot[7]
                item.itemslotarms[7] = item.assignmentinvslot[8]
                item.itemslotarms[8] = item.assignmentinvslot[9]
                item.itemslotarms[9] = item.assignmentinvslot[10]
                item.itemslotarms[10] = item.assignmentinvslot[11]
                item.itemslotarms[11] = item.assignmentinvslot[12]
                item.itemslotarms[12] = item.assignmentinvslot[13]
                item.itemslotarms[13] = item.assignmentinvslot[14]
                item.itemslotarms[14] = item.assignmentinvslot[15]
                item.itemslotarms[15] = item.assignmentinvslot[16]
                item.itemslotarms[16] = item.assignmentinvslot[17]    
            if item.inventoryslot4[5] == 'armorhands':
                item.itemslothands[0] = item.assignmentinvslot[0]
                item.itemslothands[1] = item.assignmentinvslot[2]
                item.itemslothands[2] = item.assignmentinvslot[3]
                item.itemslothands[3] = item.assignmentinvslot[4]
                item.itemslothands[4] = item.assignmentinvslot[5]
                item.itemslothands[5] = item.assignmentinvslot[6]
                item.itemslothands[6] = item.assignmentinvslot[7]
                item.itemslothands[7] = item.assignmentinvslot[8]
                item.itemslothands[8] = item.assignmentinvslot[9]
                item.itemslothands[9] = item.assignmentinvslot[10]
                item.itemslothands[10] = item.assignmentinvslot[11]
                item.itemslothands[11] = item.assignmentinvslot[12]
                item.itemslothands[12] = item.assignmentinvslot[13]
                item.itemslothands[13] = item.assignmentinvslot[14]
                item.itemslothands[14] = item.assignmentinvslot[15]
                item.itemslothands[15] = item.assignmentinvslot[16]
                item.itemslothands[16] = item.assignmentinvslot[17]   
            if item.inventoryslot4[5] == 'armorlegs':
                item.itemslotlegs[0] = item.assignmentinvslot[0]
                item.itemslotlegs[1] = item.assignmentinvslot[2]
                item.itemslotlegs[2] = item.assignmentinvslot[3]
                item.itemslotlegs[3] = item.assignmentinvslot[4]
                item.itemslotlegs[4] = item.assignmentinvslot[5]
                item.itemslotlegs[5] = item.assignmentinvslot[6]
                item.itemslotlegs[6] = item.assignmentinvslot[7]
                item.itemslotlegs[7] = item.assignmentinvslot[8]
                item.itemslotlegs[8] = item.assignmentinvslot[9]
                item.itemslotlegs[9] = item.assignmentinvslot[10]
                item.itemslotlegs[10] = item.assignmentinvslot[11]
                item.itemslotlegs[11] = item.assignmentinvslot[12]
                item.itemslotlegs[12] = item.assignmentinvslot[13]
                item.itemslotlegs[13] = item.assignmentinvslot[14]
                item.itemslotlegs[14] = item.assignmentinvslot[15]
                item.itemslotlegs[15] = item.assignmentinvslot[16]
                item.itemslotlegs[16] = item.assignmentinvslot[17]    
            if item.inventoryslot4[5] == 'armorfoot':
                item.itemslotfoot[0] = item.assignmentinvslot[0]
                item.itemslotfoot[1] = item.assignmentinvslot[2]
                item.itemslotfoot[2] = item.assignmentinvslot[3]
                item.itemslotfoot[3] = item.assignmentinvslot[4]
                item.itemslotfoot[4] = item.assignmentinvslot[5]
                item.itemslotfoot[5] = item.assignmentinvslot[6]
                item.itemslotfoot[6] = item.assignmentinvslot[7]
                item.itemslotfoot[7] = item.assignmentinvslot[8]
                item.itemslotfoot[8] = item.assignmentinvslot[9]
                item.itemslotfoot[9] = item.assignmentinvslot[10]
                item.itemslotfoot[10] = item.assignmentinvslot[11]
                item.itemslotfoot[11] = item.assignmentinvslot[12]
                item.itemslotfoot[12] = item.assignmentinvslot[13]
                item.itemslotfoot[13] = item.assignmentinvslot[14]
                item.itemslotfoot[14] = item.assignmentinvslot[15]
                item.itemslotfoot[15] = item.assignmentinvslot[16]
                item.itemslotfoot[16] = item.assignmentinvslot[17]    
            if item.inventoryslot4[5] == 'armoracc':
                if item.itemslotacc1[0] == 0:    
                    item.itemslotacc1[0] = item.assignmentinvslot[0]
                    item.itemslotacc1[1] = item.assignmentinvslot[2]
                    item.itemslotacc1[2] = item.assignmentinvslot[3]
                    item.itemslotacc1[3] = item.assignmentinvslot[4]
                    item.itemslotacc1[4] = item.assignmentinvslot[5]
                    item.itemslotacc1[5] = item.assignmentinvslot[6]
                    item.itemslotacc1[6] = item.assignmentinvslot[7]
                    item.itemslotacc1[7] = item.assignmentinvslot[8]
                    item.itemslotacc1[8] = item.assignmentinvslot[9]
                    item.itemslotacc1[9] = item.assignmentinvslot[10]
                    item.itemslotacc1[10] = item.assignmentinvslot[11]
                    item.itemslotacc1[11] = item.assignmentinvslot[12]
                    item.itemslotacc1[12] = item.assignmentinvslot[13]
                    item.itemslotacc1[13] = item.assignmentinvslot[14]
                    item.itemslotacc1[14] = item.assignmentinvslot[15]
                    item.itemslotacc1[15] = item.assignmentinvslot[16]
                    item.itemslotacc1[16] = item.assignmentinvslot[17] 
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] == 0):
                    item.itemslotacc2[0] = item.assignmentinvslot[0]
                    item.itemslotacc2[1] = item.assignmentinvslot[2]
                    item.itemslotacc2[2] = item.assignmentinvslot[3]
                    item.itemslotacc2[3] = item.assignmentinvslot[4]
                    item.itemslotacc2[4] = item.assignmentinvslot[5]
                    item.itemslotacc2[5] = item.assignmentinvslot[6]
                    item.itemslotacc2[6] = item.assignmentinvslot[7]
                    item.itemslotacc2[7] = item.assignmentinvslot[8]
                    item.itemslotacc2[8] = item.assignmentinvslot[9]
                    item.itemslotacc2[9] = item.assignmentinvslot[10]
                    item.itemslotacc2[10] = item.assignmentinvslot[11]
                    item.itemslotacc2[11] = item.assignmentinvslot[12]
                    item.itemslotacc2[12] = item.assignmentinvslot[13]
                    item.itemslotacc2[13] = item.assignmentinvslot[14]
                    item.itemslotacc2[14] = item.assignmentinvslot[15]
                    item.itemslotacc2[15] = item.assignmentinvslot[16]
                    item.itemslotacc2[16] = item.assignmentinvslot[17]  
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] == 0):
                    item.itemslotacc3[0] = item.assignmentinvslot[0]
                    item.itemslotacc3[1] = item.assignmentinvslot[2]
                    item.itemslotacc3[2] = item.assignmentinvslot[3]
                    item.itemslotacc3[3] = item.assignmentinvslot[4]
                    item.itemslotacc3[4] = item.assignmentinvslot[5]
                    item.itemslotacc3[5] = item.assignmentinvslot[6]
                    item.itemslotacc3[6] = item.assignmentinvslot[7]
                    item.itemslotacc3[7] = item.assignmentinvslot[8]
                    item.itemslotacc3[8] = item.assignmentinvslot[9]
                    item.itemslotacc3[9] = item.assignmentinvslot[10]
                    item.itemslotacc3[10] = item.assignmentinvslot[11]
                    item.itemslotacc3[11] = item.assignmentinvslot[12]
                    item.itemslotacc3[12] = item.assignmentinvslot[13]
                    item.itemslotacc3[13] = item.assignmentinvslot[14]
                    item.itemslotacc3[14] = item.assignmentinvslot[15]
                    item.itemslotacc3[15] = item.assignmentinvslot[16]
                    item.itemslotacc3[16] = item.assignmentinvslot[17]               
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na akcesoria są w użyciu')
            if item.inventoryslot4[5] == 'armoractive': 
                if (item.itemslotactive1[0] == 0):
                    item.itemslotactive1[0] = item.assignmentinvslot[0]
                    item.itemslotactive1[1] = item.assignmentinvslot[2]
                    item.itemslotactive1[2] = item.assignmentinvslot[3]
                    item.itemslotactive1[3] = item.assignmentinvslot[4]
                    item.itemslotactive1[4] = item.assignmentinvslot[5]
                    item.itemslotactive1[5] = item.assignmentinvslot[6]
                    item.itemslotactive1[6] = item.assignmentinvslot[7]
                    item.itemslotactive1[7] = item.assignmentinvslot[8]
                    item.itemslotactive1[8] = item.assignmentinvslot[9]
                    item.itemslotactive1[9] = item.assignmentinvslot[10]
                    item.itemslotactive1[10] = item.assignmentinvslot[11]
                    item.itemslotactive1[11] = item.assignmentinvslot[12]
                    item.itemslotactive1[12] = item.assignmentinvslot[13]
                    item.itemslotactive1[13] = item.assignmentinvslot[14]
                    item.itemslotactive1[14] = item.assignmentinvslot[15]
                    item.itemslotactive1[15] = item.assignmentinvslot[16]
                    item.itemslotactive1[16] = item.assignmentinvslot[17]           
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] == 0):
                    item.itemslotactive2[0] = item.assignmentinvslot[0]
                    item.itemslotactive2[1] = item.assignmentinvslot[2]
                    item.itemslotactive2[2] = item.assignmentinvslot[3]
                    item.itemslotactive2[3] = item.assignmentinvslot[4]
                    item.itemslotactive2[4] = item.assignmentinvslot[5]
                    item.itemslotactive2[5] = item.assignmentinvslot[6]
                    item.itemslotactive2[6] = item.assignmentinvslot[7]
                    item.itemslotactive2[7] = item.assignmentinvslot[8]
                    item.itemslotactive2[8] = item.assignmentinvslot[9]
                    item.itemslotactive2[9] = item.assignmentinvslot[10]
                    item.itemslotactive2[10] = item.assignmentinvslot[11]
                    item.itemslotactive2[11] = item.assignmentinvslot[12]
                    item.itemslotactive2[12] = item.assignmentinvslot[13]
                    item.itemslotactive2[13] = item.assignmentinvslot[14]
                    item.itemslotactive2[14] = item.assignmentinvslot[15]
                    item.itemslotactive2[15] = item.assignmentinvslot[16]
                    item.itemslotactive2[16] = item.assignmentinvslot[17]                
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] == 0):
                    item.itemslotactive3[0] = item.assignmentinvslot[0]
                    item.itemslotactive3[1] = item.assignmentinvslot[2]
                    item.itemslotactive3[2] = item.assignmentinvslot[3]
                    item.itemslotactive3[3] = item.assignmentinvslot[4]
                    item.itemslotactive3[4] = item.assignmentinvslot[5]
                    item.itemslotactive3[5] = item.assignmentinvslot[6]
                    item.itemslotactive3[6] = item.assignmentinvslot[7]
                    item.itemslotactive3[7] = item.assignmentinvslot[8]
                    item.itemslotactive3[8] = item.assignmentinvslot[9]
                    item.itemslotactive3[9] = item.assignmentinvslot[10]
                    item.itemslotactive3[10] = item.assignmentinvslot[11]
                    item.itemslotactive3[11] = item.assignmentinvslot[12]
                    item.itemslotactive3[12] = item.assignmentinvslot[13]
                    item.itemslotactive3[13] = item.assignmentinvslot[14]
                    item.itemslotactive3[14] = item.assignmentinvslot[15]
                    item.itemslotactive3[15] = item.assignmentinvslot[16]
                    item.itemslotactive3[16] = item.assignmentinvslot[17]                 
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] == 0):
                    item.itemslotactive4[0] = item.assignmentinvslot[0]
                    item.itemslotactive4[1] = item.assignmentinvslot[2]
                    item.itemslotactive4[2] = item.assignmentinvslot[3]
                    item.itemslotactive4[3] = item.assignmentinvslot[4]
                    item.itemslotactive4[4] = item.assignmentinvslot[5]
                    item.itemslotactive4[5] = item.assignmentinvslot[6]
                    item.itemslotactive4[6] = item.assignmentinvslot[7]
                    item.itemslotactive4[7] = item.assignmentinvslot[8]
                    item.itemslotactive4[8] = item.assignmentinvslot[9]
                    item.itemslotactive4[9] = item.assignmentinvslot[10]
                    item.itemslotactive4[10] = item.assignmentinvslot[11]
                    item.itemslotactive4[11] = item.assignmentinvslot[12]
                    item.itemslotactive4[12] = item.assignmentinvslot[13]
                    item.itemslotactive4[13] = item.assignmentinvslot[14]
                    item.itemslotactive4[14] = item.assignmentinvslot[15]
                    item.itemslotactive4[15] = item.assignmentinvslot[16]
                    item.itemslotactive4[16] = item.assignmentinvslot[17]    
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] == 0):
                    item.itemslotactive5[0] = item.assignmentinvslot[0]
                    item.itemslotactive5[1] = item.assignmentinvslot[2]
                    item.itemslotactive5[2] = item.assignmentinvslot[3]
                    item.itemslotactive5[3] = item.assignmentinvslot[4]
                    item.itemslotactive5[4] = item.assignmentinvslot[5]
                    item.itemslotactive5[5] = item.assignmentinvslot[6]
                    item.itemslotactive5[6] = item.assignmentinvslot[7]
                    item.itemslotactive5[7] = item.assignmentinvslot[8]
                    item.itemslotactive5[8] = item.assignmentinvslot[9]
                    item.itemslotactive5[9] = item.assignmentinvslot[10]
                    item.itemslotactive5[10] = item.assignmentinvslot[11]
                    item.itemslotactive5[11] = item.assignmentinvslot[12]
                    item.itemslotactive5[12] = item.assignmentinvslot[13]
                    item.itemslotactive5[13] = item.assignmentinvslot[14]
                    item.itemslotactive5[14] = item.assignmentinvslot[15]
                    item.itemslotactive5[15] = item.assignmentinvslot[16]
                    item.itemslotactive5[16] = item.assignmentinvslot[17]     
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] == 0):
                    item.itemslotactive6[0] = item.assignmentinvslot[0]
                    item.itemslotactive6[1] = item.assignmentinvslot[2]
                    item.itemslotactive6[2] = item.assignmentinvslot[3]
                    item.itemslotactive6[3] = item.assignmentinvslot[4]
                    item.itemslotactive6[4] = item.assignmentinvslot[5]
                    item.itemslotactive6[5] = item.assignmentinvslot[6]
                    item.itemslotactive6[6] = item.assignmentinvslot[7]
                    item.itemslotactive6[7] = item.assignmentinvslot[8]
                    item.itemslotactive6[8] = item.assignmentinvslot[9]
                    item.itemslotactive6[9] = item.assignmentinvslot[10]
                    item.itemslotactive6[10] = item.assignmentinvslot[11]
                    item.itemslotactive6[11] = item.assignmentinvslot[12]
                    item.itemslotactive6[12] = item.assignmentinvslot[13]
                    item.itemslotactive6[13] = item.assignmentinvslot[14]
                    item.itemslotactive6[14] = item.assignmentinvslot[15]
                    item.itemslotactive6[15] = item.assignmentinvslot[16]
                    item.itemslotactive6[16] = item.assignmentinvslot[17]                   
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na przedmioty aktywne są w użyciu')
        if (item.inventoryslot5[4] == lookforinv) and (item.inventoryslot5[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot5
            if item.inventoryslot5[5] == 'armorhead':
                item.itemslothead[0] = item.assignmentinvslot[0]
                item.itemslothead[1] = item.assignmentinvslot[2]
                item.itemslothead[2] = item.assignmentinvslot[3]
                item.itemslothead[3] = item.assignmentinvslot[4]
                item.itemslothead[4] = item.assignmentinvslot[5]
                item.itemslothead[5] = item.assignmentinvslot[6]
                item.itemslothead[6] = item.assignmentinvslot[7]
                item.itemslothead[7] = item.assignmentinvslot[8]
                item.itemslothead[8] = item.assignmentinvslot[9]
                item.itemslothead[9] = item.assignmentinvslot[10]
                item.itemslothead[10] = item.assignmentinvslot[11]
                item.itemslothead[11] = item.assignmentinvslot[12]
                item.itemslothead[12] = item.assignmentinvslot[13]
                item.itemslothead[13] = item.assignmentinvslot[14]
                item.itemslothead[14] = item.assignmentinvslot[15]
                item.itemslothead[15] = item.assignmentinvslot[16]
                item.itemslothead[16] = item.assignmentinvslot[17]
            if item.inventoryslot5[5] == 'armorchest':
                item.itemslotchest[0] = item.assignmentinvslot[0]
                item.itemslotchest[1] = item.assignmentinvslot[2]
                item.itemslotchest[2] = item.assignmentinvslot[3]
                item.itemslotchest[3] = item.assignmentinvslot[4]
                item.itemslotchest[4] = item.assignmentinvslot[5]
                item.itemslotchest[5] = item.assignmentinvslot[6]
                item.itemslotchest[6] = item.assignmentinvslot[7]
                item.itemslotchest[7] = item.assignmentinvslot[8]
                item.itemslotchest[8] = item.assignmentinvslot[9]
                item.itemslotchest[9] = item.assignmentinvslot[10]
                item.itemslotchest[10] = item.assignmentinvslot[11]
                item.itemslotchest[11] = item.assignmentinvslot[12]
                item.itemslotchest[12] = item.assignmentinvslot[13]
                item.itemslotchest[13] = item.assignmentinvslot[14]
                item.itemslotchest[14] = item.assignmentinvslot[15]
                item.itemslotchest[15] = item.assignmentinvslot[16]
                item.itemslotchest[16] = item.assignmentinvslot[17]
            if item.inventoryslot5[5] == 'armorarms':
                item.itemslotarms[0] = item.assignmentinvslot[0]
                item.itemslotarms[1] = item.assignmentinvslot[2]
                item.itemslotarms[2] = item.assignmentinvslot[3]
                item.itemslotarms[3] = item.assignmentinvslot[4]
                item.itemslotarms[4] = item.assignmentinvslot[5]
                item.itemslotarms[5] = item.assignmentinvslot[6]
                item.itemslotarms[6] = item.assignmentinvslot[7]
                item.itemslotarms[7] = item.assignmentinvslot[8]
                item.itemslotarms[8] = item.assignmentinvslot[9]
                item.itemslotarms[9] = item.assignmentinvslot[10]
                item.itemslotarms[10] = item.assignmentinvslot[11]
                item.itemslotarms[11] = item.assignmentinvslot[12]
                item.itemslotarms[12] = item.assignmentinvslot[13]
                item.itemslotarms[13] = item.assignmentinvslot[14]
                item.itemslotarms[14] = item.assignmentinvslot[15]
                item.itemslotarms[15] = item.assignmentinvslot[16]
                item.itemslotarms[16] = item.assignmentinvslot[17]    
            if item.inventoryslot5[5] == 'armorhands':
                item.itemslothands[0] = item.assignmentinvslot[0]
                item.itemslothands[1] = item.assignmentinvslot[2]
                item.itemslothands[2] = item.assignmentinvslot[3]
                item.itemslothands[3] = item.assignmentinvslot[4]
                item.itemslothands[4] = item.assignmentinvslot[5]
                item.itemslothands[5] = item.assignmentinvslot[6]
                item.itemslothands[6] = item.assignmentinvslot[7]
                item.itemslothands[7] = item.assignmentinvslot[8]
                item.itemslothands[8] = item.assignmentinvslot[9]
                item.itemslothands[9] = item.assignmentinvslot[10]
                item.itemslothands[10] = item.assignmentinvslot[11]
                item.itemslothands[11] = item.assignmentinvslot[12]
                item.itemslothands[12] = item.assignmentinvslot[13]
                item.itemslothands[13] = item.assignmentinvslot[14]
                item.itemslothands[14] = item.assignmentinvslot[15]
                item.itemslothands[15] = item.assignmentinvslot[16]
                item.itemslothands[16] = item.assignmentinvslot[17]   
            if item.inventoryslot5[5] == 'armorlegs':
                item.itemslotlegs[0] = item.assignmentinvslot[0]
                item.itemslotlegs[1] = item.assignmentinvslot[2]
                item.itemslotlegs[2] = item.assignmentinvslot[3]
                item.itemslotlegs[3] = item.assignmentinvslot[4]
                item.itemslotlegs[4] = item.assignmentinvslot[5]
                item.itemslotlegs[5] = item.assignmentinvslot[6]
                item.itemslotlegs[6] = item.assignmentinvslot[7]
                item.itemslotlegs[7] = item.assignmentinvslot[8]
                item.itemslotlegs[8] = item.assignmentinvslot[9]
                item.itemslotlegs[9] = item.assignmentinvslot[10]
                item.itemslotlegs[10] = item.assignmentinvslot[11]
                item.itemslotlegs[11] = item.assignmentinvslot[12]
                item.itemslotlegs[12] = item.assignmentinvslot[13]
                item.itemslotlegs[13] = item.assignmentinvslot[14]
                item.itemslotlegs[14] = item.assignmentinvslot[15]
                item.itemslotlegs[15] = item.assignmentinvslot[16]
                item.itemslotlegs[16] = item.assignmentinvslot[17]    
            if item.inventoryslot5[5] == 'armorfoot':
                item.itemslotfoot[0] = item.assignmentinvslot[0]
                item.itemslotfoot[1] = item.assignmentinvslot[2]
                item.itemslotfoot[2] = item.assignmentinvslot[3]
                item.itemslotfoot[3] = item.assignmentinvslot[4]
                item.itemslotfoot[4] = item.assignmentinvslot[5]
                item.itemslotfoot[5] = item.assignmentinvslot[6]
                item.itemslotfoot[6] = item.assignmentinvslot[7]
                item.itemslotfoot[7] = item.assignmentinvslot[8]
                item.itemslotfoot[8] = item.assignmentinvslot[9]
                item.itemslotfoot[9] = item.assignmentinvslot[10]
                item.itemslotfoot[10] = item.assignmentinvslot[11]
                item.itemslotfoot[11] = item.assignmentinvslot[12]
                item.itemslotfoot[12] = item.assignmentinvslot[13]
                item.itemslotfoot[13] = item.assignmentinvslot[14]
                item.itemslotfoot[14] = item.assignmentinvslot[15]
                item.itemslotfoot[15] = item.assignmentinvslot[16]
                item.itemslotfoot[16] = item.assignmentinvslot[17]    
            if item.inventoryslot5[5] == 'armoracc':
                if item.itemslotacc1[0] == 0:    
                    item.itemslotacc1[0] = item.assignmentinvslot[0]
                    item.itemslotacc1[1] = item.assignmentinvslot[2]
                    item.itemslotacc1[2] = item.assignmentinvslot[3]
                    item.itemslotacc1[3] = item.assignmentinvslot[4]
                    item.itemslotacc1[4] = item.assignmentinvslot[5]
                    item.itemslotacc1[5] = item.assignmentinvslot[6]
                    item.itemslotacc1[6] = item.assignmentinvslot[7]
                    item.itemslotacc1[7] = item.assignmentinvslot[8]
                    item.itemslotacc1[8] = item.assignmentinvslot[9]
                    item.itemslotacc1[9] = item.assignmentinvslot[10]
                    item.itemslotacc1[10] = item.assignmentinvslot[11]
                    item.itemslotacc1[11] = item.assignmentinvslot[12]
                    item.itemslotacc1[12] = item.assignmentinvslot[13]
                    item.itemslotacc1[13] = item.assignmentinvslot[14]
                    item.itemslotacc1[14] = item.assignmentinvslot[15]
                    item.itemslotacc1[15] = item.assignmentinvslot[16]
                    item.itemslotacc1[16] = item.assignmentinvslot[17] 
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] == 0):
                    item.itemslotacc2[0] = item.assignmentinvslot[0]
                    item.itemslotacc2[1] = item.assignmentinvslot[2]
                    item.itemslotacc2[2] = item.assignmentinvslot[3]
                    item.itemslotacc2[3] = item.assignmentinvslot[4]
                    item.itemslotacc2[4] = item.assignmentinvslot[5]
                    item.itemslotacc2[5] = item.assignmentinvslot[6]
                    item.itemslotacc2[6] = item.assignmentinvslot[7]
                    item.itemslotacc2[7] = item.assignmentinvslot[8]
                    item.itemslotacc2[8] = item.assignmentinvslot[9]
                    item.itemslotacc2[9] = item.assignmentinvslot[10]
                    item.itemslotacc2[10] = item.assignmentinvslot[11]
                    item.itemslotacc2[11] = item.assignmentinvslot[12]
                    item.itemslotacc2[12] = item.assignmentinvslot[13]
                    item.itemslotacc2[13] = item.assignmentinvslot[14]
                    item.itemslotacc2[14] = item.assignmentinvslot[15]
                    item.itemslotacc2[15] = item.assignmentinvslot[16]
                    item.itemslotacc2[16] = item.assignmentinvslot[17]  
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] == 0):
                    item.itemslotacc3[0] = item.assignmentinvslot[0]
                    item.itemslotacc3[1] = item.assignmentinvslot[2]
                    item.itemslotacc3[2] = item.assignmentinvslot[3]
                    item.itemslotacc3[3] = item.assignmentinvslot[4]
                    item.itemslotacc3[4] = item.assignmentinvslot[5]
                    item.itemslotacc3[5] = item.assignmentinvslot[6]
                    item.itemslotacc3[6] = item.assignmentinvslot[7]
                    item.itemslotacc3[7] = item.assignmentinvslot[8]
                    item.itemslotacc3[8] = item.assignmentinvslot[9]
                    item.itemslotacc3[9] = item.assignmentinvslot[10]
                    item.itemslotacc3[10] = item.assignmentinvslot[11]
                    item.itemslotacc3[11] = item.assignmentinvslot[12]
                    item.itemslotacc3[12] = item.assignmentinvslot[13]
                    item.itemslotacc3[13] = item.assignmentinvslot[14]
                    item.itemslotacc3[14] = item.assignmentinvslot[15]
                    item.itemslotacc3[15] = item.assignmentinvslot[16]
                    item.itemslotacc3[16] = item.assignmentinvslot[17]               
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na akcesoria są w użyciu')
            if item.inventoryslot5[5] == 'armoractive': 
                if (item.itemslotactive1[0] == 0):
                    item.itemslotactive1[0] = item.assignmentinvslot[0]
                    item.itemslotactive1[1] = item.assignmentinvslot[2]
                    item.itemslotactive1[2] = item.assignmentinvslot[3]
                    item.itemslotactive1[3] = item.assignmentinvslot[4]
                    item.itemslotactive1[4] = item.assignmentinvslot[5]
                    item.itemslotactive1[5] = item.assignmentinvslot[6]
                    item.itemslotactive1[6] = item.assignmentinvslot[7]
                    item.itemslotactive1[7] = item.assignmentinvslot[8]
                    item.itemslotactive1[8] = item.assignmentinvslot[9]
                    item.itemslotactive1[9] = item.assignmentinvslot[10]
                    item.itemslotactive1[10] = item.assignmentinvslot[11]
                    item.itemslotactive1[11] = item.assignmentinvslot[12]
                    item.itemslotactive1[12] = item.assignmentinvslot[13]
                    item.itemslotactive1[13] = item.assignmentinvslot[14]
                    item.itemslotactive1[14] = item.assignmentinvslot[15]
                    item.itemslotactive1[15] = item.assignmentinvslot[16]
                    item.itemslotactive1[16] = item.assignmentinvslot[17]           
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] == 0):
                    item.itemslotactive2[0] = item.assignmentinvslot[0]
                    item.itemslotactive2[1] = item.assignmentinvslot[2]
                    item.itemslotactive2[2] = item.assignmentinvslot[3]
                    item.itemslotactive2[3] = item.assignmentinvslot[4]
                    item.itemslotactive2[4] = item.assignmentinvslot[5]
                    item.itemslotactive2[5] = item.assignmentinvslot[6]
                    item.itemslotactive2[6] = item.assignmentinvslot[7]
                    item.itemslotactive2[7] = item.assignmentinvslot[8]
                    item.itemslotactive2[8] = item.assignmentinvslot[9]
                    item.itemslotactive2[9] = item.assignmentinvslot[10]
                    item.itemslotactive2[10] = item.assignmentinvslot[11]
                    item.itemslotactive2[11] = item.assignmentinvslot[12]
                    item.itemslotactive2[12] = item.assignmentinvslot[13]
                    item.itemslotactive2[13] = item.assignmentinvslot[14]
                    item.itemslotactive2[14] = item.assignmentinvslot[15]
                    item.itemslotactive2[15] = item.assignmentinvslot[16]
                    item.itemslotactive2[16] = item.assignmentinvslot[17]                
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] == 0):
                    item.itemslotactive3[0] = item.assignmentinvslot[0]
                    item.itemslotactive3[1] = item.assignmentinvslot[2]
                    item.itemslotactive3[2] = item.assignmentinvslot[3]
                    item.itemslotactive3[3] = item.assignmentinvslot[4]
                    item.itemslotactive3[4] = item.assignmentinvslot[5]
                    item.itemslotactive3[5] = item.assignmentinvslot[6]
                    item.itemslotactive3[6] = item.assignmentinvslot[7]
                    item.itemslotactive3[7] = item.assignmentinvslot[8]
                    item.itemslotactive3[8] = item.assignmentinvslot[9]
                    item.itemslotactive3[9] = item.assignmentinvslot[10]
                    item.itemslotactive3[10] = item.assignmentinvslot[11]
                    item.itemslotactive3[11] = item.assignmentinvslot[12]
                    item.itemslotactive3[12] = item.assignmentinvslot[13]
                    item.itemslotactive3[13] = item.assignmentinvslot[14]
                    item.itemslotactive3[14] = item.assignmentinvslot[15]
                    item.itemslotactive3[15] = item.assignmentinvslot[16]
                    item.itemslotactive3[16] = item.assignmentinvslot[17]                 
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] == 0):
                    item.itemslotactive4[0] = item.assignmentinvslot[0]
                    item.itemslotactive4[1] = item.assignmentinvslot[2]
                    item.itemslotactive4[2] = item.assignmentinvslot[3]
                    item.itemslotactive4[3] = item.assignmentinvslot[4]
                    item.itemslotactive4[4] = item.assignmentinvslot[5]
                    item.itemslotactive4[5] = item.assignmentinvslot[6]
                    item.itemslotactive4[6] = item.assignmentinvslot[7]
                    item.itemslotactive4[7] = item.assignmentinvslot[8]
                    item.itemslotactive4[8] = item.assignmentinvslot[9]
                    item.itemslotactive4[9] = item.assignmentinvslot[10]
                    item.itemslotactive4[10] = item.assignmentinvslot[11]
                    item.itemslotactive4[11] = item.assignmentinvslot[12]
                    item.itemslotactive4[12] = item.assignmentinvslot[13]
                    item.itemslotactive4[13] = item.assignmentinvslot[14]
                    item.itemslotactive4[14] = item.assignmentinvslot[15]
                    item.itemslotactive4[15] = item.assignmentinvslot[16]
                    item.itemslotactive4[16] = item.assignmentinvslot[17]    
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] == 0):
                    item.itemslotactive5[0] = item.assignmentinvslot[0]
                    item.itemslotactive5[1] = item.assignmentinvslot[2]
                    item.itemslotactive5[2] = item.assignmentinvslot[3]
                    item.itemslotactive5[3] = item.assignmentinvslot[4]
                    item.itemslotactive5[4] = item.assignmentinvslot[5]
                    item.itemslotactive5[5] = item.assignmentinvslot[6]
                    item.itemslotactive5[6] = item.assignmentinvslot[7]
                    item.itemslotactive5[7] = item.assignmentinvslot[8]
                    item.itemslotactive5[8] = item.assignmentinvslot[9]
                    item.itemslotactive5[9] = item.assignmentinvslot[10]
                    item.itemslotactive5[10] = item.assignmentinvslot[11]
                    item.itemslotactive5[11] = item.assignmentinvslot[12]
                    item.itemslotactive5[12] = item.assignmentinvslot[13]
                    item.itemslotactive5[13] = item.assignmentinvslot[14]
                    item.itemslotactive5[14] = item.assignmentinvslot[15]
                    item.itemslotactive5[15] = item.assignmentinvslot[16]
                    item.itemslotactive5[16] = item.assignmentinvslot[17]     
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] == 0):
                    item.itemslotactive6[0] = item.assignmentinvslot[0]
                    item.itemslotactive6[1] = item.assignmentinvslot[2]
                    item.itemslotactive6[2] = item.assignmentinvslot[3]
                    item.itemslotactive6[3] = item.assignmentinvslot[4]
                    item.itemslotactive6[4] = item.assignmentinvslot[5]
                    item.itemslotactive6[5] = item.assignmentinvslot[6]
                    item.itemslotactive6[6] = item.assignmentinvslot[7]
                    item.itemslotactive6[7] = item.assignmentinvslot[8]
                    item.itemslotactive6[8] = item.assignmentinvslot[9]
                    item.itemslotactive6[9] = item.assignmentinvslot[10]
                    item.itemslotactive6[10] = item.assignmentinvslot[11]
                    item.itemslotactive6[11] = item.assignmentinvslot[12]
                    item.itemslotactive6[12] = item.assignmentinvslot[13]
                    item.itemslotactive6[13] = item.assignmentinvslot[14]
                    item.itemslotactive6[14] = item.assignmentinvslot[15]
                    item.itemslotactive6[15] = item.assignmentinvslot[16]
                    item.itemslotactive6[16] = item.assignmentinvslot[17]                   
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na przedmioty aktywne są w użyciu')
        if (item.inventoryslot6[4] == lookforinv) and (item.inventoryslot6[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot6
            if item.inventoryslot6[5] == 'armorhead':
                item.itemslothead[0] = item.assignmentinvslot[0]
                item.itemslothead[1] = item.assignmentinvslot[2]
                item.itemslothead[2] = item.assignmentinvslot[3]
                item.itemslothead[3] = item.assignmentinvslot[4]
                item.itemslothead[4] = item.assignmentinvslot[5]
                item.itemslothead[5] = item.assignmentinvslot[6]
                item.itemslothead[6] = item.assignmentinvslot[7]
                item.itemslothead[7] = item.assignmentinvslot[8]
                item.itemslothead[8] = item.assignmentinvslot[9]
                item.itemslothead[9] = item.assignmentinvslot[10]
                item.itemslothead[10] = item.assignmentinvslot[11]
                item.itemslothead[11] = item.assignmentinvslot[12]
                item.itemslothead[12] = item.assignmentinvslot[13]
                item.itemslothead[13] = item.assignmentinvslot[14]
                item.itemslothead[14] = item.assignmentinvslot[15]
                item.itemslothead[15] = item.assignmentinvslot[16]
                item.itemslothead[16] = item.assignmentinvslot[17]
            if item.inventoryslot6[5] == 'armorchest':
                item.itemslotchest[0] = item.assignmentinvslot[0]
                item.itemslotchest[1] = item.assignmentinvslot[2]
                item.itemslotchest[2] = item.assignmentinvslot[3]
                item.itemslotchest[3] = item.assignmentinvslot[4]
                item.itemslotchest[4] = item.assignmentinvslot[5]
                item.itemslotchest[5] = item.assignmentinvslot[6]
                item.itemslotchest[6] = item.assignmentinvslot[7]
                item.itemslotchest[7] = item.assignmentinvslot[8]
                item.itemslotchest[8] = item.assignmentinvslot[9]
                item.itemslotchest[9] = item.assignmentinvslot[10]
                item.itemslotchest[10] = item.assignmentinvslot[11]
                item.itemslotchest[11] = item.assignmentinvslot[12]
                item.itemslotchest[12] = item.assignmentinvslot[13]
                item.itemslotchest[13] = item.assignmentinvslot[14]
                item.itemslotchest[14] = item.assignmentinvslot[15]
                item.itemslotchest[15] = item.assignmentinvslot[16]
                item.itemslotchest[16] = item.assignmentinvslot[17]
            if item.inventoryslot6[5] == 'armorarms':
                item.itemslotarms[0] = item.assignmentinvslot[0]
                item.itemslotarms[1] = item.assignmentinvslot[2]
                item.itemslotarms[2] = item.assignmentinvslot[3]
                item.itemslotarms[3] = item.assignmentinvslot[4]
                item.itemslotarms[4] = item.assignmentinvslot[5]
                item.itemslotarms[5] = item.assignmentinvslot[6]
                item.itemslotarms[6] = item.assignmentinvslot[7]
                item.itemslotarms[7] = item.assignmentinvslot[8]
                item.itemslotarms[8] = item.assignmentinvslot[9]
                item.itemslotarms[9] = item.assignmentinvslot[10]
                item.itemslotarms[10] = item.assignmentinvslot[11]
                item.itemslotarms[11] = item.assignmentinvslot[12]
                item.itemslotarms[12] = item.assignmentinvslot[13]
                item.itemslotarms[13] = item.assignmentinvslot[14]
                item.itemslotarms[14] = item.assignmentinvslot[15]
                item.itemslotarms[15] = item.assignmentinvslot[16]
                item.itemslotarms[16] = item.assignmentinvslot[17]    
            if item.inventoryslot6[5] == 'armorhands':
                item.itemslothands[0] = item.assignmentinvslot[0]
                item.itemslothands[1] = item.assignmentinvslot[2]
                item.itemslothands[2] = item.assignmentinvslot[3]
                item.itemslothands[3] = item.assignmentinvslot[4]
                item.itemslothands[4] = item.assignmentinvslot[5]
                item.itemslothands[5] = item.assignmentinvslot[6]
                item.itemslothands[6] = item.assignmentinvslot[7]
                item.itemslothands[7] = item.assignmentinvslot[8]
                item.itemslothands[8] = item.assignmentinvslot[9]
                item.itemslothands[9] = item.assignmentinvslot[10]
                item.itemslothands[10] = item.assignmentinvslot[11]
                item.itemslothands[11] = item.assignmentinvslot[12]
                item.itemslothands[12] = item.assignmentinvslot[13]
                item.itemslothands[13] = item.assignmentinvslot[14]
                item.itemslothands[14] = item.assignmentinvslot[15]
                item.itemslothands[15] = item.assignmentinvslot[16]
                item.itemslothands[16] = item.assignmentinvslot[17]   
            if item.inventoryslot6[5] == 'armorlegs':
                item.itemslotlegs[0] = item.assignmentinvslot[0]
                item.itemslotlegs[1] = item.assignmentinvslot[2]
                item.itemslotlegs[2] = item.assignmentinvslot[3]
                item.itemslotlegs[3] = item.assignmentinvslot[4]
                item.itemslotlegs[4] = item.assignmentinvslot[5]
                item.itemslotlegs[5] = item.assignmentinvslot[6]
                item.itemslotlegs[6] = item.assignmentinvslot[7]
                item.itemslotlegs[7] = item.assignmentinvslot[8]
                item.itemslotlegs[8] = item.assignmentinvslot[9]
                item.itemslotlegs[9] = item.assignmentinvslot[10]
                item.itemslotlegs[10] = item.assignmentinvslot[11]
                item.itemslotlegs[11] = item.assignmentinvslot[12]
                item.itemslotlegs[12] = item.assignmentinvslot[13]
                item.itemslotlegs[13] = item.assignmentinvslot[14]
                item.itemslotlegs[14] = item.assignmentinvslot[15]
                item.itemslotlegs[15] = item.assignmentinvslot[16]
                item.itemslotlegs[16] = item.assignmentinvslot[17]    
            if item.inventoryslot6[5] == 'armorfoot':
                item.itemslotfoot[0] = item.assignmentinvslot[0]
                item.itemslotfoot[1] = item.assignmentinvslot[2]
                item.itemslotfoot[2] = item.assignmentinvslot[3]
                item.itemslotfoot[3] = item.assignmentinvslot[4]
                item.itemslotfoot[4] = item.assignmentinvslot[5]
                item.itemslotfoot[5] = item.assignmentinvslot[6]
                item.itemslotfoot[6] = item.assignmentinvslot[7]
                item.itemslotfoot[7] = item.assignmentinvslot[8]
                item.itemslotfoot[8] = item.assignmentinvslot[9]
                item.itemslotfoot[9] = item.assignmentinvslot[10]
                item.itemslotfoot[10] = item.assignmentinvslot[11]
                item.itemslotfoot[11] = item.assignmentinvslot[12]
                item.itemslotfoot[12] = item.assignmentinvslot[13]
                item.itemslotfoot[13] = item.assignmentinvslot[14]
                item.itemslotfoot[14] = item.assignmentinvslot[15]
                item.itemslotfoot[15] = item.assignmentinvslot[16]
                item.itemslotfoot[16] = item.assignmentinvslot[17]    
            if item.inventoryslot6[5] == 'armoracc':
                if item.itemslotacc1[0] == 0:    
                    item.itemslotacc1[0] = item.assignmentinvslot[0]
                    item.itemslotacc1[1] = item.assignmentinvslot[2]
                    item.itemslotacc1[2] = item.assignmentinvslot[3]
                    item.itemslotacc1[3] = item.assignmentinvslot[4]
                    item.itemslotacc1[4] = item.assignmentinvslot[5]
                    item.itemslotacc1[5] = item.assignmentinvslot[6]
                    item.itemslotacc1[6] = item.assignmentinvslot[7]
                    item.itemslotacc1[7] = item.assignmentinvslot[8]
                    item.itemslotacc1[8] = item.assignmentinvslot[9]
                    item.itemslotacc1[9] = item.assignmentinvslot[10]
                    item.itemslotacc1[10] = item.assignmentinvslot[11]
                    item.itemslotacc1[11] = item.assignmentinvslot[12]
                    item.itemslotacc1[12] = item.assignmentinvslot[13]
                    item.itemslotacc1[13] = item.assignmentinvslot[14]
                    item.itemslotacc1[14] = item.assignmentinvslot[15]
                    item.itemslotacc1[15] = item.assignmentinvslot[16]
                    item.itemslotacc1[16] = item.assignmentinvslot[17] 
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] == 0):
                    item.itemslotacc2[0] = item.assignmentinvslot[0]
                    item.itemslotacc2[1] = item.assignmentinvslot[2]
                    item.itemslotacc2[2] = item.assignmentinvslot[3]
                    item.itemslotacc2[3] = item.assignmentinvslot[4]
                    item.itemslotacc2[4] = item.assignmentinvslot[5]
                    item.itemslotacc2[5] = item.assignmentinvslot[6]
                    item.itemslotacc2[6] = item.assignmentinvslot[7]
                    item.itemslotacc2[7] = item.assignmentinvslot[8]
                    item.itemslotacc2[8] = item.assignmentinvslot[9]
                    item.itemslotacc2[9] = item.assignmentinvslot[10]
                    item.itemslotacc2[10] = item.assignmentinvslot[11]
                    item.itemslotacc2[11] = item.assignmentinvslot[12]
                    item.itemslotacc2[12] = item.assignmentinvslot[13]
                    item.itemslotacc2[13] = item.assignmentinvslot[14]
                    item.itemslotacc2[14] = item.assignmentinvslot[15]
                    item.itemslotacc2[15] = item.assignmentinvslot[16]
                    item.itemslotacc2[16] = item.assignmentinvslot[17]  
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] == 0):
                    item.itemslotacc3[0] = item.assignmentinvslot[0]
                    item.itemslotacc3[1] = item.assignmentinvslot[2]
                    item.itemslotacc3[2] = item.assignmentinvslot[3]
                    item.itemslotacc3[3] = item.assignmentinvslot[4]
                    item.itemslotacc3[4] = item.assignmentinvslot[5]
                    item.itemslotacc3[5] = item.assignmentinvslot[6]
                    item.itemslotacc3[6] = item.assignmentinvslot[7]
                    item.itemslotacc3[7] = item.assignmentinvslot[8]
                    item.itemslotacc3[8] = item.assignmentinvslot[9]
                    item.itemslotacc3[9] = item.assignmentinvslot[10]
                    item.itemslotacc3[10] = item.assignmentinvslot[11]
                    item.itemslotacc3[11] = item.assignmentinvslot[12]
                    item.itemslotacc3[12] = item.assignmentinvslot[13]
                    item.itemslotacc3[13] = item.assignmentinvslot[14]
                    item.itemslotacc3[14] = item.assignmentinvslot[15]
                    item.itemslotacc3[15] = item.assignmentinvslot[16]
                    item.itemslotacc3[16] = item.assignmentinvslot[17]               
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na akcesoria są w użyciu')
            if item.inventoryslot6[5] == 'armoractive': 
                if (item.itemslotactive1[0] == 0):
                    item.itemslotactive1[0] = item.assignmentinvslot[0]
                    item.itemslotactive1[1] = item.assignmentinvslot[2]
                    item.itemslotactive1[2] = item.assignmentinvslot[3]
                    item.itemslotactive1[3] = item.assignmentinvslot[4]
                    item.itemslotactive1[4] = item.assignmentinvslot[5]
                    item.itemslotactive1[5] = item.assignmentinvslot[6]
                    item.itemslotactive1[6] = item.assignmentinvslot[7]
                    item.itemslotactive1[7] = item.assignmentinvslot[8]
                    item.itemslotactive1[8] = item.assignmentinvslot[9]
                    item.itemslotactive1[9] = item.assignmentinvslot[10]
                    item.itemslotactive1[10] = item.assignmentinvslot[11]
                    item.itemslotactive1[11] = item.assignmentinvslot[12]
                    item.itemslotactive1[12] = item.assignmentinvslot[13]
                    item.itemslotactive1[13] = item.assignmentinvslot[14]
                    item.itemslotactive1[14] = item.assignmentinvslot[15]
                    item.itemslotactive1[15] = item.assignmentinvslot[16]
                    item.itemslotactive1[16] = item.assignmentinvslot[17]           
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] == 0):
                    item.itemslotactive2[0] = item.assignmentinvslot[0]
                    item.itemslotactive2[1] = item.assignmentinvslot[2]
                    item.itemslotactive2[2] = item.assignmentinvslot[3]
                    item.itemslotactive2[3] = item.assignmentinvslot[4]
                    item.itemslotactive2[4] = item.assignmentinvslot[5]
                    item.itemslotactive2[5] = item.assignmentinvslot[6]
                    item.itemslotactive2[6] = item.assignmentinvslot[7]
                    item.itemslotactive2[7] = item.assignmentinvslot[8]
                    item.itemslotactive2[8] = item.assignmentinvslot[9]
                    item.itemslotactive2[9] = item.assignmentinvslot[10]
                    item.itemslotactive2[10] = item.assignmentinvslot[11]
                    item.itemslotactive2[11] = item.assignmentinvslot[12]
                    item.itemslotactive2[12] = item.assignmentinvslot[13]
                    item.itemslotactive2[13] = item.assignmentinvslot[14]
                    item.itemslotactive2[14] = item.assignmentinvslot[15]
                    item.itemslotactive2[15] = item.assignmentinvslot[16]
                    item.itemslotactive2[16] = item.assignmentinvslot[17]                
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] == 0):
                    item.itemslotactive3[0] = item.assignmentinvslot[0]
                    item.itemslotactive3[1] = item.assignmentinvslot[2]
                    item.itemslotactive3[2] = item.assignmentinvslot[3]
                    item.itemslotactive3[3] = item.assignmentinvslot[4]
                    item.itemslotactive3[4] = item.assignmentinvslot[5]
                    item.itemslotactive3[5] = item.assignmentinvslot[6]
                    item.itemslotactive3[6] = item.assignmentinvslot[7]
                    item.itemslotactive3[7] = item.assignmentinvslot[8]
                    item.itemslotactive3[8] = item.assignmentinvslot[9]
                    item.itemslotactive3[9] = item.assignmentinvslot[10]
                    item.itemslotactive3[10] = item.assignmentinvslot[11]
                    item.itemslotactive3[11] = item.assignmentinvslot[12]
                    item.itemslotactive3[12] = item.assignmentinvslot[13]
                    item.itemslotactive3[13] = item.assignmentinvslot[14]
                    item.itemslotactive3[14] = item.assignmentinvslot[15]
                    item.itemslotactive3[15] = item.assignmentinvslot[16]
                    item.itemslotactive3[16] = item.assignmentinvslot[17]                 
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] == 0):
                    item.itemslotactive4[0] = item.assignmentinvslot[0]
                    item.itemslotactive4[1] = item.assignmentinvslot[2]
                    item.itemslotactive4[2] = item.assignmentinvslot[3]
                    item.itemslotactive4[3] = item.assignmentinvslot[4]
                    item.itemslotactive4[4] = item.assignmentinvslot[5]
                    item.itemslotactive4[5] = item.assignmentinvslot[6]
                    item.itemslotactive4[6] = item.assignmentinvslot[7]
                    item.itemslotactive4[7] = item.assignmentinvslot[8]
                    item.itemslotactive4[8] = item.assignmentinvslot[9]
                    item.itemslotactive4[9] = item.assignmentinvslot[10]
                    item.itemslotactive4[10] = item.assignmentinvslot[11]
                    item.itemslotactive4[11] = item.assignmentinvslot[12]
                    item.itemslotactive4[12] = item.assignmentinvslot[13]
                    item.itemslotactive4[13] = item.assignmentinvslot[14]
                    item.itemslotactive4[14] = item.assignmentinvslot[15]
                    item.itemslotactive4[15] = item.assignmentinvslot[16]
                    item.itemslotactive4[16] = item.assignmentinvslot[17]    
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] == 0):
                    item.itemslotactive5[0] = item.assignmentinvslot[0]
                    item.itemslotactive5[1] = item.assignmentinvslot[2]
                    item.itemslotactive5[2] = item.assignmentinvslot[3]
                    item.itemslotactive5[3] = item.assignmentinvslot[4]
                    item.itemslotactive5[4] = item.assignmentinvslot[5]
                    item.itemslotactive5[5] = item.assignmentinvslot[6]
                    item.itemslotactive5[6] = item.assignmentinvslot[7]
                    item.itemslotactive5[7] = item.assignmentinvslot[8]
                    item.itemslotactive5[8] = item.assignmentinvslot[9]
                    item.itemslotactive5[9] = item.assignmentinvslot[10]
                    item.itemslotactive5[10] = item.assignmentinvslot[11]
                    item.itemslotactive5[11] = item.assignmentinvslot[12]
                    item.itemslotactive5[12] = item.assignmentinvslot[13]
                    item.itemslotactive5[13] = item.assignmentinvslot[14]
                    item.itemslotactive5[14] = item.assignmentinvslot[15]
                    item.itemslotactive5[15] = item.assignmentinvslot[16]
                    item.itemslotactive5[16] = item.assignmentinvslot[17]     
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] == 0):
                    item.itemslotactive6[0] = item.assignmentinvslot[0]
                    item.itemslotactive6[1] = item.assignmentinvslot[2]
                    item.itemslotactive6[2] = item.assignmentinvslot[3]
                    item.itemslotactive6[3] = item.assignmentinvslot[4]
                    item.itemslotactive6[4] = item.assignmentinvslot[5]
                    item.itemslotactive6[5] = item.assignmentinvslot[6]
                    item.itemslotactive6[6] = item.assignmentinvslot[7]
                    item.itemslotactive6[7] = item.assignmentinvslot[8]
                    item.itemslotactive6[8] = item.assignmentinvslot[9]
                    item.itemslotactive6[9] = item.assignmentinvslot[10]
                    item.itemslotactive6[10] = item.assignmentinvslot[11]
                    item.itemslotactive6[11] = item.assignmentinvslot[12]
                    item.itemslotactive6[12] = item.assignmentinvslot[13]
                    item.itemslotactive6[13] = item.assignmentinvslot[14]
                    item.itemslotactive6[14] = item.assignmentinvslot[15]
                    item.itemslotactive6[15] = item.assignmentinvslot[16]
                    item.itemslotactive6[16] = item.assignmentinvslot[17]                   
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na przedmioty aktywne są w użyciu')
        if (item.inventoryslot7[4] == lookforinv) and (item.inventoryslot7[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot7
            if item.inventoryslot7[5] == 'armorhead':
                item.itemslothead[0] = item.assignmentinvslot[0]
                item.itemslothead[1] = item.assignmentinvslot[2]
                item.itemslothead[2] = item.assignmentinvslot[3]
                item.itemslothead[3] = item.assignmentinvslot[4]
                item.itemslothead[4] = item.assignmentinvslot[5]
                item.itemslothead[5] = item.assignmentinvslot[6]
                item.itemslothead[6] = item.assignmentinvslot[7]
                item.itemslothead[7] = item.assignmentinvslot[8]
                item.itemslothead[8] = item.assignmentinvslot[9]
                item.itemslothead[9] = item.assignmentinvslot[10]
                item.itemslothead[10] = item.assignmentinvslot[11]
                item.itemslothead[11] = item.assignmentinvslot[12]
                item.itemslothead[12] = item.assignmentinvslot[13]
                item.itemslothead[13] = item.assignmentinvslot[14]
                item.itemslothead[14] = item.assignmentinvslot[15]
                item.itemslothead[15] = item.assignmentinvslot[16]
                item.itemslothead[16] = item.assignmentinvslot[17]
            if item.inventoryslot7[5] == 'armorchest':
                item.itemslotchest[0] = item.assignmentinvslot[0]
                item.itemslotchest[1] = item.assignmentinvslot[2]
                item.itemslotchest[2] = item.assignmentinvslot[3]
                item.itemslotchest[3] = item.assignmentinvslot[4]
                item.itemslotchest[4] = item.assignmentinvslot[5]
                item.itemslotchest[5] = item.assignmentinvslot[6]
                item.itemslotchest[6] = item.assignmentinvslot[7]
                item.itemslotchest[7] = item.assignmentinvslot[8]
                item.itemslotchest[8] = item.assignmentinvslot[9]
                item.itemslotchest[9] = item.assignmentinvslot[10]
                item.itemslotchest[10] = item.assignmentinvslot[11]
                item.itemslotchest[11] = item.assignmentinvslot[12]
                item.itemslotchest[12] = item.assignmentinvslot[13]
                item.itemslotchest[13] = item.assignmentinvslot[14]
                item.itemslotchest[14] = item.assignmentinvslot[15]
                item.itemslotchest[15] = item.assignmentinvslot[16]
                item.itemslotchest[16] = item.assignmentinvslot[17]
            if item.inventoryslot7[5] == 'armorarms':
                item.itemslotarms[0] = item.assignmentinvslot[0]
                item.itemslotarms[1] = item.assignmentinvslot[2]
                item.itemslotarms[2] = item.assignmentinvslot[3]
                item.itemslotarms[3] = item.assignmentinvslot[4]
                item.itemslotarms[4] = item.assignmentinvslot[5]
                item.itemslotarms[5] = item.assignmentinvslot[6]
                item.itemslotarms[6] = item.assignmentinvslot[7]
                item.itemslotarms[7] = item.assignmentinvslot[8]
                item.itemslotarms[8] = item.assignmentinvslot[9]
                item.itemslotarms[9] = item.assignmentinvslot[10]
                item.itemslotarms[10] = item.assignmentinvslot[11]
                item.itemslotarms[11] = item.assignmentinvslot[12]
                item.itemslotarms[12] = item.assignmentinvslot[13]
                item.itemslotarms[13] = item.assignmentinvslot[14]
                item.itemslotarms[14] = item.assignmentinvslot[15]
                item.itemslotarms[15] = item.assignmentinvslot[16]
                item.itemslotarms[16] = item.assignmentinvslot[17]    
            if item.inventoryslot7[5] == 'armorhands':
                item.itemslothands[0] = item.assignmentinvslot[0]
                item.itemslothands[1] = item.assignmentinvslot[2]
                item.itemslothands[2] = item.assignmentinvslot[3]
                item.itemslothands[3] = item.assignmentinvslot[4]
                item.itemslothands[4] = item.assignmentinvslot[5]
                item.itemslothands[5] = item.assignmentinvslot[6]
                item.itemslothands[6] = item.assignmentinvslot[7]
                item.itemslothands[7] = item.assignmentinvslot[8]
                item.itemslothands[8] = item.assignmentinvslot[9]
                item.itemslothands[9] = item.assignmentinvslot[10]
                item.itemslothands[10] = item.assignmentinvslot[11]
                item.itemslothands[11] = item.assignmentinvslot[12]
                item.itemslothands[12] = item.assignmentinvslot[13]
                item.itemslothands[13] = item.assignmentinvslot[14]
                item.itemslothands[14] = item.assignmentinvslot[15]
                item.itemslothands[15] = item.assignmentinvslot[16]
                item.itemslothands[16] = item.assignmentinvslot[17]   
            if item.inventoryslot7[5] == 'armorlegs':
                item.itemslotlegs[0] = item.assignmentinvslot[0]
                item.itemslotlegs[1] = item.assignmentinvslot[2]
                item.itemslotlegs[2] = item.assignmentinvslot[3]
                item.itemslotlegs[3] = item.assignmentinvslot[4]
                item.itemslotlegs[4] = item.assignmentinvslot[5]
                item.itemslotlegs[5] = item.assignmentinvslot[6]
                item.itemslotlegs[6] = item.assignmentinvslot[7]
                item.itemslotlegs[7] = item.assignmentinvslot[8]
                item.itemslotlegs[8] = item.assignmentinvslot[9]
                item.itemslotlegs[9] = item.assignmentinvslot[10]
                item.itemslotlegs[10] = item.assignmentinvslot[11]
                item.itemslotlegs[11] = item.assignmentinvslot[12]
                item.itemslotlegs[12] = item.assignmentinvslot[13]
                item.itemslotlegs[13] = item.assignmentinvslot[14]
                item.itemslotlegs[14] = item.assignmentinvslot[15]
                item.itemslotlegs[15] = item.assignmentinvslot[16]
                item.itemslotlegs[16] = item.assignmentinvslot[17]    
            if item.inventoryslot7[5] == 'armorfoot':
                item.itemslotfoot[0] = item.assignmentinvslot[0]
                item.itemslotfoot[1] = item.assignmentinvslot[2]
                item.itemslotfoot[2] = item.assignmentinvslot[3]
                item.itemslotfoot[3] = item.assignmentinvslot[4]
                item.itemslotfoot[4] = item.assignmentinvslot[5]
                item.itemslotfoot[5] = item.assignmentinvslot[6]
                item.itemslotfoot[6] = item.assignmentinvslot[7]
                item.itemslotfoot[7] = item.assignmentinvslot[8]
                item.itemslotfoot[8] = item.assignmentinvslot[9]
                item.itemslotfoot[9] = item.assignmentinvslot[10]
                item.itemslotfoot[10] = item.assignmentinvslot[11]
                item.itemslotfoot[11] = item.assignmentinvslot[12]
                item.itemslotfoot[12] = item.assignmentinvslot[13]
                item.itemslotfoot[13] = item.assignmentinvslot[14]
                item.itemslotfoot[14] = item.assignmentinvslot[15]
                item.itemslotfoot[15] = item.assignmentinvslot[16]
                item.itemslotfoot[16] = item.assignmentinvslot[17]    
            if item.inventoryslot7[5] == 'armoracc':
                if item.itemslotacc1[0] == 0:    
                    item.itemslotacc1[0] = item.assignmentinvslot[0]
                    item.itemslotacc1[1] = item.assignmentinvslot[2]
                    item.itemslotacc1[2] = item.assignmentinvslot[3]
                    item.itemslotacc1[3] = item.assignmentinvslot[4]
                    item.itemslotacc1[4] = item.assignmentinvslot[5]
                    item.itemslotacc1[5] = item.assignmentinvslot[6]
                    item.itemslotacc1[6] = item.assignmentinvslot[7]
                    item.itemslotacc1[7] = item.assignmentinvslot[8]
                    item.itemslotacc1[8] = item.assignmentinvslot[9]
                    item.itemslotacc1[9] = item.assignmentinvslot[10]
                    item.itemslotacc1[10] = item.assignmentinvslot[11]
                    item.itemslotacc1[11] = item.assignmentinvslot[12]
                    item.itemslotacc1[12] = item.assignmentinvslot[13]
                    item.itemslotacc1[13] = item.assignmentinvslot[14]
                    item.itemslotacc1[14] = item.assignmentinvslot[15]
                    item.itemslotacc1[15] = item.assignmentinvslot[16]
                    item.itemslotacc1[16] = item.assignmentinvslot[17] 
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] == 0):
                    item.itemslotacc2[0] = item.assignmentinvslot[0]
                    item.itemslotacc2[1] = item.assignmentinvslot[2]
                    item.itemslotacc2[2] = item.assignmentinvslot[3]
                    item.itemslotacc2[3] = item.assignmentinvslot[4]
                    item.itemslotacc2[4] = item.assignmentinvslot[5]
                    item.itemslotacc2[5] = item.assignmentinvslot[6]
                    item.itemslotacc2[6] = item.assignmentinvslot[7]
                    item.itemslotacc2[7] = item.assignmentinvslot[8]
                    item.itemslotacc2[8] = item.assignmentinvslot[9]
                    item.itemslotacc2[9] = item.assignmentinvslot[10]
                    item.itemslotacc2[10] = item.assignmentinvslot[11]
                    item.itemslotacc2[11] = item.assignmentinvslot[12]
                    item.itemslotacc2[12] = item.assignmentinvslot[13]
                    item.itemslotacc2[13] = item.assignmentinvslot[14]
                    item.itemslotacc2[14] = item.assignmentinvslot[15]
                    item.itemslotacc2[15] = item.assignmentinvslot[16]
                    item.itemslotacc2[16] = item.assignmentinvslot[17]  
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] == 0):
                    item.itemslotacc3[0] = item.assignmentinvslot[0]
                    item.itemslotacc3[1] = item.assignmentinvslot[2]
                    item.itemslotacc3[2] = item.assignmentinvslot[3]
                    item.itemslotacc3[3] = item.assignmentinvslot[4]
                    item.itemslotacc3[4] = item.assignmentinvslot[5]
                    item.itemslotacc3[5] = item.assignmentinvslot[6]
                    item.itemslotacc3[6] = item.assignmentinvslot[7]
                    item.itemslotacc3[7] = item.assignmentinvslot[8]
                    item.itemslotacc3[8] = item.assignmentinvslot[9]
                    item.itemslotacc3[9] = item.assignmentinvslot[10]
                    item.itemslotacc3[10] = item.assignmentinvslot[11]
                    item.itemslotacc3[11] = item.assignmentinvslot[12]
                    item.itemslotacc3[12] = item.assignmentinvslot[13]
                    item.itemslotacc3[13] = item.assignmentinvslot[14]
                    item.itemslotacc3[14] = item.assignmentinvslot[15]
                    item.itemslotacc3[15] = item.assignmentinvslot[16]
                    item.itemslotacc3[16] = item.assignmentinvslot[17]               
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na akcesoria są w użyciu')
            if item.inventoryslot7[5] == 'armoractive': 
                if (item.itemslotactive1[0] == 0):
                    item.itemslotactive1[0] = item.assignmentinvslot[0]
                    item.itemslotactive1[1] = item.assignmentinvslot[2]
                    item.itemslotactive1[2] = item.assignmentinvslot[3]
                    item.itemslotactive1[3] = item.assignmentinvslot[4]
                    item.itemslotactive1[4] = item.assignmentinvslot[5]
                    item.itemslotactive1[5] = item.assignmentinvslot[6]
                    item.itemslotactive1[6] = item.assignmentinvslot[7]
                    item.itemslotactive1[7] = item.assignmentinvslot[8]
                    item.itemslotactive1[8] = item.assignmentinvslot[9]
                    item.itemslotactive1[9] = item.assignmentinvslot[10]
                    item.itemslotactive1[10] = item.assignmentinvslot[11]
                    item.itemslotactive1[11] = item.assignmentinvslot[12]
                    item.itemslotactive1[12] = item.assignmentinvslot[13]
                    item.itemslotactive1[13] = item.assignmentinvslot[14]
                    item.itemslotactive1[14] = item.assignmentinvslot[15]
                    item.itemslotactive1[15] = item.assignmentinvslot[16]
                    item.itemslotactive1[16] = item.assignmentinvslot[17]           
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] == 0):
                    item.itemslotactive2[0] = item.assignmentinvslot[0]
                    item.itemslotactive2[1] = item.assignmentinvslot[2]
                    item.itemslotactive2[2] = item.assignmentinvslot[3]
                    item.itemslotactive2[3] = item.assignmentinvslot[4]
                    item.itemslotactive2[4] = item.assignmentinvslot[5]
                    item.itemslotactive2[5] = item.assignmentinvslot[6]
                    item.itemslotactive2[6] = item.assignmentinvslot[7]
                    item.itemslotactive2[7] = item.assignmentinvslot[8]
                    item.itemslotactive2[8] = item.assignmentinvslot[9]
                    item.itemslotactive2[9] = item.assignmentinvslot[10]
                    item.itemslotactive2[10] = item.assignmentinvslot[11]
                    item.itemslotactive2[11] = item.assignmentinvslot[12]
                    item.itemslotactive2[12] = item.assignmentinvslot[13]
                    item.itemslotactive2[13] = item.assignmentinvslot[14]
                    item.itemslotactive2[14] = item.assignmentinvslot[15]
                    item.itemslotactive2[15] = item.assignmentinvslot[16]
                    item.itemslotactive2[16] = item.assignmentinvslot[17]                
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] == 0):
                    item.itemslotactive3[0] = item.assignmentinvslot[0]
                    item.itemslotactive3[1] = item.assignmentinvslot[2]
                    item.itemslotactive3[2] = item.assignmentinvslot[3]
                    item.itemslotactive3[3] = item.assignmentinvslot[4]
                    item.itemslotactive3[4] = item.assignmentinvslot[5]
                    item.itemslotactive3[5] = item.assignmentinvslot[6]
                    item.itemslotactive3[6] = item.assignmentinvslot[7]
                    item.itemslotactive3[7] = item.assignmentinvslot[8]
                    item.itemslotactive3[8] = item.assignmentinvslot[9]
                    item.itemslotactive3[9] = item.assignmentinvslot[10]
                    item.itemslotactive3[10] = item.assignmentinvslot[11]
                    item.itemslotactive3[11] = item.assignmentinvslot[12]
                    item.itemslotactive3[12] = item.assignmentinvslot[13]
                    item.itemslotactive3[13] = item.assignmentinvslot[14]
                    item.itemslotactive3[14] = item.assignmentinvslot[15]
                    item.itemslotactive3[15] = item.assignmentinvslot[16]
                    item.itemslotactive3[16] = item.assignmentinvslot[17]                 
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] == 0):
                    item.itemslotactive4[0] = item.assignmentinvslot[0]
                    item.itemslotactive4[1] = item.assignmentinvslot[2]
                    item.itemslotactive4[2] = item.assignmentinvslot[3]
                    item.itemslotactive4[3] = item.assignmentinvslot[4]
                    item.itemslotactive4[4] = item.assignmentinvslot[5]
                    item.itemslotactive4[5] = item.assignmentinvslot[6]
                    item.itemslotactive4[6] = item.assignmentinvslot[7]
                    item.itemslotactive4[7] = item.assignmentinvslot[8]
                    item.itemslotactive4[8] = item.assignmentinvslot[9]
                    item.itemslotactive4[9] = item.assignmentinvslot[10]
                    item.itemslotactive4[10] = item.assignmentinvslot[11]
                    item.itemslotactive4[11] = item.assignmentinvslot[12]
                    item.itemslotactive4[12] = item.assignmentinvslot[13]
                    item.itemslotactive4[13] = item.assignmentinvslot[14]
                    item.itemslotactive4[14] = item.assignmentinvslot[15]
                    item.itemslotactive4[15] = item.assignmentinvslot[16]
                    item.itemslotactive4[16] = item.assignmentinvslot[17]    
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] == 0):
                    item.itemslotactive5[0] = item.assignmentinvslot[0]
                    item.itemslotactive5[1] = item.assignmentinvslot[2]
                    item.itemslotactive5[2] = item.assignmentinvslot[3]
                    item.itemslotactive5[3] = item.assignmentinvslot[4]
                    item.itemslotactive5[4] = item.assignmentinvslot[5]
                    item.itemslotactive5[5] = item.assignmentinvslot[6]
                    item.itemslotactive5[6] = item.assignmentinvslot[7]
                    item.itemslotactive5[7] = item.assignmentinvslot[8]
                    item.itemslotactive5[8] = item.assignmentinvslot[9]
                    item.itemslotactive5[9] = item.assignmentinvslot[10]
                    item.itemslotactive5[10] = item.assignmentinvslot[11]
                    item.itemslotactive5[11] = item.assignmentinvslot[12]
                    item.itemslotactive5[12] = item.assignmentinvslot[13]
                    item.itemslotactive5[13] = item.assignmentinvslot[14]
                    item.itemslotactive5[14] = item.assignmentinvslot[15]
                    item.itemslotactive5[15] = item.assignmentinvslot[16]
                    item.itemslotactive5[16] = item.assignmentinvslot[17]     
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] == 0):
                    item.itemslotactive6[0] = item.assignmentinvslot[0]
                    item.itemslotactive6[1] = item.assignmentinvslot[2]
                    item.itemslotactive6[2] = item.assignmentinvslot[3]
                    item.itemslotactive6[3] = item.assignmentinvslot[4]
                    item.itemslotactive6[4] = item.assignmentinvslot[5]
                    item.itemslotactive6[5] = item.assignmentinvslot[6]
                    item.itemslotactive6[6] = item.assignmentinvslot[7]
                    item.itemslotactive6[7] = item.assignmentinvslot[8]
                    item.itemslotactive6[8] = item.assignmentinvslot[9]
                    item.itemslotactive6[9] = item.assignmentinvslot[10]
                    item.itemslotactive6[10] = item.assignmentinvslot[11]
                    item.itemslotactive6[11] = item.assignmentinvslot[12]
                    item.itemslotactive6[12] = item.assignmentinvslot[13]
                    item.itemslotactive6[13] = item.assignmentinvslot[14]
                    item.itemslotactive6[14] = item.assignmentinvslot[15]
                    item.itemslotactive6[15] = item.assignmentinvslot[16]
                    item.itemslotactive6[16] = item.assignmentinvslot[17]                   
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na przedmioty aktywne są w użyciu')
        if (item.inventoryslot8[4] == lookforinv) and (item.inventoryslot8[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot8
            if item.inventoryslot8[5] == 'armorhead':
                item.itemslothead[0] = item.assignmentinvslot[0]
                item.itemslothead[1] = item.assignmentinvslot[2]
                item.itemslothead[2] = item.assignmentinvslot[3]
                item.itemslothead[3] = item.assignmentinvslot[4]
                item.itemslothead[4] = item.assignmentinvslot[5]
                item.itemslothead[5] = item.assignmentinvslot[6]
                item.itemslothead[6] = item.assignmentinvslot[7]
                item.itemslothead[7] = item.assignmentinvslot[8]
                item.itemslothead[8] = item.assignmentinvslot[9]
                item.itemslothead[9] = item.assignmentinvslot[10]
                item.itemslothead[10] = item.assignmentinvslot[11]
                item.itemslothead[11] = item.assignmentinvslot[12]
                item.itemslothead[12] = item.assignmentinvslot[13]
                item.itemslothead[13] = item.assignmentinvslot[14]
                item.itemslothead[14] = item.assignmentinvslot[15]
                item.itemslothead[15] = item.assignmentinvslot[16]
                item.itemslothead[16] = item.assignmentinvslot[17]
            if item.inventoryslot8[5] == 'armorchest':
                item.itemslotchest[0] = item.assignmentinvslot[0]
                item.itemslotchest[1] = item.assignmentinvslot[2]
                item.itemslotchest[2] = item.assignmentinvslot[3]
                item.itemslotchest[3] = item.assignmentinvslot[4]
                item.itemslotchest[4] = item.assignmentinvslot[5]
                item.itemslotchest[5] = item.assignmentinvslot[6]
                item.itemslotchest[6] = item.assignmentinvslot[7]
                item.itemslotchest[7] = item.assignmentinvslot[8]
                item.itemslotchest[8] = item.assignmentinvslot[9]
                item.itemslotchest[9] = item.assignmentinvslot[10]
                item.itemslotchest[10] = item.assignmentinvslot[11]
                item.itemslotchest[11] = item.assignmentinvslot[12]
                item.itemslotchest[12] = item.assignmentinvslot[13]
                item.itemslotchest[13] = item.assignmentinvslot[14]
                item.itemslotchest[14] = item.assignmentinvslot[15]
                item.itemslotchest[15] = item.assignmentinvslot[16]
                item.itemslotchest[16] = item.assignmentinvslot[17]
            if item.inventoryslot8[5] == 'armorarms':
                item.itemslotarms[0] = item.assignmentinvslot[0]
                item.itemslotarms[1] = item.assignmentinvslot[2]
                item.itemslotarms[2] = item.assignmentinvslot[3]
                item.itemslotarms[3] = item.assignmentinvslot[4]
                item.itemslotarms[4] = item.assignmentinvslot[5]
                item.itemslotarms[5] = item.assignmentinvslot[6]
                item.itemslotarms[6] = item.assignmentinvslot[7]
                item.itemslotarms[7] = item.assignmentinvslot[8]
                item.itemslotarms[8] = item.assignmentinvslot[9]
                item.itemslotarms[9] = item.assignmentinvslot[10]
                item.itemslotarms[10] = item.assignmentinvslot[11]
                item.itemslotarms[11] = item.assignmentinvslot[12]
                item.itemslotarms[12] = item.assignmentinvslot[13]
                item.itemslotarms[13] = item.assignmentinvslot[14]
                item.itemslotarms[14] = item.assignmentinvslot[15]
                item.itemslotarms[15] = item.assignmentinvslot[16]
                item.itemslotarms[16] = item.assignmentinvslot[17]    
            if item.inventoryslot8[5] == 'armorhands':
                item.itemslothands[0] = item.assignmentinvslot[0]
                item.itemslothands[1] = item.assignmentinvslot[2]
                item.itemslothands[2] = item.assignmentinvslot[3]
                item.itemslothands[3] = item.assignmentinvslot[4]
                item.itemslothands[4] = item.assignmentinvslot[5]
                item.itemslothands[5] = item.assignmentinvslot[6]
                item.itemslothands[6] = item.assignmentinvslot[7]
                item.itemslothands[7] = item.assignmentinvslot[8]
                item.itemslothands[8] = item.assignmentinvslot[9]
                item.itemslothands[9] = item.assignmentinvslot[10]
                item.itemslothands[10] = item.assignmentinvslot[11]
                item.itemslothands[11] = item.assignmentinvslot[12]
                item.itemslothands[12] = item.assignmentinvslot[13]
                item.itemslothands[13] = item.assignmentinvslot[14]
                item.itemslothands[14] = item.assignmentinvslot[15]
                item.itemslothands[15] = item.assignmentinvslot[16]
                item.itemslothands[16] = item.assignmentinvslot[17]   
            if item.inventoryslot8[5] == 'armorlegs':
                item.itemslotlegs[0] = item.assignmentinvslot[0]
                item.itemslotlegs[1] = item.assignmentinvslot[2]
                item.itemslotlegs[2] = item.assignmentinvslot[3]
                item.itemslotlegs[3] = item.assignmentinvslot[4]
                item.itemslotlegs[4] = item.assignmentinvslot[5]
                item.itemslotlegs[5] = item.assignmentinvslot[6]
                item.itemslotlegs[6] = item.assignmentinvslot[7]
                item.itemslotlegs[7] = item.assignmentinvslot[8]
                item.itemslotlegs[8] = item.assignmentinvslot[9]
                item.itemslotlegs[9] = item.assignmentinvslot[10]
                item.itemslotlegs[10] = item.assignmentinvslot[11]
                item.itemslotlegs[11] = item.assignmentinvslot[12]
                item.itemslotlegs[12] = item.assignmentinvslot[13]
                item.itemslotlegs[13] = item.assignmentinvslot[14]
                item.itemslotlegs[14] = item.assignmentinvslot[15]
                item.itemslotlegs[15] = item.assignmentinvslot[16]
                item.itemslotlegs[16] = item.assignmentinvslot[17]    
            if item.inventoryslot8[5] == 'armorfoot':
                item.itemslotfoot[0] = item.assignmentinvslot[0]
                item.itemslotfoot[1] = item.assignmentinvslot[2]
                item.itemslotfoot[2] = item.assignmentinvslot[3]
                item.itemslotfoot[3] = item.assignmentinvslot[4]
                item.itemslotfoot[4] = item.assignmentinvslot[5]
                item.itemslotfoot[5] = item.assignmentinvslot[6]
                item.itemslotfoot[6] = item.assignmentinvslot[7]
                item.itemslotfoot[7] = item.assignmentinvslot[8]
                item.itemslotfoot[8] = item.assignmentinvslot[9]
                item.itemslotfoot[9] = item.assignmentinvslot[10]
                item.itemslotfoot[10] = item.assignmentinvslot[11]
                item.itemslotfoot[11] = item.assignmentinvslot[12]
                item.itemslotfoot[12] = item.assignmentinvslot[13]
                item.itemslotfoot[13] = item.assignmentinvslot[14]
                item.itemslotfoot[14] = item.assignmentinvslot[15]
                item.itemslotfoot[15] = item.assignmentinvslot[16]
                item.itemslotfoot[16] = item.assignmentinvslot[17]    
            if item.inventoryslot8[5] == 'armoracc':
                if item.itemslotacc1[0] == 0:    
                    item.itemslotacc1[0] = item.assignmentinvslot[0]
                    item.itemslotacc1[1] = item.assignmentinvslot[2]
                    item.itemslotacc1[2] = item.assignmentinvslot[3]
                    item.itemslotacc1[3] = item.assignmentinvslot[4]
                    item.itemslotacc1[4] = item.assignmentinvslot[5]
                    item.itemslotacc1[5] = item.assignmentinvslot[6]
                    item.itemslotacc1[6] = item.assignmentinvslot[7]
                    item.itemslotacc1[7] = item.assignmentinvslot[8]
                    item.itemslotacc1[8] = item.assignmentinvslot[9]
                    item.itemslotacc1[9] = item.assignmentinvslot[10]
                    item.itemslotacc1[10] = item.assignmentinvslot[11]
                    item.itemslotacc1[11] = item.assignmentinvslot[12]
                    item.itemslotacc1[12] = item.assignmentinvslot[13]
                    item.itemslotacc1[13] = item.assignmentinvslot[14]
                    item.itemslotacc1[14] = item.assignmentinvslot[15]
                    item.itemslotacc1[15] = item.assignmentinvslot[16]
                    item.itemslotacc1[16] = item.assignmentinvslot[17] 
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] == 0):
                    item.itemslotacc2[0] = item.assignmentinvslot[0]
                    item.itemslotacc2[1] = item.assignmentinvslot[2]
                    item.itemslotacc2[2] = item.assignmentinvslot[3]
                    item.itemslotacc2[3] = item.assignmentinvslot[4]
                    item.itemslotacc2[4] = item.assignmentinvslot[5]
                    item.itemslotacc2[5] = item.assignmentinvslot[6]
                    item.itemslotacc2[6] = item.assignmentinvslot[7]
                    item.itemslotacc2[7] = item.assignmentinvslot[8]
                    item.itemslotacc2[8] = item.assignmentinvslot[9]
                    item.itemslotacc2[9] = item.assignmentinvslot[10]
                    item.itemslotacc2[10] = item.assignmentinvslot[11]
                    item.itemslotacc2[11] = item.assignmentinvslot[12]
                    item.itemslotacc2[12] = item.assignmentinvslot[13]
                    item.itemslotacc2[13] = item.assignmentinvslot[14]
                    item.itemslotacc2[14] = item.assignmentinvslot[15]
                    item.itemslotacc2[15] = item.assignmentinvslot[16]
                    item.itemslotacc2[16] = item.assignmentinvslot[17]  
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] == 0):
                    item.itemslotacc3[0] = item.assignmentinvslot[0]
                    item.itemslotacc3[1] = item.assignmentinvslot[2]
                    item.itemslotacc3[2] = item.assignmentinvslot[3]
                    item.itemslotacc3[3] = item.assignmentinvslot[4]
                    item.itemslotacc3[4] = item.assignmentinvslot[5]
                    item.itemslotacc3[5] = item.assignmentinvslot[6]
                    item.itemslotacc3[6] = item.assignmentinvslot[7]
                    item.itemslotacc3[7] = item.assignmentinvslot[8]
                    item.itemslotacc3[8] = item.assignmentinvslot[9]
                    item.itemslotacc3[9] = item.assignmentinvslot[10]
                    item.itemslotacc3[10] = item.assignmentinvslot[11]
                    item.itemslotacc3[11] = item.assignmentinvslot[12]
                    item.itemslotacc3[12] = item.assignmentinvslot[13]
                    item.itemslotacc3[13] = item.assignmentinvslot[14]
                    item.itemslotacc3[14] = item.assignmentinvslot[15]
                    item.itemslotacc3[15] = item.assignmentinvslot[16]
                    item.itemslotacc3[16] = item.assignmentinvslot[17]               
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na akcesoria są w użyciu')
            if item.inventoryslot8[5] == 'armoractive': 
                if (item.itemslotactive1[0] == 0):
                    item.itemslotactive1[0] = item.assignmentinvslot[0]
                    item.itemslotactive1[1] = item.assignmentinvslot[2]
                    item.itemslotactive1[2] = item.assignmentinvslot[3]
                    item.itemslotactive1[3] = item.assignmentinvslot[4]
                    item.itemslotactive1[4] = item.assignmentinvslot[5]
                    item.itemslotactive1[5] = item.assignmentinvslot[6]
                    item.itemslotactive1[6] = item.assignmentinvslot[7]
                    item.itemslotactive1[7] = item.assignmentinvslot[8]
                    item.itemslotactive1[8] = item.assignmentinvslot[9]
                    item.itemslotactive1[9] = item.assignmentinvslot[10]
                    item.itemslotactive1[10] = item.assignmentinvslot[11]
                    item.itemslotactive1[11] = item.assignmentinvslot[12]
                    item.itemslotactive1[12] = item.assignmentinvslot[13]
                    item.itemslotactive1[13] = item.assignmentinvslot[14]
                    item.itemslotactive1[14] = item.assignmentinvslot[15]
                    item.itemslotactive1[15] = item.assignmentinvslot[16]
                    item.itemslotactive1[16] = item.assignmentinvslot[17]           
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] == 0):
                    item.itemslotactive2[0] = item.assignmentinvslot[0]
                    item.itemslotactive2[1] = item.assignmentinvslot[2]
                    item.itemslotactive2[2] = item.assignmentinvslot[3]
                    item.itemslotactive2[3] = item.assignmentinvslot[4]
                    item.itemslotactive2[4] = item.assignmentinvslot[5]
                    item.itemslotactive2[5] = item.assignmentinvslot[6]
                    item.itemslotactive2[6] = item.assignmentinvslot[7]
                    item.itemslotactive2[7] = item.assignmentinvslot[8]
                    item.itemslotactive2[8] = item.assignmentinvslot[9]
                    item.itemslotactive2[9] = item.assignmentinvslot[10]
                    item.itemslotactive2[10] = item.assignmentinvslot[11]
                    item.itemslotactive2[11] = item.assignmentinvslot[12]
                    item.itemslotactive2[12] = item.assignmentinvslot[13]
                    item.itemslotactive2[13] = item.assignmentinvslot[14]
                    item.itemslotactive2[14] = item.assignmentinvslot[15]
                    item.itemslotactive2[15] = item.assignmentinvslot[16]
                    item.itemslotactive2[16] = item.assignmentinvslot[17]                
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] == 0):
                    item.itemslotactive3[0] = item.assignmentinvslot[0]
                    item.itemslotactive3[1] = item.assignmentinvslot[2]
                    item.itemslotactive3[2] = item.assignmentinvslot[3]
                    item.itemslotactive3[3] = item.assignmentinvslot[4]
                    item.itemslotactive3[4] = item.assignmentinvslot[5]
                    item.itemslotactive3[5] = item.assignmentinvslot[6]
                    item.itemslotactive3[6] = item.assignmentinvslot[7]
                    item.itemslotactive3[7] = item.assignmentinvslot[8]
                    item.itemslotactive3[8] = item.assignmentinvslot[9]
                    item.itemslotactive3[9] = item.assignmentinvslot[10]
                    item.itemslotactive3[10] = item.assignmentinvslot[11]
                    item.itemslotactive3[11] = item.assignmentinvslot[12]
                    item.itemslotactive3[12] = item.assignmentinvslot[13]
                    item.itemslotactive3[13] = item.assignmentinvslot[14]
                    item.itemslotactive3[14] = item.assignmentinvslot[15]
                    item.itemslotactive3[15] = item.assignmentinvslot[16]
                    item.itemslotactive3[16] = item.assignmentinvslot[17]                 
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] == 0):
                    item.itemslotactive4[0] = item.assignmentinvslot[0]
                    item.itemslotactive4[1] = item.assignmentinvslot[2]
                    item.itemslotactive4[2] = item.assignmentinvslot[3]
                    item.itemslotactive4[3] = item.assignmentinvslot[4]
                    item.itemslotactive4[4] = item.assignmentinvslot[5]
                    item.itemslotactive4[5] = item.assignmentinvslot[6]
                    item.itemslotactive4[6] = item.assignmentinvslot[7]
                    item.itemslotactive4[7] = item.assignmentinvslot[8]
                    item.itemslotactive4[8] = item.assignmentinvslot[9]
                    item.itemslotactive4[9] = item.assignmentinvslot[10]
                    item.itemslotactive4[10] = item.assignmentinvslot[11]
                    item.itemslotactive4[11] = item.assignmentinvslot[12]
                    item.itemslotactive4[12] = item.assignmentinvslot[13]
                    item.itemslotactive4[13] = item.assignmentinvslot[14]
                    item.itemslotactive4[14] = item.assignmentinvslot[15]
                    item.itemslotactive4[15] = item.assignmentinvslot[16]
                    item.itemslotactive4[16] = item.assignmentinvslot[17]    
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] == 0):
                    item.itemslotactive5[0] = item.assignmentinvslot[0]
                    item.itemslotactive5[1] = item.assignmentinvslot[2]
                    item.itemslotactive5[2] = item.assignmentinvslot[3]
                    item.itemslotactive5[3] = item.assignmentinvslot[4]
                    item.itemslotactive5[4] = item.assignmentinvslot[5]
                    item.itemslotactive5[5] = item.assignmentinvslot[6]
                    item.itemslotactive5[6] = item.assignmentinvslot[7]
                    item.itemslotactive5[7] = item.assignmentinvslot[8]
                    item.itemslotactive5[8] = item.assignmentinvslot[9]
                    item.itemslotactive5[9] = item.assignmentinvslot[10]
                    item.itemslotactive5[10] = item.assignmentinvslot[11]
                    item.itemslotactive5[11] = item.assignmentinvslot[12]
                    item.itemslotactive5[12] = item.assignmentinvslot[13]
                    item.itemslotactive5[13] = item.assignmentinvslot[14]
                    item.itemslotactive5[14] = item.assignmentinvslot[15]
                    item.itemslotactive5[15] = item.assignmentinvslot[16]
                    item.itemslotactive5[16] = item.assignmentinvslot[17]     
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] == 0):
                    item.itemslotactive6[0] = item.assignmentinvslot[0]
                    item.itemslotactive6[1] = item.assignmentinvslot[2]
                    item.itemslotactive6[2] = item.assignmentinvslot[3]
                    item.itemslotactive6[3] = item.assignmentinvslot[4]
                    item.itemslotactive6[4] = item.assignmentinvslot[5]
                    item.itemslotactive6[5] = item.assignmentinvslot[6]
                    item.itemslotactive6[6] = item.assignmentinvslot[7]
                    item.itemslotactive6[7] = item.assignmentinvslot[8]
                    item.itemslotactive6[8] = item.assignmentinvslot[9]
                    item.itemslotactive6[9] = item.assignmentinvslot[10]
                    item.itemslotactive6[10] = item.assignmentinvslot[11]
                    item.itemslotactive6[11] = item.assignmentinvslot[12]
                    item.itemslotactive6[12] = item.assignmentinvslot[13]
                    item.itemslotactive6[13] = item.assignmentinvslot[14]
                    item.itemslotactive6[14] = item.assignmentinvslot[15]
                    item.itemslotactive6[15] = item.assignmentinvslot[16]
                    item.itemslotactive6[16] = item.assignmentinvslot[17]                   
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na przedmioty aktywne są w użyciu')
        if (item.inventoryslot9[4] == lookforinv) and (item.inventoryslot9[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot9
            if item.inventoryslot9[5] == 'armorhead':
                item.itemslothead[0] = item.assignmentinvslot[0]
                item.itemslothead[1] = item.assignmentinvslot[2]
                item.itemslothead[2] = item.assignmentinvslot[3]
                item.itemslothead[3] = item.assignmentinvslot[4]
                item.itemslothead[4] = item.assignmentinvslot[5]
                item.itemslothead[5] = item.assignmentinvslot[6]
                item.itemslothead[6] = item.assignmentinvslot[7]
                item.itemslothead[7] = item.assignmentinvslot[8]
                item.itemslothead[8] = item.assignmentinvslot[9]
                item.itemslothead[9] = item.assignmentinvslot[10]
                item.itemslothead[10] = item.assignmentinvslot[11]
                item.itemslothead[11] = item.assignmentinvslot[12]
                item.itemslothead[12] = item.assignmentinvslot[13]
                item.itemslothead[13] = item.assignmentinvslot[14]
                item.itemslothead[14] = item.assignmentinvslot[15]
                item.itemslothead[15] = item.assignmentinvslot[16]
                item.itemslothead[16] = item.assignmentinvslot[17]
            if item.inventoryslot9[5] == 'armorchest':
                item.itemslotchest[0] = item.assignmentinvslot[0]
                item.itemslotchest[1] = item.assignmentinvslot[2]
                item.itemslotchest[2] = item.assignmentinvslot[3]
                item.itemslotchest[3] = item.assignmentinvslot[4]
                item.itemslotchest[4] = item.assignmentinvslot[5]
                item.itemslotchest[5] = item.assignmentinvslot[6]
                item.itemslotchest[6] = item.assignmentinvslot[7]
                item.itemslotchest[7] = item.assignmentinvslot[8]
                item.itemslotchest[8] = item.assignmentinvslot[9]
                item.itemslotchest[9] = item.assignmentinvslot[10]
                item.itemslotchest[10] = item.assignmentinvslot[11]
                item.itemslotchest[11] = item.assignmentinvslot[12]
                item.itemslotchest[12] = item.assignmentinvslot[13]
                item.itemslotchest[13] = item.assignmentinvslot[14]
                item.itemslotchest[14] = item.assignmentinvslot[15]
                item.itemslotchest[15] = item.assignmentinvslot[16]
                item.itemslotchest[16] = item.assignmentinvslot[17]
            if item.inventoryslot9[5] == 'armorarms':
                item.itemslotarms[0] = item.assignmentinvslot[0]
                item.itemslotarms[1] = item.assignmentinvslot[2]
                item.itemslotarms[2] = item.assignmentinvslot[3]
                item.itemslotarms[3] = item.assignmentinvslot[4]
                item.itemslotarms[4] = item.assignmentinvslot[5]
                item.itemslotarms[5] = item.assignmentinvslot[6]
                item.itemslotarms[6] = item.assignmentinvslot[7]
                item.itemslotarms[7] = item.assignmentinvslot[8]
                item.itemslotarms[8] = item.assignmentinvslot[9]
                item.itemslotarms[9] = item.assignmentinvslot[10]
                item.itemslotarms[10] = item.assignmentinvslot[11]
                item.itemslotarms[11] = item.assignmentinvslot[12]
                item.itemslotarms[12] = item.assignmentinvslot[13]
                item.itemslotarms[13] = item.assignmentinvslot[14]
                item.itemslotarms[14] = item.assignmentinvslot[15]
                item.itemslotarms[15] = item.assignmentinvslot[16]
                item.itemslotarms[16] = item.assignmentinvslot[17]    
            if item.inventoryslot9[5] == 'armorhands':
                item.itemslothands[0] = item.assignmentinvslot[0]
                item.itemslothands[1] = item.assignmentinvslot[2]
                item.itemslothands[2] = item.assignmentinvslot[3]
                item.itemslothands[3] = item.assignmentinvslot[4]
                item.itemslothands[4] = item.assignmentinvslot[5]
                item.itemslothands[5] = item.assignmentinvslot[6]
                item.itemslothands[6] = item.assignmentinvslot[7]
                item.itemslothands[7] = item.assignmentinvslot[8]
                item.itemslothands[8] = item.assignmentinvslot[9]
                item.itemslothands[9] = item.assignmentinvslot[10]
                item.itemslothands[10] = item.assignmentinvslot[11]
                item.itemslothands[11] = item.assignmentinvslot[12]
                item.itemslothands[12] = item.assignmentinvslot[13]
                item.itemslothands[13] = item.assignmentinvslot[14]
                item.itemslothands[14] = item.assignmentinvslot[15]
                item.itemslothands[15] = item.assignmentinvslot[16]
                item.itemslothands[16] = item.assignmentinvslot[17]   
            if item.inventoryslot9[5] == 'armorlegs':
                item.itemslotlegs[0] = item.assignmentinvslot[0]
                item.itemslotlegs[1] = item.assignmentinvslot[2]
                item.itemslotlegs[2] = item.assignmentinvslot[3]
                item.itemslotlegs[3] = item.assignmentinvslot[4]
                item.itemslotlegs[4] = item.assignmentinvslot[5]
                item.itemslotlegs[5] = item.assignmentinvslot[6]
                item.itemslotlegs[6] = item.assignmentinvslot[7]
                item.itemslotlegs[7] = item.assignmentinvslot[8]
                item.itemslotlegs[8] = item.assignmentinvslot[9]
                item.itemslotlegs[9] = item.assignmentinvslot[10]
                item.itemslotlegs[10] = item.assignmentinvslot[11]
                item.itemslotlegs[11] = item.assignmentinvslot[12]
                item.itemslotlegs[12] = item.assignmentinvslot[13]
                item.itemslotlegs[13] = item.assignmentinvslot[14]
                item.itemslotlegs[14] = item.assignmentinvslot[15]
                item.itemslotlegs[15] = item.assignmentinvslot[16]
                item.itemslotlegs[16] = item.assignmentinvslot[17]    
            if item.inventoryslot9[5] == 'armorfoot':
                item.itemslotfoot[0] = item.assignmentinvslot[0]
                item.itemslotfoot[1] = item.assignmentinvslot[2]
                item.itemslotfoot[2] = item.assignmentinvslot[3]
                item.itemslotfoot[3] = item.assignmentinvslot[4]
                item.itemslotfoot[4] = item.assignmentinvslot[5]
                item.itemslotfoot[5] = item.assignmentinvslot[6]
                item.itemslotfoot[6] = item.assignmentinvslot[7]
                item.itemslotfoot[7] = item.assignmentinvslot[8]
                item.itemslotfoot[8] = item.assignmentinvslot[9]
                item.itemslotfoot[9] = item.assignmentinvslot[10]
                item.itemslotfoot[10] = item.assignmentinvslot[11]
                item.itemslotfoot[11] = item.assignmentinvslot[12]
                item.itemslotfoot[12] = item.assignmentinvslot[13]
                item.itemslotfoot[13] = item.assignmentinvslot[14]
                item.itemslotfoot[14] = item.assignmentinvslot[15]
                item.itemslotfoot[15] = item.assignmentinvslot[16]
                item.itemslotfoot[16] = item.assignmentinvslot[17]    
            if item.inventoryslot9[5] == 'armoracc':
                if item.itemslotacc1[0] == 0:    
                    item.itemslotacc1[0] = item.assignmentinvslot[0]
                    item.itemslotacc1[1] = item.assignmentinvslot[2]
                    item.itemslotacc1[2] = item.assignmentinvslot[3]
                    item.itemslotacc1[3] = item.assignmentinvslot[4]
                    item.itemslotacc1[4] = item.assignmentinvslot[5]
                    item.itemslotacc1[5] = item.assignmentinvslot[6]
                    item.itemslotacc1[6] = item.assignmentinvslot[7]
                    item.itemslotacc1[7] = item.assignmentinvslot[8]
                    item.itemslotacc1[8] = item.assignmentinvslot[9]
                    item.itemslotacc1[9] = item.assignmentinvslot[10]
                    item.itemslotacc1[10] = item.assignmentinvslot[11]
                    item.itemslotacc1[11] = item.assignmentinvslot[12]
                    item.itemslotacc1[12] = item.assignmentinvslot[13]
                    item.itemslotacc1[13] = item.assignmentinvslot[14]
                    item.itemslotacc1[14] = item.assignmentinvslot[15]
                    item.itemslotacc1[15] = item.assignmentinvslot[16]
                    item.itemslotacc1[16] = item.assignmentinvslot[17] 
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] == 0):
                    item.itemslotacc2[0] = item.assignmentinvslot[0]
                    item.itemslotacc2[1] = item.assignmentinvslot[2]
                    item.itemslotacc2[2] = item.assignmentinvslot[3]
                    item.itemslotacc2[3] = item.assignmentinvslot[4]
                    item.itemslotacc2[4] = item.assignmentinvslot[5]
                    item.itemslotacc2[5] = item.assignmentinvslot[6]
                    item.itemslotacc2[6] = item.assignmentinvslot[7]
                    item.itemslotacc2[7] = item.assignmentinvslot[8]
                    item.itemslotacc2[8] = item.assignmentinvslot[9]
                    item.itemslotacc2[9] = item.assignmentinvslot[10]
                    item.itemslotacc2[10] = item.assignmentinvslot[11]
                    item.itemslotacc2[11] = item.assignmentinvslot[12]
                    item.itemslotacc2[12] = item.assignmentinvslot[13]
                    item.itemslotacc2[13] = item.assignmentinvslot[14]
                    item.itemslotacc2[14] = item.assignmentinvslot[15]
                    item.itemslotacc2[15] = item.assignmentinvslot[16]
                    item.itemslotacc2[16] = item.assignmentinvslot[17]  
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] == 0):
                    item.itemslotacc3[0] = item.assignmentinvslot[0]
                    item.itemslotacc3[1] = item.assignmentinvslot[2]
                    item.itemslotacc3[2] = item.assignmentinvslot[3]
                    item.itemslotacc3[3] = item.assignmentinvslot[4]
                    item.itemslotacc3[4] = item.assignmentinvslot[5]
                    item.itemslotacc3[5] = item.assignmentinvslot[6]
                    item.itemslotacc3[6] = item.assignmentinvslot[7]
                    item.itemslotacc3[7] = item.assignmentinvslot[8]
                    item.itemslotacc3[8] = item.assignmentinvslot[9]
                    item.itemslotacc3[9] = item.assignmentinvslot[10]
                    item.itemslotacc3[10] = item.assignmentinvslot[11]
                    item.itemslotacc3[11] = item.assignmentinvslot[12]
                    item.itemslotacc3[12] = item.assignmentinvslot[13]
                    item.itemslotacc3[13] = item.assignmentinvslot[14]
                    item.itemslotacc3[14] = item.assignmentinvslot[15]
                    item.itemslotacc3[15] = item.assignmentinvslot[16]
                    item.itemslotacc3[16] = item.assignmentinvslot[17]               
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na akcesoria są w użyciu')
            if item.inventoryslot9[5] == 'armoractive': 
                if (item.itemslotactive1[0] == 0):
                    item.itemslotactive1[0] = item.assignmentinvslot[0]
                    item.itemslotactive1[1] = item.assignmentinvslot[2]
                    item.itemslotactive1[2] = item.assignmentinvslot[3]
                    item.itemslotactive1[3] = item.assignmentinvslot[4]
                    item.itemslotactive1[4] = item.assignmentinvslot[5]
                    item.itemslotactive1[5] = item.assignmentinvslot[6]
                    item.itemslotactive1[6] = item.assignmentinvslot[7]
                    item.itemslotactive1[7] = item.assignmentinvslot[8]
                    item.itemslotactive1[8] = item.assignmentinvslot[9]
                    item.itemslotactive1[9] = item.assignmentinvslot[10]
                    item.itemslotactive1[10] = item.assignmentinvslot[11]
                    item.itemslotactive1[11] = item.assignmentinvslot[12]
                    item.itemslotactive1[12] = item.assignmentinvslot[13]
                    item.itemslotactive1[13] = item.assignmentinvslot[14]
                    item.itemslotactive1[14] = item.assignmentinvslot[15]
                    item.itemslotactive1[15] = item.assignmentinvslot[16]
                    item.itemslotactive1[16] = item.assignmentinvslot[17]           
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] == 0):
                    item.itemslotactive2[0] = item.assignmentinvslot[0]
                    item.itemslotactive2[1] = item.assignmentinvslot[2]
                    item.itemslotactive2[2] = item.assignmentinvslot[3]
                    item.itemslotactive2[3] = item.assignmentinvslot[4]
                    item.itemslotactive2[4] = item.assignmentinvslot[5]
                    item.itemslotactive2[5] = item.assignmentinvslot[6]
                    item.itemslotactive2[6] = item.assignmentinvslot[7]
                    item.itemslotactive2[7] = item.assignmentinvslot[8]
                    item.itemslotactive2[8] = item.assignmentinvslot[9]
                    item.itemslotactive2[9] = item.assignmentinvslot[10]
                    item.itemslotactive2[10] = item.assignmentinvslot[11]
                    item.itemslotactive2[11] = item.assignmentinvslot[12]
                    item.itemslotactive2[12] = item.assignmentinvslot[13]
                    item.itemslotactive2[13] = item.assignmentinvslot[14]
                    item.itemslotactive2[14] = item.assignmentinvslot[15]
                    item.itemslotactive2[15] = item.assignmentinvslot[16]
                    item.itemslotactive2[16] = item.assignmentinvslot[17]                
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] == 0):
                    item.itemslotactive3[0] = item.assignmentinvslot[0]
                    item.itemslotactive3[1] = item.assignmentinvslot[2]
                    item.itemslotactive3[2] = item.assignmentinvslot[3]
                    item.itemslotactive3[3] = item.assignmentinvslot[4]
                    item.itemslotactive3[4] = item.assignmentinvslot[5]
                    item.itemslotactive3[5] = item.assignmentinvslot[6]
                    item.itemslotactive3[6] = item.assignmentinvslot[7]
                    item.itemslotactive3[7] = item.assignmentinvslot[8]
                    item.itemslotactive3[8] = item.assignmentinvslot[9]
                    item.itemslotactive3[9] = item.assignmentinvslot[10]
                    item.itemslotactive3[10] = item.assignmentinvslot[11]
                    item.itemslotactive3[11] = item.assignmentinvslot[12]
                    item.itemslotactive3[12] = item.assignmentinvslot[13]
                    item.itemslotactive3[13] = item.assignmentinvslot[14]
                    item.itemslotactive3[14] = item.assignmentinvslot[15]
                    item.itemslotactive3[15] = item.assignmentinvslot[16]
                    item.itemslotactive3[16] = item.assignmentinvslot[17]                 
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] == 0):
                    item.itemslotactive4[0] = item.assignmentinvslot[0]
                    item.itemslotactive4[1] = item.assignmentinvslot[2]
                    item.itemslotactive4[2] = item.assignmentinvslot[3]
                    item.itemslotactive4[3] = item.assignmentinvslot[4]
                    item.itemslotactive4[4] = item.assignmentinvslot[5]
                    item.itemslotactive4[5] = item.assignmentinvslot[6]
                    item.itemslotactive4[6] = item.assignmentinvslot[7]
                    item.itemslotactive4[7] = item.assignmentinvslot[8]
                    item.itemslotactive4[8] = item.assignmentinvslot[9]
                    item.itemslotactive4[9] = item.assignmentinvslot[10]
                    item.itemslotactive4[10] = item.assignmentinvslot[11]
                    item.itemslotactive4[11] = item.assignmentinvslot[12]
                    item.itemslotactive4[12] = item.assignmentinvslot[13]
                    item.itemslotactive4[13] = item.assignmentinvslot[14]
                    item.itemslotactive4[14] = item.assignmentinvslot[15]
                    item.itemslotactive4[15] = item.assignmentinvslot[16]
                    item.itemslotactive4[16] = item.assignmentinvslot[17]    
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] == 0):
                    item.itemslotactive5[0] = item.assignmentinvslot[0]
                    item.itemslotactive5[1] = item.assignmentinvslot[2]
                    item.itemslotactive5[2] = item.assignmentinvslot[3]
                    item.itemslotactive5[3] = item.assignmentinvslot[4]
                    item.itemslotactive5[4] = item.assignmentinvslot[5]
                    item.itemslotactive5[5] = item.assignmentinvslot[6]
                    item.itemslotactive5[6] = item.assignmentinvslot[7]
                    item.itemslotactive5[7] = item.assignmentinvslot[8]
                    item.itemslotactive5[8] = item.assignmentinvslot[9]
                    item.itemslotactive5[9] = item.assignmentinvslot[10]
                    item.itemslotactive5[10] = item.assignmentinvslot[11]
                    item.itemslotactive5[11] = item.assignmentinvslot[12]
                    item.itemslotactive5[12] = item.assignmentinvslot[13]
                    item.itemslotactive5[13] = item.assignmentinvslot[14]
                    item.itemslotactive5[14] = item.assignmentinvslot[15]
                    item.itemslotactive5[15] = item.assignmentinvslot[16]
                    item.itemslotactive5[16] = item.assignmentinvslot[17]     
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] == 0):
                    item.itemslotactive6[0] = item.assignmentinvslot[0]
                    item.itemslotactive6[1] = item.assignmentinvslot[2]
                    item.itemslotactive6[2] = item.assignmentinvslot[3]
                    item.itemslotactive6[3] = item.assignmentinvslot[4]
                    item.itemslotactive6[4] = item.assignmentinvslot[5]
                    item.itemslotactive6[5] = item.assignmentinvslot[6]
                    item.itemslotactive6[6] = item.assignmentinvslot[7]
                    item.itemslotactive6[7] = item.assignmentinvslot[8]
                    item.itemslotactive6[8] = item.assignmentinvslot[9]
                    item.itemslotactive6[9] = item.assignmentinvslot[10]
                    item.itemslotactive6[10] = item.assignmentinvslot[11]
                    item.itemslotactive6[11] = item.assignmentinvslot[12]
                    item.itemslotactive6[12] = item.assignmentinvslot[13]
                    item.itemslotactive6[13] = item.assignmentinvslot[14]
                    item.itemslotactive6[14] = item.assignmentinvslot[15]
                    item.itemslotactive6[15] = item.assignmentinvslot[16]
                    item.itemslotactive6[16] = item.assignmentinvslot[17]                   
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na przedmioty aktywne są w użyciu')
        if (item.inventoryslot10[4] == lookforinv) and (item.inventoryslot10[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot10
            if item.inventoryslot10[5] == 'armorhead':
                item.itemslothead[0] = item.assignmentinvslot[0]
                item.itemslothead[1] = item.assignmentinvslot[2]
                item.itemslothead[2] = item.assignmentinvslot[3]
                item.itemslothead[3] = item.assignmentinvslot[4]
                item.itemslothead[4] = item.assignmentinvslot[5]
                item.itemslothead[5] = item.assignmentinvslot[6]
                item.itemslothead[6] = item.assignmentinvslot[7]
                item.itemslothead[7] = item.assignmentinvslot[8]
                item.itemslothead[8] = item.assignmentinvslot[9]
                item.itemslothead[9] = item.assignmentinvslot[10]
                item.itemslothead[10] = item.assignmentinvslot[11]
                item.itemslothead[11] = item.assignmentinvslot[12]
                item.itemslothead[12] = item.assignmentinvslot[13]
                item.itemslothead[13] = item.assignmentinvslot[14]
                item.itemslothead[14] = item.assignmentinvslot[15]
                item.itemslothead[15] = item.assignmentinvslot[16]
                item.itemslothead[16] = item.assignmentinvslot[17]
            if item.inventoryslot10[5] == 'armorchest':
                item.itemslotchest[0] = item.assignmentinvslot[0]
                item.itemslotchest[1] = item.assignmentinvslot[2]
                item.itemslotchest[2] = item.assignmentinvslot[3]
                item.itemslotchest[3] = item.assignmentinvslot[4]
                item.itemslotchest[4] = item.assignmentinvslot[5]
                item.itemslotchest[5] = item.assignmentinvslot[6]
                item.itemslotchest[6] = item.assignmentinvslot[7]
                item.itemslotchest[7] = item.assignmentinvslot[8]
                item.itemslotchest[8] = item.assignmentinvslot[9]
                item.itemslotchest[9] = item.assignmentinvslot[10]
                item.itemslotchest[10] = item.assignmentinvslot[11]
                item.itemslotchest[11] = item.assignmentinvslot[12]
                item.itemslotchest[12] = item.assignmentinvslot[13]
                item.itemslotchest[13] = item.assignmentinvslot[14]
                item.itemslotchest[14] = item.assignmentinvslot[15]
                item.itemslotchest[15] = item.assignmentinvslot[16]
                item.itemslotchest[16] = item.assignmentinvslot[17]
            if item.inventoryslot10[5] == 'armorarms':
                item.itemslotarms[0] = item.assignmentinvslot[0]
                item.itemslotarms[1] = item.assignmentinvslot[2]
                item.itemslotarms[2] = item.assignmentinvslot[3]
                item.itemslotarms[3] = item.assignmentinvslot[4]
                item.itemslotarms[4] = item.assignmentinvslot[5]
                item.itemslotarms[5] = item.assignmentinvslot[6]
                item.itemslotarms[6] = item.assignmentinvslot[7]
                item.itemslotarms[7] = item.assignmentinvslot[8]
                item.itemslotarms[8] = item.assignmentinvslot[9]
                item.itemslotarms[9] = item.assignmentinvslot[10]
                item.itemslotarms[10] = item.assignmentinvslot[11]
                item.itemslotarms[11] = item.assignmentinvslot[12]
                item.itemslotarms[12] = item.assignmentinvslot[13]
                item.itemslotarms[13] = item.assignmentinvslot[14]
                item.itemslotarms[14] = item.assignmentinvslot[15]
                item.itemslotarms[15] = item.assignmentinvslot[16]
                item.itemslotarms[16] = item.assignmentinvslot[17]    
            if item.inventoryslot10[5] == 'armorhands':
                item.itemslothands[0] = item.assignmentinvslot[0]
                item.itemslothands[1] = item.assignmentinvslot[2]
                item.itemslothands[2] = item.assignmentinvslot[3]
                item.itemslothands[3] = item.assignmentinvslot[4]
                item.itemslothands[4] = item.assignmentinvslot[5]
                item.itemslothands[5] = item.assignmentinvslot[6]
                item.itemslothands[6] = item.assignmentinvslot[7]
                item.itemslothands[7] = item.assignmentinvslot[8]
                item.itemslothands[8] = item.assignmentinvslot[9]
                item.itemslothands[9] = item.assignmentinvslot[10]
                item.itemslothands[10] = item.assignmentinvslot[11]
                item.itemslothands[11] = item.assignmentinvslot[12]
                item.itemslothands[12] = item.assignmentinvslot[13]
                item.itemslothands[13] = item.assignmentinvslot[14]
                item.itemslothands[14] = item.assignmentinvslot[15]
                item.itemslothands[15] = item.assignmentinvslot[16]
                item.itemslothands[16] = item.assignmentinvslot[17]   
            if item.inventoryslot10[5] == 'armorlegs':
                item.itemslotlegs[0] = item.assignmentinvslot[0]
                item.itemslotlegs[1] = item.assignmentinvslot[2]
                item.itemslotlegs[2] = item.assignmentinvslot[3]
                item.itemslotlegs[3] = item.assignmentinvslot[4]
                item.itemslotlegs[4] = item.assignmentinvslot[5]
                item.itemslotlegs[5] = item.assignmentinvslot[6]
                item.itemslotlegs[6] = item.assignmentinvslot[7]
                item.itemslotlegs[7] = item.assignmentinvslot[8]
                item.itemslotlegs[8] = item.assignmentinvslot[9]
                item.itemslotlegs[9] = item.assignmentinvslot[10]
                item.itemslotlegs[10] = item.assignmentinvslot[11]
                item.itemslotlegs[11] = item.assignmentinvslot[12]
                item.itemslotlegs[12] = item.assignmentinvslot[13]
                item.itemslotlegs[13] = item.assignmentinvslot[14]
                item.itemslotlegs[14] = item.assignmentinvslot[15]
                item.itemslotlegs[15] = item.assignmentinvslot[16]
                item.itemslotlegs[16] = item.assignmentinvslot[17]    
            if item.inventoryslot10[5] == 'armorfoot':
                item.itemslotfoot[0] = item.assignmentinvslot[0]
                item.itemslotfoot[1] = item.assignmentinvslot[2]
                item.itemslotfoot[2] = item.assignmentinvslot[3]
                item.itemslotfoot[3] = item.assignmentinvslot[4]
                item.itemslotfoot[4] = item.assignmentinvslot[5]
                item.itemslotfoot[5] = item.assignmentinvslot[6]
                item.itemslotfoot[6] = item.assignmentinvslot[7]
                item.itemslotfoot[7] = item.assignmentinvslot[8]
                item.itemslotfoot[8] = item.assignmentinvslot[9]
                item.itemslotfoot[9] = item.assignmentinvslot[10]
                item.itemslotfoot[10] = item.assignmentinvslot[11]
                item.itemslotfoot[11] = item.assignmentinvslot[12]
                item.itemslotfoot[12] = item.assignmentinvslot[13]
                item.itemslotfoot[13] = item.assignmentinvslot[14]
                item.itemslotfoot[14] = item.assignmentinvslot[15]
                item.itemslotfoot[15] = item.assignmentinvslot[16]
                item.itemslotfoot[16] = item.assignmentinvslot[17]    
            if item.inventoryslot10[5] == 'armoracc':
                if item.itemslotacc1[0] == 0:    
                    item.itemslotacc1[0] = item.assignmentinvslot[0]
                    item.itemslotacc1[1] = item.assignmentinvslot[2]
                    item.itemslotacc1[2] = item.assignmentinvslot[3]
                    item.itemslotacc1[3] = item.assignmentinvslot[4]
                    item.itemslotacc1[4] = item.assignmentinvslot[5]
                    item.itemslotacc1[5] = item.assignmentinvslot[6]
                    item.itemslotacc1[6] = item.assignmentinvslot[7]
                    item.itemslotacc1[7] = item.assignmentinvslot[8]
                    item.itemslotacc1[8] = item.assignmentinvslot[9]
                    item.itemslotacc1[9] = item.assignmentinvslot[10]
                    item.itemslotacc1[10] = item.assignmentinvslot[11]
                    item.itemslotacc1[11] = item.assignmentinvslot[12]
                    item.itemslotacc1[12] = item.assignmentinvslot[13]
                    item.itemslotacc1[13] = item.assignmentinvslot[14]
                    item.itemslotacc1[14] = item.assignmentinvslot[15]
                    item.itemslotacc1[15] = item.assignmentinvslot[16]
                    item.itemslotacc1[16] = item.assignmentinvslot[17] 
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] == 0):
                    item.itemslotacc2[0] = item.assignmentinvslot[0]
                    item.itemslotacc2[1] = item.assignmentinvslot[2]
                    item.itemslotacc2[2] = item.assignmentinvslot[3]
                    item.itemslotacc2[3] = item.assignmentinvslot[4]
                    item.itemslotacc2[4] = item.assignmentinvslot[5]
                    item.itemslotacc2[5] = item.assignmentinvslot[6]
                    item.itemslotacc2[6] = item.assignmentinvslot[7]
                    item.itemslotacc2[7] = item.assignmentinvslot[8]
                    item.itemslotacc2[8] = item.assignmentinvslot[9]
                    item.itemslotacc2[9] = item.assignmentinvslot[10]
                    item.itemslotacc2[10] = item.assignmentinvslot[11]
                    item.itemslotacc2[11] = item.assignmentinvslot[12]
                    item.itemslotacc2[12] = item.assignmentinvslot[13]
                    item.itemslotacc2[13] = item.assignmentinvslot[14]
                    item.itemslotacc2[14] = item.assignmentinvslot[15]
                    item.itemslotacc2[15] = item.assignmentinvslot[16]
                    item.itemslotacc2[16] = item.assignmentinvslot[17]  
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] == 0):
                    item.itemslotacc3[0] = item.assignmentinvslot[0]
                    item.itemslotacc3[1] = item.assignmentinvslot[2]
                    item.itemslotacc3[2] = item.assignmentinvslot[3]
                    item.itemslotacc3[3] = item.assignmentinvslot[4]
                    item.itemslotacc3[4] = item.assignmentinvslot[5]
                    item.itemslotacc3[5] = item.assignmentinvslot[6]
                    item.itemslotacc3[6] = item.assignmentinvslot[7]
                    item.itemslotacc3[7] = item.assignmentinvslot[8]
                    item.itemslotacc3[8] = item.assignmentinvslot[9]
                    item.itemslotacc3[9] = item.assignmentinvslot[10]
                    item.itemslotacc3[10] = item.assignmentinvslot[11]
                    item.itemslotacc3[11] = item.assignmentinvslot[12]
                    item.itemslotacc3[12] = item.assignmentinvslot[13]
                    item.itemslotacc3[13] = item.assignmentinvslot[14]
                    item.itemslotacc3[14] = item.assignmentinvslot[15]
                    item.itemslotacc3[15] = item.assignmentinvslot[16]
                    item.itemslotacc3[16] = item.assignmentinvslot[17]               
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na akcesoria są w użyciu')
            if item.inventoryslot10[5] == 'armoractive': 
                if (item.itemslotactive1[0] == 0):
                    item.itemslotactive1[0] = item.assignmentinvslot[0]
                    item.itemslotactive1[1] = item.assignmentinvslot[2]
                    item.itemslotactive1[2] = item.assignmentinvslot[3]
                    item.itemslotactive1[3] = item.assignmentinvslot[4]
                    item.itemslotactive1[4] = item.assignmentinvslot[5]
                    item.itemslotactive1[5] = item.assignmentinvslot[6]
                    item.itemslotactive1[6] = item.assignmentinvslot[7]
                    item.itemslotactive1[7] = item.assignmentinvslot[8]
                    item.itemslotactive1[8] = item.assignmentinvslot[9]
                    item.itemslotactive1[9] = item.assignmentinvslot[10]
                    item.itemslotactive1[10] = item.assignmentinvslot[11]
                    item.itemslotactive1[11] = item.assignmentinvslot[12]
                    item.itemslotactive1[12] = item.assignmentinvslot[13]
                    item.itemslotactive1[13] = item.assignmentinvslot[14]
                    item.itemslotactive1[14] = item.assignmentinvslot[15]
                    item.itemslotactive1[15] = item.assignmentinvslot[16]
                    item.itemslotactive1[16] = item.assignmentinvslot[17]           
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] == 0):
                    item.itemslotactive2[0] = item.assignmentinvslot[0]
                    item.itemslotactive2[1] = item.assignmentinvslot[2]
                    item.itemslotactive2[2] = item.assignmentinvslot[3]
                    item.itemslotactive2[3] = item.assignmentinvslot[4]
                    item.itemslotactive2[4] = item.assignmentinvslot[5]
                    item.itemslotactive2[5] = item.assignmentinvslot[6]
                    item.itemslotactive2[6] = item.assignmentinvslot[7]
                    item.itemslotactive2[7] = item.assignmentinvslot[8]
                    item.itemslotactive2[8] = item.assignmentinvslot[9]
                    item.itemslotactive2[9] = item.assignmentinvslot[10]
                    item.itemslotactive2[10] = item.assignmentinvslot[11]
                    item.itemslotactive2[11] = item.assignmentinvslot[12]
                    item.itemslotactive2[12] = item.assignmentinvslot[13]
                    item.itemslotactive2[13] = item.assignmentinvslot[14]
                    item.itemslotactive2[14] = item.assignmentinvslot[15]
                    item.itemslotactive2[15] = item.assignmentinvslot[16]
                    item.itemslotactive2[16] = item.assignmentinvslot[17]                
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] == 0):
                    item.itemslotactive3[0] = item.assignmentinvslot[0]
                    item.itemslotactive3[1] = item.assignmentinvslot[2]
                    item.itemslotactive3[2] = item.assignmentinvslot[3]
                    item.itemslotactive3[3] = item.assignmentinvslot[4]
                    item.itemslotactive3[4] = item.assignmentinvslot[5]
                    item.itemslotactive3[5] = item.assignmentinvslot[6]
                    item.itemslotactive3[6] = item.assignmentinvslot[7]
                    item.itemslotactive3[7] = item.assignmentinvslot[8]
                    item.itemslotactive3[8] = item.assignmentinvslot[9]
                    item.itemslotactive3[9] = item.assignmentinvslot[10]
                    item.itemslotactive3[10] = item.assignmentinvslot[11]
                    item.itemslotactive3[11] = item.assignmentinvslot[12]
                    item.itemslotactive3[12] = item.assignmentinvslot[13]
                    item.itemslotactive3[13] = item.assignmentinvslot[14]
                    item.itemslotactive3[14] = item.assignmentinvslot[15]
                    item.itemslotactive3[15] = item.assignmentinvslot[16]
                    item.itemslotactive3[16] = item.assignmentinvslot[17]                 
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] == 0):
                    item.itemslotactive4[0] = item.assignmentinvslot[0]
                    item.itemslotactive4[1] = item.assignmentinvslot[2]
                    item.itemslotactive4[2] = item.assignmentinvslot[3]
                    item.itemslotactive4[3] = item.assignmentinvslot[4]
                    item.itemslotactive4[4] = item.assignmentinvslot[5]
                    item.itemslotactive4[5] = item.assignmentinvslot[6]
                    item.itemslotactive4[6] = item.assignmentinvslot[7]
                    item.itemslotactive4[7] = item.assignmentinvslot[8]
                    item.itemslotactive4[8] = item.assignmentinvslot[9]
                    item.itemslotactive4[9] = item.assignmentinvslot[10]
                    item.itemslotactive4[10] = item.assignmentinvslot[11]
                    item.itemslotactive4[11] = item.assignmentinvslot[12]
                    item.itemslotactive4[12] = item.assignmentinvslot[13]
                    item.itemslotactive4[13] = item.assignmentinvslot[14]
                    item.itemslotactive4[14] = item.assignmentinvslot[15]
                    item.itemslotactive4[15] = item.assignmentinvslot[16]
                    item.itemslotactive4[16] = item.assignmentinvslot[17]    
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] == 0):
                    item.itemslotactive5[0] = item.assignmentinvslot[0]
                    item.itemslotactive5[1] = item.assignmentinvslot[2]
                    item.itemslotactive5[2] = item.assignmentinvslot[3]
                    item.itemslotactive5[3] = item.assignmentinvslot[4]
                    item.itemslotactive5[4] = item.assignmentinvslot[5]
                    item.itemslotactive5[5] = item.assignmentinvslot[6]
                    item.itemslotactive5[6] = item.assignmentinvslot[7]
                    item.itemslotactive5[7] = item.assignmentinvslot[8]
                    item.itemslotactive5[8] = item.assignmentinvslot[9]
                    item.itemslotactive5[9] = item.assignmentinvslot[10]
                    item.itemslotactive5[10] = item.assignmentinvslot[11]
                    item.itemslotactive5[11] = item.assignmentinvslot[12]
                    item.itemslotactive5[12] = item.assignmentinvslot[13]
                    item.itemslotactive5[13] = item.assignmentinvslot[14]
                    item.itemslotactive5[14] = item.assignmentinvslot[15]
                    item.itemslotactive5[15] = item.assignmentinvslot[16]
                    item.itemslotactive5[16] = item.assignmentinvslot[17]     
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] == 0):
                    item.itemslotactive6[0] = item.assignmentinvslot[0]
                    item.itemslotactive6[1] = item.assignmentinvslot[2]
                    item.itemslotactive6[2] = item.assignmentinvslot[3]
                    item.itemslotactive6[3] = item.assignmentinvslot[4]
                    item.itemslotactive6[4] = item.assignmentinvslot[5]
                    item.itemslotactive6[5] = item.assignmentinvslot[6]
                    item.itemslotactive6[6] = item.assignmentinvslot[7]
                    item.itemslotactive6[7] = item.assignmentinvslot[8]
                    item.itemslotactive6[8] = item.assignmentinvslot[9]
                    item.itemslotactive6[9] = item.assignmentinvslot[10]
                    item.itemslotactive6[10] = item.assignmentinvslot[11]
                    item.itemslotactive6[11] = item.assignmentinvslot[12]
                    item.itemslotactive6[12] = item.assignmentinvslot[13]
                    item.itemslotactive6[13] = item.assignmentinvslot[14]
                    item.itemslotactive6[14] = item.assignmentinvslot[15]
                    item.itemslotactive6[15] = item.assignmentinvslot[16]
                    item.itemslotactive6[16] = item.assignmentinvslot[17]                   
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na przedmioty aktywne są w użyciu')

                                        
                                                                                                                                                                                                           
    if lookforinv == "armoroff": 
        lookforinv = "armor"
        if (item.itemslothead[3] == lookforinv) and (item.itemslothead[1] == ActionInput):
            item.assignmentinvslot[0] = item.itemslothead[0]
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslothead[1]
            item.assignmentinvslot[3] = item.itemslothead[2]
            item.assignmentinvslot[4] = item.itemslothead[3]
            item.assignmentinvslot[5] = item.itemslothead[4]
            item.assignmentinvslot[6] = item.itemslothead[5]
            item.assignmentinvslot[7] = item.itemslothead[6]
            item.assignmentinvslot[8] = item.itemslothead[7]
            item.assignmentinvslot[9] = item.itemslothead[8]
            item.assignmentinvslot[10] = item.itemslothead[9]
            item.assignmentinvslot[11] = item.itemslothead[10]
            item.assignmentinvslot[12] = item.itemslothead[11]
            item.assignmentinvslot[13] = item.itemslothead[12]
            item.assignmentinvslot[14] = item.itemslothead[13]
            item.assignmentinvslot[15] = item.itemslothead[14]
            item.assignmentinvslot[16] = item.itemslothead[15]
            item.assignmentinvslot[17] = item.itemslothead[16]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothead = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothead = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothead = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothead = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothead = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothead = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothead = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothead = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothead = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothead = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0
        if (item.itemslotchest[3] == lookforinv) and (item.itemslotchest[1] == ActionInput):
            item.assignmentinvslot[0] = item.itemslotchest[0]
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotchest[1]
            item.assignmentinvslot[3] = item.itemslotchest[2]
            item.assignmentinvslot[4] = item.itemslotchest[3]
            item.assignmentinvslot[5] = item.itemslotchest[4]
            item.assignmentinvslot[6] = item.itemslotchest[5]
            item.assignmentinvslot[7] = item.itemslotchest[6]
            item.assignmentinvslot[8] = item.itemslotchest[7]
            item.assignmentinvslot[9] = item.itemslotchest[8]
            item.assignmentinvslot[10] = item.itemslotchest[9]
            item.assignmentinvslot[11] = item.itemslotchest[10]
            item.assignmentinvslot[12] = item.itemslotchest[11]
            item.assignmentinvslot[13] = item.itemslotchest[12]
            item.assignmentinvslot[14] = item.itemslotchest[13]
            item.assignmentinvslot[15] = item.itemslotchest[14]
            item.assignmentinvslot[16] = item.itemslotchest[15]
            item.assignmentinvslot[17] = item.itemslotchest[16]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotchest = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotchest = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotchest = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotchest = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotchest = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotchest = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotchest = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotchest = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotchest = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotchest = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0
        if (item.itemslotarms[3] == lookforinv) and (item.itemslotarms[1] == ActionInput):
            item.assignmentinvslot[0] = item.itemslotarms[0]
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotarms[1]
            item.assignmentinvslot[3] = item.itemslotarms[2]
            item.assignmentinvslot[4] = item.itemslotarms[3]
            item.assignmentinvslot[5] = item.itemslotarms[4]
            item.assignmentinvslot[6] = item.itemslotarms[5]
            item.assignmentinvslot[7] = item.itemslotarms[6]
            item.assignmentinvslot[8] = item.itemslotarms[7]
            item.assignmentinvslot[9] = item.itemslotarms[8]
            item.assignmentinvslot[10] = item.itemslotarms[9]
            item.assignmentinvslot[11] = item.itemslotarms[10]
            item.assignmentinvslot[12] = item.itemslotarms[11]
            item.assignmentinvslot[13] = item.itemslotarms[12]
            item.assignmentinvslot[14] = item.itemslotarms[13]
            item.assignmentinvslot[15] = item.itemslotarms[14]
            item.assignmentinvslot[16] = item.itemslotarms[15]
            item.assignmentinvslot[17] = item.itemslotarms[16]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotarms = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotarms = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotarms = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotarms = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotarms = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotarms = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotarms = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotarms = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotarms = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotarms = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0    
        if (item.itemslothands[3] == lookforinv) and (item.itemslothands[1] == ActionInput):
            item.assignmentinvslot[0] = item.itemslothands[0]
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslothands[1]
            item.assignmentinvslot[3] = item.itemslothands[2]
            item.assignmentinvslot[4] = item.itemslothands[3]
            item.assignmentinvslot[5] = item.itemslothands[4]
            item.assignmentinvslot[6] = item.itemslothands[5]
            item.assignmentinvslot[7] = item.itemslothands[6]
            item.assignmentinvslot[8] = item.itemslothands[7]
            item.assignmentinvslot[9] = item.itemslothands[8]
            item.assignmentinvslot[10] = item.itemslothands[9]
            item.assignmentinvslot[11] = item.itemslothands[10]
            item.assignmentinvslot[12] = item.itemslothands[11]
            item.assignmentinvslot[13] = item.itemslothands[12]
            item.assignmentinvslot[14] = item.itemslothands[13]
            item.assignmentinvslot[15] = item.itemslothands[14]
            item.assignmentinvslot[16] = item.itemslothands[15]
            item.assignmentinvslot[17] = item.itemslothands[16]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothands = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothands = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothands = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothands = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothands = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothands = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothands = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothands = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothands = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothands = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0
        if (item.itemslotlegs[3] == lookforinv) and (item.itemslotlegs[1] == ActionInput):
            item.assignmentinvslot[0] = item.itemslotlegs[0]
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotlegs[1]
            item.assignmentinvslot[3] = item.itemslotlegs[2]
            item.assignmentinvslot[4] = item.itemslotlegs[3]
            item.assignmentinvslot[5] = item.itemslotlegs[4]
            item.assignmentinvslot[6] = item.itemslotlegs[5]
            item.assignmentinvslot[7] = item.itemslotlegs[6]
            item.assignmentinvslot[8] = item.itemslotlegs[7]
            item.assignmentinvslot[9] = item.itemslotlegs[8]
            item.assignmentinvslot[10] = item.itemslotlegs[9]
            item.assignmentinvslot[11] = item.itemslotlegs[10]
            item.assignmentinvslot[12] = item.itemslotlegs[11]
            item.assignmentinvslot[13] = item.itemslotlegs[12]
            item.assignmentinvslot[14] = item.itemslotlegs[13]
            item.assignmentinvslot[15] = item.itemslotlegs[14]
            item.assignmentinvslot[16] = item.itemslotlegs[15]
            item.assignmentinvslot[17] = item.itemslotlegs[16]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotlegs = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotlegs = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotlegs = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotlegs = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotlegs = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotlegs = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotlegs = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotlegs = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotlegs = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotlegs = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0            
        if (item.itemslotfoot[3] == lookforinv) and (item.itemslotfoot[1] == ActionInput):
            item.assignmentinvslot[0] = item.itemslotfoot[0]
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotfoot[1]
            item.assignmentinvslot[3] = item.itemslotfoot[2]
            item.assignmentinvslot[4] = item.itemslotfoot[3]
            item.assignmentinvslot[5] = item.itemslotfoot[4]
            item.assignmentinvslot[6] = item.itemslotfoot[5]
            item.assignmentinvslot[7] = item.itemslotfoot[6]
            item.assignmentinvslot[8] = item.itemslotfoot[7]
            item.assignmentinvslot[9] = item.itemslotfoot[8]
            item.assignmentinvslot[10] = item.itemslotfoot[9]
            item.assignmentinvslot[11] = item.itemslotfoot[10]
            item.assignmentinvslot[12] = item.itemslotfoot[11]
            item.assignmentinvslot[13] = item.itemslotfoot[12]
            item.assignmentinvslot[14] = item.itemslotfoot[13]
            item.assignmentinvslot[15] = item.itemslotfoot[14]
            item.assignmentinvslot[16] = item.itemslotfoot[15]
            item.assignmentinvslot[17] = item.itemslotfoot[16]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotfoot = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotfoot = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotfoot = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotfoot = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotfoot = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotfoot = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotfoot = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotfoot = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotfoot = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotfoot = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0            
        if (item.itemslotacc1[3] == lookforinv) and (item.itemslotacc1[1] == ActionInput):
            item.assignmentinvslot[0] = item.itemslotacc1[0]
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotacc1[1]
            item.assignmentinvslot[3] = item.itemslotacc1[2]
            item.assignmentinvslot[4] = item.itemslotacc1[3]
            item.assignmentinvslot[5] = item.itemslotacc1[4]
            item.assignmentinvslot[6] = item.itemslotacc1[5]
            item.assignmentinvslot[7] = item.itemslotacc1[6]
            item.assignmentinvslot[8] = item.itemslotacc1[7]
            item.assignmentinvslot[9] = item.itemslotacc1[8]
            item.assignmentinvslot[10] = item.itemslotacc1[9]
            item.assignmentinvslot[11] = item.itemslotacc1[10]
            item.assignmentinvslot[12] = item.itemslotacc1[11]
            item.assignmentinvslot[13] = item.itemslotacc1[12]
            item.assignmentinvslot[14] = item.itemslotacc1[13]
            item.assignmentinvslot[15] = item.itemslotacc1[14]
            item.assignmentinvslot[16] = item.itemslotacc1[15]
            item.assignmentinvslot[17] = item.itemslotacc1[16]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0            
        if (item.itemslotacc2[3] == lookforinv) and (item.itemslotacc2[1] == ActionInput):
            item.assignmentinvslot[0] = item.itemslotacc2[0]
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotacc2[1]
            item.assignmentinvslot[3] = item.itemslotacc2[2]
            item.assignmentinvslot[4] = item.itemslotacc2[3]
            item.assignmentinvslot[5] = item.itemslotacc2[4]
            item.assignmentinvslot[6] = item.itemslotacc2[5]
            item.assignmentinvslot[7] = item.itemslotacc2[6]
            item.assignmentinvslot[8] = item.itemslotacc2[7]
            item.assignmentinvslot[9] = item.itemslotacc2[8]
            item.assignmentinvslot[10] = item.itemslotacc2[9]
            item.assignmentinvslot[11] = item.itemslotacc2[10]
            item.assignmentinvslot[12] = item.itemslotacc2[11]
            item.assignmentinvslot[13] = item.itemslotacc2[12]
            item.assignmentinvslot[14] = item.itemslotacc2[13]
            item.assignmentinvslot[15] = item.itemslotacc2[14]
            item.assignmentinvslot[16] = item.itemslotacc2[15]
            item.assignmentinvslot[17] = item.itemslotacc2[16]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0            
        if (item.itemslotacc3[3] == lookforinv) and (item.itemslotacc3[1] == ActionInput):
            item.assignmentinvslot[0] = item.itemslotacc3[0]
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotacc3[1]
            item.assignmentinvslot[3] = item.itemslotacc3[2]
            item.assignmentinvslot[4] = item.itemslotacc3[3]
            item.assignmentinvslot[5] = item.itemslotacc3[4]
            item.assignmentinvslot[6] = item.itemslotacc3[5]
            item.assignmentinvslot[7] = item.itemslotacc3[6]
            item.assignmentinvslot[8] = item.itemslotacc3[7]
            item.assignmentinvslot[9] = item.itemslotacc3[8]
            item.assignmentinvslot[10] = item.itemslotacc3[9]
            item.assignmentinvslot[11] = item.itemslotacc3[10]
            item.assignmentinvslot[12] = item.itemslotacc3[11]
            item.assignmentinvslot[13] = item.itemslotacc3[12]
            item.assignmentinvslot[14] = item.itemslotacc3[13]
            item.assignmentinvslot[15] = item.itemslotacc3[14]
            item.assignmentinvslot[16] = item.itemslotacc3[15]
            item.assignmentinvslot[17] = item.itemslotacc3[16]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0            
        if (item.itemslotactive1[3] == lookforinv) and (item.itemslotactive1[1] == ActionInput):
            item.assignmentinvslot[0] = item.itemslotactive1[0]
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotactive1[1]
            item.assignmentinvslot[3] = item.itemslotactive1[2]
            item.assignmentinvslot[4] = item.itemslotactive1[3]
            item.assignmentinvslot[5] = item.itemslotactive1[4]
            item.assignmentinvslot[6] = item.itemslotactive1[5]
            item.assignmentinvslot[7] = item.itemslotactive1[6]
            item.assignmentinvslot[8] = item.itemslotactive1[7]
            item.assignmentinvslot[9] = item.itemslotactive1[8]
            item.assignmentinvslot[10] = item.itemslotactive1[9]
            item.assignmentinvslot[11] = item.itemslotactive1[10]
            item.assignmentinvslot[12] = item.itemslotactive1[11]
            item.assignmentinvslot[13] = item.itemslotactive1[12]
            item.assignmentinvslot[14] = item.itemslotactive1[13]
            item.assignmentinvslot[15] = item.itemslotactive1[14]
            item.assignmentinvslot[16] = item.itemslotactive1[15]
            item.assignmentinvslot[17] = item.itemslotactive1[16]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0            
        if (item.itemslotactive2[3] == lookforinv) and (item.itemslotactive2[1] == ActionInput):
            item.assignmentinvslot[0] = item.itemslotactive2[0]
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotactive2[1]
            item.assignmentinvslot[3] = item.itemslotactive2[2]
            item.assignmentinvslot[4] = item.itemslotactive2[3]
            item.assignmentinvslot[5] = item.itemslotactive2[4]
            item.assignmentinvslot[6] = item.itemslotactive2[5]
            item.assignmentinvslot[7] = item.itemslotactive2[6]
            item.assignmentinvslot[8] = item.itemslotactive2[7]
            item.assignmentinvslot[9] = item.itemslotactive2[8]
            item.assignmentinvslot[10] = item.itemslotactive2[9]
            item.assignmentinvslot[11] = item.itemslotactive2[10]
            item.assignmentinvslot[12] = item.itemslotactive2[11]
            item.assignmentinvslot[13] = item.itemslotactive2[12]
            item.assignmentinvslot[14] = item.itemslotactive2[13]
            item.assignmentinvslot[15] = item.itemslotactive2[14]
            item.assignmentinvslot[16] = item.itemslotactive2[15]
            item.assignmentinvslot[17] = item.itemslotactive2[16]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0            
        if (item.itemslotactive3[3] == lookforinv) and (item.itemslotactive3[1] == ActionInput):
            item.assignmentinvslot[0] = item.itemslotactive3[0]
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotactive3[1]
            item.assignmentinvslot[3] = item.itemslotactive3[2]
            item.assignmentinvslot[4] = item.itemslotactive3[3]
            item.assignmentinvslot[5] = item.itemslotactive3[4]
            item.assignmentinvslot[6] = item.itemslotactive3[5]
            item.assignmentinvslot[7] = item.itemslotactive3[6]
            item.assignmentinvslot[8] = item.itemslotactive3[7]
            item.assignmentinvslot[9] = item.itemslotactive3[8]
            item.assignmentinvslot[10] = item.itemslotactive3[9]
            item.assignmentinvslot[11] = item.itemslotactive3[10]
            item.assignmentinvslot[12] = item.itemslotactive3[11]
            item.assignmentinvslot[13] = item.itemslotactive3[12]
            item.assignmentinvslot[14] = item.itemslotactive3[13]
            item.assignmentinvslot[15] = item.itemslotactive3[14]
            item.assignmentinvslot[16] = item.itemslotactive3[15]
            item.assignmentinvslot[17] = item.itemslotactive3[16]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0
        if (item.itemslotactive4[3] == lookforinv) and (item.itemslotactive4[1] == ActionInput):
            item.assignmentinvslot[0] = item.itemslotactive4[0]
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotactive4[1]
            item.assignmentinvslot[3] = item.itemslotactive4[2]
            item.assignmentinvslot[4] = item.itemslotactive4[3]
            item.assignmentinvslot[5] = item.itemslotactive4[4]
            item.assignmentinvslot[6] = item.itemslotactive4[5]
            item.assignmentinvslot[7] = item.itemslotactive4[6]
            item.assignmentinvslot[8] = item.itemslotactive4[7]
            item.assignmentinvslot[9] = item.itemslotactive4[8]
            item.assignmentinvslot[10] = item.itemslotactive4[9]
            item.assignmentinvslot[11] = item.itemslotactive4[10]
            item.assignmentinvslot[12] = item.itemslotactive4[11]
            item.assignmentinvslot[13] = item.itemslotactive4[12]
            item.assignmentinvslot[14] = item.itemslotactive4[13]
            item.assignmentinvslot[15] = item.itemslotactive4[14]
            item.assignmentinvslot[16] = item.itemslotactive4[15]
            item.assignmentinvslot[17] = item.itemslotactive4[16]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive4 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive4 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive4 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive4 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive4 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive4 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive4 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive4 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive4 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive4 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0
        if (item.itemslotactive5[3] == lookforinv) and (item.itemslotactive5[1] == ActionInput):
            item.assignmentinvslot[0] = item.itemslotactive5[0]
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotactive5[1]
            item.assignmentinvslot[3] = item.itemslotactive5[2]
            item.assignmentinvslot[4] = item.itemslotactive5[3]
            item.assignmentinvslot[5] = item.itemslotactive5[4]
            item.assignmentinvslot[6] = item.itemslotactive5[5]
            item.assignmentinvslot[7] = item.itemslotactive5[6]
            item.assignmentinvslot[8] = item.itemslotactive5[7]
            item.assignmentinvslot[9] = item.itemslotactive5[8]
            item.assignmentinvslot[10] = item.itemslotactive5[9]
            item.assignmentinvslot[11] = item.itemslotactive5[10]
            item.assignmentinvslot[12] = item.itemslotactive5[11]
            item.assignmentinvslot[13] = item.itemslotactive5[12]
            item.assignmentinvslot[14] = item.itemslotactive5[13]
            item.assignmentinvslot[15] = item.itemslotactive5[14]
            item.assignmentinvslot[16] = item.itemslotactive5[15]
            item.assignmentinvslot[17] = item.itemslotactive5[16]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive5 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive5 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive5 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive5 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive5 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive5 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive5 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive5 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive5 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive5 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0
        if (item.itemslotactive6[3] == lookforinv) and (item.itemslotactive6[1] == ActionInput):
            item.assignmentinvslot[0] = item.itemslotactive6[0]
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotactive6[1]
            item.assignmentinvslot[3] = item.itemslotactive6[2]
            item.assignmentinvslot[4] = item.itemslotactive6[3]
            item.assignmentinvslot[5] = item.itemslotactive6[4]
            item.assignmentinvslot[6] = item.itemslotactive6[5]
            item.assignmentinvslot[7] = item.itemslotactive6[6]
            item.assignmentinvslot[8] = item.itemslotactive6[7]
            item.assignmentinvslot[9] = item.itemslotactive6[8]
            item.assignmentinvslot[10] = item.itemslotactive6[9]
            item.assignmentinvslot[11] = item.itemslotactive6[10]
            item.assignmentinvslot[12] = item.itemslotactive6[11]
            item.assignmentinvslot[13] = item.itemslotactive6[12]
            item.assignmentinvslot[14] = item.itemslotactive6[13]
            item.assignmentinvslot[15] = item.itemslotactive6[14]
            item.assignmentinvslot[16] = item.itemslotactive6[15]
            item.assignmentinvslot[17] = item.itemslotactive6[16]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive6 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive6 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive6 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive6 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive6 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive6 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive6 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive6 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive6 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive6 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0
        
    if lookforinv == "weapon": #do zrobienia
        if (item.inventoryslot1[4] == lookforinv) and (item.inventoryslot1[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot1        









        
    if lookforinv == "weaponoff":
        lookforinv = "weapon"
        if (item.itemslotweapon1[3] == lookforinv) and (item.itemslotweapon1[1] == ActionInput):
            item.assignmentinvslot[0] = item.itemslotweapon1[0]
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotweapon1[1]
            item.assignmentinvslot[3] = item.itemslotweapon1[2]
            item.assignmentinvslot[4] = item.itemslotweapon1[3]
            item.assignmentinvslot[5] = item.itemslotweapon1[4]
            item.assignmentinvslot[6] = item.itemslotweapon1[5]
            item.assignmentinvslot[7] = item.itemslotweapon1[6]
            item.assignmentinvslot[8] = item.itemslotweapon1[7]
            item.assignmentinvslot[9] = item.itemslotweapon1[8]
            item.assignmentinvslot[10] = item.itemslotweapon1[9]
            item.assignmentinvslot[11] = item.itemslotweapon1[10]
            item.assignmentinvslot[12] = item.itemslotweapon1[11]
            item.assignmentinvslot[13] = item.itemslotweapon1[12]
            item.assignmentinvslot[14] = item.itemslotweapon1[13]
            item.assignmentinvslot[15] = item.itemslotweapon1[14]
            item.assignmentinvslot[16] = item.itemslotweapon1[15]
            item.assignmentinvslot[17] = item.itemslotweapon1[16]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0
        if (item.itemslotweapon2[3] == lookforinv) and (item.itemslotweapon2[1] == ActionInput):
            item.assignmentinvslot[0] = item.itemslotweapon2[0]
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotweapon2[1]
            item.assignmentinvslot[3] = item.itemslotweapon2[2]
            item.assignmentinvslot[4] = item.itemslotweapon2[3]
            item.assignmentinvslot[5] = item.itemslotweapon2[4]
            item.assignmentinvslot[6] = item.itemslotweapon2[5]
            item.assignmentinvslot[7] = item.itemslotweapon2[6]
            item.assignmentinvslot[8] = item.itemslotweapon2[7]
            item.assignmentinvslot[9] = item.itemslotweapon2[8]
            item.assignmentinvslot[10] = item.itemslotweapon2[9]
            item.assignmentinvslot[11] = item.itemslotweapon2[10]
            item.assignmentinvslot[12] = item.itemslotweapon2[11]
            item.assignmentinvslot[13] = item.itemslotweapon2[12]
            item.assignmentinvslot[14] = item.itemslotweapon2[13]
            item.assignmentinvslot[15] = item.itemslotweapon2[14]
            item.assignmentinvslot[16] = item.itemslotweapon2[15]
            item.assignmentinvslot[17] = item.itemslotweapon2[16]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0
        
    return item
def lookforinvtype(ActionInput):
    if ActionInput == "ekwipunek":
        lookfornamesinv(item)
        lookforuseditems(item)
        lookforwornitems(item)
        print('')
        print('')
        
def lookfornamesinv(item):
    print("Twój Ekwipunek:")
    if item.inventoryslot1[0] != 0:
        print(item.inventoryslot1[1], item.inventoryslot1[2])
    if item.inventoryslot2[0] != 0:
        print(item.inventoryslot2[1], item.inventoryslot2[2])
    if item.inventoryslot3[0] != 0:
        print(item.inventoryslot3[1], item.inventoryslot3[2])
    if item.inventoryslot4[0] != 0:
        print(item.inventoryslot4[1], item.inventoryslot4[2])
    if item.inventoryslot5[0] != 0:
        print(item.inventoryslot5[1], item.inventoryslot5[2])
    if item.inventoryslot6[0] != 0:
        print(item.inventoryslot6[1], item.inventoryslot6[2])
    if item.inventoryslot7[0] != 0:
        print(item.inventoryslot7[1], item.inventoryslot7[2])
    if item.inventoryslot8[0] != 0:
        print(item.inventoryslot8[1], item.inventoryslot8[2])
    if item.inventoryslot9[0] != 0:
        print(item.inventoryslot9[1], item.inventoryslot9[2])
    if item.inventoryslot10[0] != 0:
        print(item.inventoryslot10[1], item.inventoryslot10[2])
def lookforuseditems(item):
    print("Twój Oręż i Używane Przedmioty:")
    if item.itemslotweapon1[0] != 0:
        print(item.itemslotweapon1[1])
    if item.itemslotweapon2[0] != 0:
        print(item.itemslotweapon2[1])
    if item.itemslotactive1[0] != 0:
        print(item.itemslotactive1[1])
    if item.itemslotactive2[0] != 0:
        print(item.itemslotactive2[1])
    if item.itemslotactive3[0] != 0:
        print(item.itemslotactive3[1])
    if item.itemslotactive4[0] != 0:
        print(item.itemslotactive4[1])
    if item.itemslotactive5[0] != 0:
        print(item.itemslotactive5[1])
    if item.itemslotactive6[0] != 0:
        print(item.itemslotactive6[1])
def lookforwornitems(item):
    print("Twoja Zbroja i Akcesoria:")
    if item.itemslothead[0] != 0:
        print(item.itemslothead[1])
    if item.itemslotchest[0] != 0:
        print(item.itemslotchest[1])
    if item.itemslotarms[0] != 0:
        print(item.itemslotarms[1])
    if item.itemslothands[0] != 0:
        print(item.itemslothands[1])
    if item.itemslotlegs[0] != 0:
        print(item.itemslotlegs[1])
    if item.itemslotfoot[0] != 0:
        print(item.itemslotfoot[1])
    if item.itemslotacc1[0] != 0:
        print(item.itemslotacc1[1])
    if item.itemslotacc2[0] != 0:
        print(item.itemslotacc2[1])
    if item.itemslotacc3[0] != 0:
        print(item.itemslotacc3[1])
def DebugAdditem(item):
    print("slot nr 1")
    print("indeks 0 (istnienie) =")
    item.assignmentinvslot[0] = int(input())
    print("indeks 1 (ilość) =")
    item.assignmentinvslot[1] = int(input())
    print("indeks 2 (nazwa) =")
    item.assignmentinvslot[2] = str(input())
    print("indeks 3 (opis) =")
    item.assignmentinvslot[3] = str(input())
    print("indeks 4 (typ) =")
    item.assignmentinvslot[4] = str(input())
    print("indeks 5 (podtyp) =")
    item.assignmentinvslot[5] = str(input())
    print("indeks 6 (+hp) =")
    item.assignmentinvslot[6] = int(input())
    print("indeks 7 (+mp) =")
    item.assignmentinvslot[7] = int(input())
    print("indeks 8 (maxhp) =")
    item.assignmentinvslot[8] = int(input())
    print("indeks 9 (maxmp) =")
    item.assignmentinvslot[9] = int(input())
    print("indeks 10 (+exp) =")
    item.assignmentinvslot[10] = int(input())
    print("indeks 11 (str) =")
    item.assignmentinvslot[11] = int(input())
    print("indeks 12 (dex) =")
    item.assignmentinvslot[12] = int(input())
    print("indeks 13 (int) =")
    item.assignmentinvslot[13] = int(input())
    print("indeks 14 (end) =")
    item.assignmentinvslot[14] = int(input())
    print("indeks 15 (luck) =")
    item.assignmentinvslot[15] = int(input())
    print("indeks 16 (dmg broni) =")
    item.assignmentinvslot[16] = int(input())
    print("indeks 17 (ID) =")
    item.assignmentinvslot[17] = int(input())
    print("Podaj slot w ekwipunku dla przedmiotu (1-10)")
    debugslotchoice = int(input())
    if debugslotchoice == 1:
        item.inventoryslot1 = item.assignmentinvslot
    if debugslotchoice == 2:
        item.inventoryslot2 = item.assignmentinvslot
    if debugslotchoice == 3:
        item.inventoryslot3 = item.assignmentinvslot
    if debugslotchoice == 4:
        item.inventoryslot4 = item.assignmentinvslot
    if debugslotchoice == 5:
        item.inventoryslot5 = item.assignmentinvslot
    if debugslotchoice == 6:
        item.inventoryslot6 = item.assignmentinvslot
    if debugslotchoice == 7:
        item.inventoryslot7 = item.assignmentinvslot
    if debugslotchoice == 8:
        item.inventoryslot8 = item.assignmentinvslot
    if debugslotchoice == 9:
        item.inventoryslot9 = item.assignmentinvslot
    if debugslotchoice == 10:
        item.inventoryslot10 = item.assignmentinvslot
    return item
    
    
#####EKWIPUNEK#####
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
    

def ActionCheck(ActionInput,Lokacja,LocMoveset,item,lookforinv): #nie testowane, powiedzmy że działa
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
            print("...")
    if ActionInput in DebugAction:
        if ActionInput == 'debug':
            print("Jakieś dane tu się będą pokazywać")
        if ActionInput == 'additem':
            DebugAdditem(item)
     #NIŻEJ ZMIENIŁEM or NA and   
    if (ActionInput not in MovementAction) and (ActionInput not in OtherAction) and (ActionInput not in DebugAction):
        print("???")
    return ActionInput, Lokacja, LocMoveset, item, lookforinv

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
#####GŁÓWNY MODUŁ#####
    


ActionInput = ""
start = 1
Lokacja = 1
lookforinv = ''
item = Inventory(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
defineinventory(item)
#Staty = PlayerStats("edgy", 100, 20, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
#Staty.PlayerName()
#print(Staty.StatDisplay())
while Lokacja != 0: #lokacja 0 to GAME OVER
    LocDescCheck(Lokacja)
    LocMoveset=LocMovesetCheck(Lokacja)
    ActionInput = input().lower()
    #to zmieniłem i TO JEST KLUCZOWE:
    (ActionInput, Lokacja, LocMoveset, item, lookforinv)=ActionCheck(ActionInput,Lokacja,LocMoveset,item,lookforinv)
    itemuse(lookforinv,ActionInput)
    lookforinventory(lookforinv,ActionInput,item)
    
    
    

    
