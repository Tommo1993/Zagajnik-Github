class Inventory:
    def __init__(item, gold, X, itemslotactive1, itemslotactive2, itemslotactive3, itemslotactive4, itemslotactive5, itemslotactive6, itemslotweapon1, itemslotweapon2, itemslothead, itemslotchest, itemslotarms, itemslothands, itemslotlegs, itemslotfoot, itemslotacc1, itemslotacc2, itemslotacc3, inventoryslot1, inventoryslot2, inventoryslot3, inventoryslot4, inventoryslot5, inventoryslot6, inventoryslot7, inventoryslot8, inventoryslot9, inventoryslot10, assignmentinvslot):
        item.gold=0
        item.X=0
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
    def itemuse(lookforinv,ActionInput):
        if ActionInput == 'zjedz':
            print("Co chciałbyś zjeść?")
            ActionInput = input().lower()
            lookforinv="food"
        if ActionInput == 'użyj':
            print("Co chciałbyś użyć?")
            ActionInput = input().lower()
            lookforinv="consumable"
        if ActionInput == 'opis':
            print("O którym przedmiocie chcesz wiedzieć więcej?")
            ActionInput = input().lower()
            lookforinv="desc"
        if ActionInput == 'ubierz':
            print("Co chciałbyś ubrać na siebię?")
            ActionInput = input().lower()
            lookforinv="armor"
        if ActionInput == 'dobądź':
            print("Jaką broń chciałbyś dobyć?")
            ActionInput = input().lower()
            lookforinv="weapon"
        if ActionInput == 'zdejmij':
            print("Co chciałbyś zdjąć z siebie?")
            ActionInput = input().lower()
            lookforinv="armor"
        if ActionInput == 'schowaj':
            print("Jaką broń chciałbyś schować?")
            ActionInput = input().lower()
            lookforinv="weapon"
        if ActionInput == 'upuść':
            print("Jaki przedmiot chciałbyś upuścić? Tej akcji nie można cofnąć! (Wybierz przedmiot nie używany przez ciebię)")
            ActionInput = input().lower()
    def lookforinventory(lookforinv,ActionInput,player,item):
        if lookforinv == "food":
            if (item.inventoryslot1[4] == lookforinv) and (item.inventoryslot1[2] == ActionInput):
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
        if lookforinv == "armor":
            print()
        if lookforinv == "weapon":
            print()
    def lookforinvtype(ActionInput):
        if ActionInput == "ekwipunek":
            lookfornamesinv()
            lookforuseditems()
            lookforwornitems()
    def lookfornamesinv(item):
        print("Twój Ekwipunek:")
        print(item.inventoryslot1[1], item.inventoryslot1[2])
        print(item.inventoryslot2[1], item.inventoryslot2[2])
        print(item.inventoryslot3[1], item.inventoryslot3[2])
        print(item.inventoryslot4[1], item.inventoryslot4[2])
        print(item.inventoryslot5[1], item.inventoryslot5[2])
        print(item.inventoryslot6[1], item.inventoryslot6[2])
        print(item.inventoryslot7[1], item.inventoryslot7[2])
        print(item.inventoryslot8[1], item.inventoryslot8[2])
        print(item.inventoryslot9[1], item.inventoryslot9[2])
        print(item.inventoryslot10[1], item.inventoryslot10[2])
    def lookforuseditems(item):
        print("Twój Oręż i Używane Przedmioty:")
        print(item.itemslotweapon1[1])
        print(item.itemslotweapon2[1])
        print(item.itemslotactive1[1])
        print(item.itemslotactive2[1])
        print(item.itemslotactive3[1])
        print(item.itemslotactive4[1])
        print(item.itemslotactive5[1])
        print(item.itemslotactive6[1])
    def lookforwornitems(item):
        print("Twoja Zbroja i Akcesoria:")
        print(item.itemslothead[1])
        print(item.itemslotchest[1])
        print(item.itemslotarms[1])
        print(item.itemslothands[1])
        print(item.itemslotlegs[1])
        print(item.itemslotfoot[1])
        print(item.itemslotacc1[1])
        print(item.itemslotacc2[1])
        print(item.itemslotacc3[1])
    def ttt1(LocMoveset):
        print(LocMoveset)
        if LocMoveset[4] == 1:
            print("win")
        if LocMoveset[4] != 1:
            print("sumting wong")
        
    

